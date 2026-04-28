import asyncio
import json
import os
import re
from typing import Dict, Union

from dotenv import load_dotenv
from google import genai

# Load configuration once at module level
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_ID = "gemini-2.5-flash"


def get_word_analysis(word: str, lang: str = "en") -> dict | str:
    """
    Get detailed linguistic analysis of a single word in the specified language.

    Args:
        word: The input word to analyze (can include article/prefix but not features of a sentence).
        lang: Source language of the input.

    Returns:
        Dictionary with word analysis or error if input does not follow the rules.
        return an error if there is no translation, or no definition or no POS, a return of the word analysis cannot have empty fields.
    """
    # Cache the prompt template to avoid string formatting on each call
    prompt_template: str = """
    You are a language assistant. 
    If the input is a single word (optionally with an article or prefix), return a JSON object with:
    - "word_fr": the word translated into french (add article or previx if appropriate, the word should start with a uppercase letter)
    - "word_lang": the word translated into {lang} (add article or previx if appropriate, the word should start with a uppercase letter)
    - "part_of_speech": the grammatical category in {lang} (e.g., noun, verb, adjective, etc.)
    - "synonyms": a list of synonyms for the word (in french and after each of them between pareenthesis the translation in {lang}, if no synonym found return an empty list)
    - "definitions": a list of definitions strictly in {lang} (if multiple, use "1", "2", no more than the two main definitions) (if the word change in defintion like noun to verb or else don't validate this translation), make sure the translation provided make sens in french don't do litteral translation.
    - "example": an example (related to the definition) sentence using the word in context in french (two examples)
    - "example_translated": the example sentence translated into {lang}

    If the input is a sentence or not just a word (with optional article/prefix), return this string: 
    "Input inappropriate: please provide a single word (with optional article or prefix)."

    Input word: "{word}"
    """

    def treat_data():
        response = client.models.generate_content(
            model=MODEL_ID, contents=prompt_template.format(word=word, lang=lang)
        )
        clean_text = re.sub(
            r"^```json\s*|\s*```$", "", response.text.strip(), flags=re.DOTALL
        )
        data = json.loads(clean_text)
        return data

    return asyncio.to_thread(treat_data)
