from flask import Blueprint, render_template
from flask_login import current_user

from services.dashboard_service import DashboardService

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route('/', methods=['GET'])
def dashboard():
    flashcards = DashboardService.get_user_flashcards(current_user)
    return render_template('dashboard.html', flashcards=flashcards)
