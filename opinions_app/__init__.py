from . import models, views, error_handler, cli_commands
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'SECRET KEY'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импортируем остальные модули, чтобы зарегистрировать маршруты, обработчики и команды
