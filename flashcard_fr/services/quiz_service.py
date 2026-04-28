from typing import List, Tuple, Union, Optional, Dict
import random

from flask_login import current_user
from models import Card, Meaning
from repositories.quiz.quiz_repository import MeaningRepository
from repositories.card.card_repository import CardRepository
from utils.helper import to_list


class QuizMeaningService:
    @staticmethod
    def prepa_quiz(user_id:int) -> Union[Tuple[bool, int], Tuple[bool, Meaning]]:
        cards: List[Card] = CardRepository.get_n_random_cards(current_user.id, 4)
        index: int = random.randint(0, len(cards) - 1)
        quiz_state: Optional[Meaning] = MeaningRepository.get_quiz_state(user_id)

        if quiz_state == None:
            MeaningRepository.create_quiz_state(
                user_id,
                cards[index].word_fr,
                cards[index].word_lang,
                [
                    cards[0].word_lang,
                    cards[1].word_lang,
                    cards[2].word_lang,
                    cards[3].word_lang,
                ],
                1,
                0,
            )

            quiz_state: Meaning = MeaningRepository.get_quiz_state(user_id)

        if quiz_state.round > 10:
            score: int = quiz_state.score
            score_in_poucent: int = int((score / 10) * 100)

            MeaningRepository.reset_quiz_data(
                user_id,
                cards[index].word_fr,
                cards[index].word_lang,
                [
                    cards[0].word_lang,
                    cards[1].word_lang,
                    cards[2].word_lang,
                    cards[3].word_lang,
                ],
            )

            return True, score_in_poucent

        quiz_data = {
            "word_FR": quiz_state.current_word,
            "correct_answer": quiz_state.correct_answer,
            "choices": to_list(quiz_state.choices),
            "round": quiz_state.round,
            "score": quiz_state.score,
        }

        return False, quiz_data

    @staticmethod
    def get_new_round_data(answer: bool, round: int, score: int) -> Tuple[Dict, str]:
        cards = CardRepository.get_n_random_cards(current_user.id, 4)
        index = random.randint(0, len(cards) - 1)
        correct_answer = cards[index].word_lang

        data = {
            "is_correct": answer,
            "word_FR": cards[index].word_fr,
            "choices": [
                cards[0].word_lang,
                cards[1].word_lang,
                cards[2].word_lang,
                cards[3].word_lang,
            ],
            "round": f"{round}",
            "score": f"{score}",
        }

        return data, correct_answer

    @staticmethod
    def update_round(user_id: int, user_choice:str) -> Union[Dict, Dict[bool, Optional[int]]]:
        quiz_state = MeaningRepository.get_quiz_state(user_id)
        answer = quiz_state.correct_answer == user_choice

        score = quiz_state.score
        if answer:
            score += 1

        round = quiz_state.round + 1

        new_quiz_data = QuizMeaningService.get_new_round_data(answer, round, score)
        data_to_send = new_quiz_data[0]
        correct_answer = new_quiz_data[1]
        MeaningRepository.update_quiz_state(
            user_id,
            data_to_send["word_FR"],
            correct_answer,
            data_to_send["choices"],
            round,
            score,
        )

        if round > 10:
            total_attempts = quiz_state.attempts
            all_time_score = quiz_state.all_time_score
            score_in_percent = int((score / 10) * 100)
            new_total_attempts = total_attempts + 1
            new_all_time_score = (
                (all_time_score * total_attempts) + score_in_percent
            ) / new_total_attempts
            MeaningRepository.update_attemps(user_id, new_total_attempts)
            MeaningRepository.update_all_time_score(user_id, new_all_time_score)
            return {"is_end": True, "score": score, "is_correct": answer}

        return data_to_send
