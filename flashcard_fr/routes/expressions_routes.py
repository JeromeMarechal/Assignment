from flask import Blueprint, render_template

expressions_bp = Blueprint("expressions", __name__)


@expressions_bp.route('/', methods=['GET'])
def expressions():
    return render_template('expressions.html')
