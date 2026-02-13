import ast
from collections import defaultdict

def build_diacritic_dict(filepath):
    """
    Output format:

    {
        'ּ': {
            'diacritic_char_index': [...],
            'subword_index': [...],
            'diacritic_subword_char_index': [...]
        },
        ...
    }
    """

    diacritics = defaultdict(lambda: {
        "diacritic_char_index": [],
        "subword_index": [],
        "diacritic_subword_char_index": []
    })

    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # only process tuple lines
            if not (line.startswith("(") and line.endswith(")")):
                continue

            dchar, char_i, sub_i, subchar_i = ast.literal_eval(line)

            diacritics[dchar]["diacritic_char_index"].append(char_i)
            diacritics[dchar]["subword_index"].append(sub_i)
            diacritics[dchar]["diacritic_subword_char_index"].append(subchar_i)

    return dict(diacritics)


if __name__ == "__main__":
    path = "./diacritics_to_reformat.txt"

    result = build_diacritic_dict(path)

    with open("diacritic_stats_reformatted.txt", "w", encoding="utf-8") as f:
        print(result, file=f)
