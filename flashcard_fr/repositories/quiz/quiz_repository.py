from models import db, Card, Meaning
from sqlalchemy import func
from typing import List, Optional
from utils.helper import to_join


class MeaningRepository:
    @staticmethod
    def get_quiz_state(user_id: int) -> Meaning:
        return Meaning.query.filter_by(user_id=user_id).first()
    
    @staticmethod
    def create_quiz_state(user_id:int, word_FR:str, correct_answer:str, choices:List[str], round:int, score:int) -> None:
        quiz_data: Meaning = Meaning(
            user_id=user_id,
            current_word=word_FR,
            correct_answer=correct_answer,
            choices=to_join(choices),
            round=round,
            score=score,
        )

        db.session.add(quiz_data)
        db.session.commit()

    @staticmethod
    def update_quiz_state(user_id:int, word_FR:str, correct_answer:str, choices:List[str], round:int, score:int) -> None:
        quiz: Optional[Meaning] = MeaningRepository.get_quiz_state(user_id)

        quiz.current_word = word_FR
        quiz.correct_answer = correct_answer
        quiz.choices = to_join(choices)
        quiz.round = round
        quiz.score = score

        db.session.commit()

    @staticmethod
    def reset_quiz_data(user_id:int, word_FR:str, correct_answer:str, choices:List[str]) -> None:
        quiz: Optional[Meaning] = MeaningRepository.get_quiz_state(user_id)
        if quiz:
            quiz.current_word = word_FR
            quiz.correct_answer = correct_answer
            quiz.choices = to_join(choices)
            quiz.round = 1
            quiz.score = 0

            db.session.commit()

    @staticmethod
    def update_all_time_score(user_id:int, all_time_score:int) -> None:
        quiz: Optional[Meaning] = MeaningRepository.get_quiz_state(user_id)
        if quiz:
            quiz.all_time_score = all_time_score

            db.session.commit()

    @staticmethod
    def update_attemps(user_id: int, attempts: int) -> None:
        quiz: Optional[Meaning] = MeaningRepository.get_quiz_state(user_id)
        if quiz:
            quiz.attempts = attempts

            db.session.commit()
