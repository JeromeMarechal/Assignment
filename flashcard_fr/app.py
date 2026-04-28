from flask import Flask, render_template
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from config import Config
from models import User, db
from routes.auth_routes import auth_bp
from routes.card_routes import card_bp
from routes.dashboard_routes import dashboard_bp
from routes.quiz_routes import quiz_bp
from routes.expressions_routes import expressions_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(card_bp, url_prefix='/card')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(quiz_bp, url_prefix='/quiz')
app.register_blueprint(expressions_bp, url_prefix='/expressions')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_tables():
    with app.app_context():
        db.create_all()


create_tables()


@app.route("/")
@login_required
def home():
    return render_template("home.html", user_name=current_user.username)

if __name__ == "__main__":
    app.run(debug=True)
