from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.tables.note import Note

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
    post = db.relationship('Note', backref='user', lazy=True)
