from flask import Blueprint, jsonify, render_template, request
from flask_login import current_user, login_required

from services.quiz_service import QuizMeaningService
from services.card_service import CardService

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route('/', methods=['GET'])
@login_required
def quiz():
    return render_template("quiz.html")

@quiz_bp.route('/meaning', methods=['GET'])
@login_required
def quiz_meaning():
    is_enough_cards = CardService.is_enough_cards_for_quiz(current_user.id)
    return render_template("quiz_exercises/meaning/meaning.html", is_enough_cards=is_enough_cards)

#class QuizMeaningPlayView(MethodView):
@quiz_bp.route('/meaning/play', methods=['GET', 'POST'])
@login_required
def quiz_meaning_play():
    if request.method == "GET":
        is_end, quiz_data = QuizMeaningService.prepa_quiz(current_user.id)

        if is_end:
            return render_template("quiz_score.html", finalScore=quiz_data)
        else:
            return render_template(
                "quiz_exercises/meaning/meaning_play.html",
                choices=quiz_data["choices"],
                round=quiz_data["round"],
                score=quiz_data["score"],
                word_FR=quiz_data["word_FR"],
            )

    if request.method == "POST":
        data = request.get_json()
        user_choice = data.get("selected_option")
        updated_data = QuizMeaningService.update_round(current_user.id, user_choice)
        return jsonify(updated_data)
