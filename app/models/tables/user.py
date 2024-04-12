from app.config.db_config import *


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False, unique=False)
    post = db.relationship('Note', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username:str, email:str, password_hash:str):
        self.username = username
        self.email = email
        
        self.password_hash = password_hash