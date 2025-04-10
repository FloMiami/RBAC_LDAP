from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '860c18631a6be3aff63a65ac2b0b3c1229c4a39edcb0229deeb14de85548da98'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views, auth

