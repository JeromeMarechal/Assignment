from models import User, Card
from typing import List


class DashboardRepository:
    @staticmethod
    def get_user_flashcards(user: User) -> List[Card]:
        flashcards: List[Card] = user.cards
        return flashcards
