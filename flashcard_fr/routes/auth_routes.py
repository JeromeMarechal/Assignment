from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from contents.language_by_region import languages_by_region
from services import auth_service


auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        username, password = [
            request.form.get(field) for field in ("username", "password")
        ]

        success, result = auth_service.login(username, password)
        
        if not success:
            return render_template('error_alert.html', message=result), 400
        
        user = result
        login_user(user)
        return redirect(url_for('home'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', languages_by_region=languages_by_region)
    
    if request.method == 'POST':
        
        username, email, native_language, password, confirmation_password = [
            request.form.get(field)
            for field in (
                "username",
                "email",
                "native_language",
                "password",
                "confirmation_password",
            )
        ]

        success, result = auth_service.register(
            username, email, native_language, password, confirmation_password
        )

        if not success:
            return render_template('error_alert.html', message=result), 400
                                                    
        new_user = result                                         
        login_user(new_user)    
        return redirect(url_for('home'))

@auth_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
