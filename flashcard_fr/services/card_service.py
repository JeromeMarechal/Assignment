import asyncio
from collections.abc import Iterable
from typing import TypedDict

from clients.translate import get_word_analysis
from models import User
from repositories.card.card_repository import CardRepository
from utils.helper import format_card_data, to_join, to_list


class TranslationResult(TypedDict):
    word_fr: str
    word_lang: str
    definitions: list[str]
    part_of_speech: str
    examples_pairs: Iterable[tuple[str, str]]
    synonyms: str
    card_id: int | None


class CardService:
    @staticmethod
    def search(word: str, lang: str) -> tuple[bool, str | str | TranslationResult]:
        if not word:
            return False, "Word is required"
        if not lang:
            return False, "Language is required"

        card = CardRepository.get_card_by_word_and_lang(word, lang)

        if card:
            translation = format_card_data(card)

        else:
            try:
                data = asyncio.run(get_word_analysis(word, lang))
            except Exception as e:
                return False, f"Error fetching translation: {str(e)}"

            if data:
                examples = to_list(data["example"])
                examples_translated = to_list(data["example_translated"])

                translation = {
                    "word_fr": data["word_fr"],
                    "word_lang": data["word_lang"],
                    "definitions": data["definitions"],
                    "part_of_speech": data["part_of_speech"],
                    "examples_pairs": zip(examples, examples_translated),
                    "synonyms": to_join(data["synonyms"]),
                    "card_id": None,
                }

                if all(value not in ([], "", None) for value in data.values()):
                    success, result = CardRepository.create_card(
                        lang, translation, examples, examples_translated
                    )
                    if success:
                        new_card = result
                        translation["card_id"] = new_card.id
                    else:
                        return False, result
            else:
                return False, "No translation found"

        return True, translation

    @staticmethod
    def add_card(card_id: int, user: User) -> tuple[bool, str]:
        card = CardRepository.get_card_by_id(card_id)
        if not card:
            return False, "Card not found"

        success, result = CardRepository.add_card_to_user(card, user)
        return success, result

    @staticmethod
    def remove_card(card_id: int, user: User) -> tuple[bool, str]:
        card = CardRepository.get_card_by_id(card_id)
        if not card:
            return False, "Card not found"

        success, result = CardRepository.remove_card_from_user(card, user)
        return success, result
    
    @staticmethod
    def is_enough_cards_for_quiz(user_id: int) -> bool:
        if CardRepository.count_user_cards(user_id) < 10:
            return False
        return True
