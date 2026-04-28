from models import Card, User
from repositories.dashboard.dashboard_repository import DashboardRepository
from utils.helper import format_card_data


class DashboardService:
    @staticmethod
    def get_user_flashcards(user: User) -> list[Card]:
        flashcrads = DashboardRepository.get_user_flashcards(user)
        list_flashcards = [format_card_data(card) for card in flashcrads]
        return list_flashcards
