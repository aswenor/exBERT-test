from diacritics import ALL_DIACRITICS
from transformers import AutoTokenizer, AutoModel

model_filepath = "../alephbert"
# Requires vocab.txt file to load possible tokens.
tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(model_filepath)

tokens: list[str] = tokenizer.tokenize(
    "וַיִּשְׁמַ֗ע אֶת־דִּבְרֵ֤י בְנֵֽי־לָבָן֙ לֵאמֹ֔ר לָקַ֣ח יַעֲקֹ֔ב אֵ֖ת כָּל־אֲשֶׁ֣ר "
    "לְאָבִ֑ינוּ וּמֵאֲשֶׁ֣ר לְאָבִ֔ינוּ עָשָׂ֕ה אֵ֥ת כָּל־הַכָּבֹ֖ד הַזֶּֽה׃"
)


def get_diacritic_maps(pretokens: list[str]) -> list[list[tuple[str, int]]]:
    maps: list[list[tuple[str, int]]] = []
    for token in pretokens:
        diacritic_map: list[tuple[str, int]] = []
        consonant_index: int = 0
        for i in range(0, len(token)):
            if token[i] in ALL_DIACRITICS:
                diacritic_map.append((token[i], consonant_index - 1))
            else:
                consonant_index += 1
        maps.append(diacritic_map)
    return maps


## Get the word character index ---- [(diacritic_char, word_char_index),...]
def get_diacritics_with_char_index(
    pretokens: list[str],
) -> list[list[tuple[str, int]]]:
    all_maps: list[list[tuple[str, int]]] = []

    for token in pretokens:
        diacritic_map: list[tuple[str, int]] = []
        for i, ch in enumerate(token):
            if ch in ALL_DIACRITICS:
                diacritic_map.append((ch, i))
        all_maps.append(diacritic_map)

    return all_maps


# Calculate the subword spans ---- [(start_char, end_char)]
def get_subword_spans(subwords: list[str]) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    cursor = 0

    for subword in subwords:
        start = cursor
        end = cursor + len(subword)
        spans.append((start, end))
        cursor = end

    return spans

######
hebrew_pretokens: list[str] = (
    "וַיִּשְׁמַ֗ע אֶת־דִּבְרֵ֤י בְנֵֽי־לָבָן֙ לֵאמֹ֔ר לָקַ֣ח יַעֲקֹ֔ב אֵ֖ת כָּל־אֲשֶׁ֣ר "
    "לְאָבִ֑ינוּ וּמֵאֲשֶׁ֣ר לְאָבִ֔ינוּ עָשָׂ֕ה אֵ֥ת כָּל־הַכָּבֹ֖ד הַזֶּֽה׃"
).split()

diacritic_maps = get_diacritic_maps(hebrew_pretokens)


## Original character to subword mapping
character_to_subword_mappings: list[dict[int, int]] = []

for pretoken_index, pretoken in enumerate(hebrew_pretokens):
    subwords: list[str] = tokenizer.tokenize(pretoken)
    character_index: int = 0

    character_to_subword_mapping: dict[int, int] = {}
    for subword_index, subword in enumerate(subwords):
        for character in subword:
            character_to_subword_mapping[character_index] = subword_index
            character_index += 1
    else:
        character_to_subword_mappings.append(character_to_subword_mapping)


# Get the full mapping of diacritic locations --- (diacritic_char, word_char_index, subword_index, subword_char_index)
hebrew_diacritics = get_diacritics_with_char_index(hebrew_pretokens)

# Per word: (diacritic_char, word_char_index, subword_index, subword_char_index)
diacritic_locations: list[list[tuple[str, int, int, int]]] = []

for word_index, pretoken in enumerate(hebrew_pretokens):
    subwords = tokenizer.tokenize(pretoken)

    # Sanity check: tokenizer must preserve characters
    #assert "".join(subwords) == pretoken, f"Tokenizer mismatch in word: {pretoken}"

    subword_spans = get_subword_spans(subwords)
    word_locations: list[tuple[str, int, int, int]] = []

    for diacritic, word_char_index in hebrew_diacritics[word_index]:
        subword_index = character_to_subword_mappings[word_index][word_char_index]
        subword_start, _ = subword_spans[subword_index]
        subword_char_index = word_char_index - subword_start

        word_locations.append(
            (diacritic, word_char_index, subword_index, subword_char_index)
        )

    diacritic_locations.append(word_locations)
