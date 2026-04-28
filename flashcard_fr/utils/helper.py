def to_list(data):
    if data is None:
        return []
    if isinstance(data, str):
        if "," in data:
            return [item.strip() for item in data.split(",") if item.strip()]
        return [data]
    return data


def to_join(data):
    """Join a list of strings into a single string separated by commas. If it's already a string, return it as is."""
    if not data:
        return ""
    if isinstance(data, list):
        return ", ".join(data)
    return data


def find_language_text(code, languages):
    """Find the language name corresponding to a given language code."""
    for region, langs in languages.items():
        if code in langs:
            return langs[code]
    return None


def format_card_data(card):

    examples = card.example.split(",")
    examples_translated = card.example_translated.split(",")

    translation = {
        "word_fr": card.word_fr,
        "word_lang": card.word_lang,
        "definitions": [card.definition],
        "part_of_speech": card.pos,
        "examples_pairs": zip(examples, examples_translated),
        "synonyms": card.synonyms,
        "card_id": card.id,
    }

    return translation
