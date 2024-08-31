import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
class Config:
    app.config["SECRET_KEY"] = 'the-secret-key'

from app import routes
