from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from contents.language_by_region import languages_by_region
from services import card_service
from utils.helper import find_language_text

card_bp = Blueprint("card", __name__)


@card_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'GET':
        return render_template('search.html', native_language_code=current_user.native_language, native_language_text=find_language_text(current_user.native_language, languages_by_region), languages_by_region=languages_by_region)
    
    if request.method == 'POST':
        word = request.form.get('word').strip().lower()
        lang = request.form.get('lang')
        
        success, result = card_service.CardService.search(word, lang)
        if not success:
            if result == "word is required":
                return render_template(
                    "error_alert.html", message="You must provide a word to search."
                ), 400
            elif result == "language is required":
                return render_template(
                    "error_alert.html", message="You must select a language."
                ), 400
            elif result == "No translation found":
                return render_template(
                    "error_alert.html",
                    message="No translation found for the given word and language.",
                ), 404
            else:
                return render_template("error_alert.html", message=result), 500

        translation = result
        return render_template('flashcard.html', word=word, lang=lang, translation=translation)    


@card_bp.route('/add_card', methods=['POST'])
@login_required
def add_card():
    card_id = request.json.get('card_id')
    if not card_id:
        message = "Card ID is required"
        return render_template('error_alert.html', message=message), 400
        
    success, result = card_service.CardService.add_card(card_id, current_user)
    if not success:
        return render_template('error_alert.html', message=result), 404


@card_bp.route('/remove_card', methods=['POST'])
@login_required
def remove_card():
    card_id = request.json.get('card_id')
    if not card_id:
        message = "Card ID is required"
        return render_template('error_alert.html', message=message), 400
    
    success, result = card_service.CardService.remove_card(card_id, current_user)
    if not success:
        return render_template('error_alert.html', message=result), 404
