from transformers import AutoTokenizer
from diacritics import ALL_DIACRITICS
from collections import Counter
import pandas as pd

model_filepath = "../alephbert"
tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(model_filepath)

## Remove diacritics before tokenization to mitigate indexing issues
def strip_diacritics(text: str) -> str:
    return "".join(ch for ch in text if ch not in ALL_DIACRITICS)

## Map diacritics to the character index of the stripped word
def original_to_stripped_index(word: str, original_index: int) -> int:
    last_base_index = -1

    for i, ch in enumerate(word):
        if ch not in ALL_DIACRITICS:
            last_base_index += 1

        if i == original_index:
            if last_base_index < 0:
                raise ValueError("Diacritic before any base letter")
            return last_base_index

    raise ValueError("Original index out of bounds")

## Get subword spans --- (start, end)
def get_subword_spans(subwords: list[str]) -> list[tuple[int, int]]:
    spans = []
    cursor = 0
    for subword in subwords:
        start = cursor
        end = cursor + len(subword)
        spans.append((start, end))
        cursor = end
    return spans

## Get character index for the diacritics --- (diacritic_char, word_char_index)
def get_diacritics_with_char_index(
    pretokens: list[str],
) -> list[list[tuple[str, int]]]:
    all_maps = []
    for token in pretokens:
        diacritic_map = []
        for i, ch in enumerate(token):
            if ch in ALL_DIACRITICS:
                diacritic_map.append((ch, i))
        all_maps.append(diacritic_map)
    return all_maps

## Count the frequencies of diacritics and the diacritic, character relations
def collect_diacritic_freqs(word: str):
    diacritic_freq = Counter()
    relation_freq = Counter()

    last_base_char = None

    for ch in word:
        if ch in ALL_DIACRITICS:
            diacritic_freq[ch] += 1

            if last_base_char is not None:
                relation_freq[(last_base_char, ch)] += 1
        else:
            last_base_char = ch

    return diacritic_freq, relation_freq

'''hebrew_pretokens: list[str] = (
    "וַיִּשְׁמַ֗ע אֶת־דִּבְרֵ֤י בְנֵֽי־לָבָן֙ לֵאמֹ֔ר לָקַ֣ח יַעֲקֹ֔ב "
    "אֵ֖ת כָּל־אֲשֶׁ֣ר לְאָבִ֑ינוּ וּמֵאֲשֶׁ֣ר לְאָבִ֔ינוּ "
    "עָשָׂ֕ה אֵ֥ת כָּל־הַכָּבֹ֖ד הַזֶּֽה׃"
).split()'''

## Load in the hebrew bible pretokens parquet file
df = pd.read_parquet("hebrew_bible_pretokens.parquet")
hebrew_pretokens = (
    df.iloc[:, 0]
    .dropna()
    .astype(str)
    .str.strip()          
    .loc[lambda s: s != ""]
    .tolist()
)

clean_pretokens: list[str] = [strip_diacritics(w) for w in hebrew_pretokens]

## Get character to subword mappings
character_to_subword_mappings: list[dict[int, int]] = []

for clean_pretoken in clean_pretokens:
    subwords = tokenizer.tokenize(clean_pretoken)
    character_index = 0

    mapping: dict[int, int] = {}
    for subword_index, subword in enumerate(subwords):
        for _ in subword:
            mapping[character_index] = subword_index
            character_index += 1

    character_to_subword_mappings.append(mapping)

## Align diacritics with subwords 
hebrew_diacritics = get_diacritics_with_char_index(hebrew_pretokens)

## Final output per word:
# (diacritic_char, original_char_index, subword_index, subword_char_index)
diacritic_locations: list[list[tuple[str, int, int, int]]] = []

## Count the frequencies of the diacritics and their related characters
global_diacritic_freq = Counter()
global_relation_freq = Counter()

for word in hebrew_pretokens:
    d_freq, r_freq = collect_diacritic_freqs(word)

    global_diacritic_freq.update(d_freq)
    global_relation_freq.update(r_freq)

# Counter for cantillation marks that have no base letter
cantillation_only_freq = Counter()

for word_index, original_word in enumerate(hebrew_pretokens):
    clean_word = clean_pretokens[word_index]
    subwords = tokenizer.tokenize(clean_word)
    subword_spans = get_subword_spans(subwords)

    word_locations = []

    for diacritic, original_char_index in hebrew_diacritics[word_index]:
        # Convert original index to stripped index
        try:
            stripped_index = original_to_stripped_index(
                original_word, original_char_index
            )
        except ValueError:
            # No base character; count as cantillation-only
            cantillation_only_freq[diacritic] += 1
            continue

        mapping = character_to_subword_mappings[word_index]

        if stripped_index not in mapping:
            # Diacritic past the last base character
            cantillation_only_freq[diacritic] += 1
            continue

        # Map stripped index to subword index
        subword_index = mapping[stripped_index]

        # Compute character index inside subword
        subword_start, _ = subword_spans[subword_index]
        subword_char_index = stripped_index - subword_start

        word_locations.append(
            (diacritic, original_char_index, subword_index, subword_char_index)
        )

    diacritic_locations.append(word_locations)

## Print results to a file 
with open("diacritic_stats.txt", "w", encoding="utf-8") as f:
    for word, locations in zip(hebrew_pretokens, diacritic_locations):
        if locations:
            print(word, file=f)
            for entry in locations:
                print("  ", entry, file=f)

    print("Diacritic frequency:", file=f)
    print(global_diacritic_freq, file=f)

    print("\nCharacter–diacritic relations:", file=f)
    print(global_relation_freq, file=f)

    print("\nCantillation frequency:", file=f)
    print(cantillation_only_freq, file=f)

