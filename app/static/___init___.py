from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@db:5432/sistema_matricula'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes
