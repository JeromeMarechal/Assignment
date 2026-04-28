from typing import List, Optional, Tuple, TypedDict, Union

from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

from models import Card, User, db, user_cards
from utils.helper import to_join


class TranslationResult(TypedDict):
    word_fr: str
    word_lang: str
    definitions: list[str]
    part_of_speech: str
    examples_pairs: list[tuple[str, str]]
    synonyms: str
    card_id: int | None


class CardRepository:
    @staticmethod
    def get_card_by_id(card_id: int) -> Optional[Card]:
        card: Optional[Card] = Card.query.get(card_id)
        return card

    @staticmethod
    def get_card_by_word_and_lang(word: str, lang: str) -> Optional[Card]:
        card: Optional[Card] = Card.query.filter(
            func.lower(Card.word_lang) == word.lower(),
            Card.lang == lang,
        ).first()
        return card

    @staticmethod
    def create_card(lang: str, translation: TranslationResult, examples: List[str], examples_translated: List[str]) -> Tuple[bool, Union[Card, str]]:
        new_card: Card = Card(
            lang=lang,
            word_fr=translation["word_fr"],
            word_lang=translation["word_lang"],
            definition=to_join(translation["definitions"]),
            pos=translation["part_of_speech"],
            synonyms=translation["synonyms"],
            example=to_join(examples),
            example_translated=to_join(examples_translated),
        )

        try:
            db.session.add(new_card)
            db.session.commit()
            return True, new_card
        except IntegrityError:
            db.session.rollback()
            return False, "Error saving card to database"

    @staticmethod
    def add_card_to_user(card: Card, user: User) -> tuple[bool, str]:
        if card not in user.cards:
            try:
                user.cards.append(card)
                db.session.commit()
                return True, "Card added to user's collection"
            except IntegrityError:
                db.session.rollback()
                return False, "Error adding card to user"
        return False, "Card already in user's collection"

    @staticmethod
    def remove_card_from_user(card: Card, user: User) -> tuple[bool, str]:
        if card in user.cards:
            try:
                user.cards.remove(card)
                db.session.commit()
                return True, "Card removed from user's collection"
            except IntegrityError:
                db.session.rollback()
                return False, "Error removing card from user"
        return False, "Card not found in user's collection"

    @staticmethod
    def get_n_random_cards(user_id: int, number_of_card: int) -> List[Card]:
        cards: List[Card] = Card.query.join(user_cards).filter(user_cards.c.user_id == user_id).order_by(db.func.random()).limit(number_of_card).all()
        return cards

    @staticmethod
    def count_user_cards(user_id: int) -> int:
        count: int = db.session.query(func.count(Card.id)).join(user_cards).filter(user_cards.c.user_id == user_id).scalar()
        return count