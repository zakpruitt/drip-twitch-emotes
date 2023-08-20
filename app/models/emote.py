from app import db

from werkzeug.security import generate_password_hash, check_password_hash

from models.base_model import BaseModel


class User(BaseModel):
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column("password", db.String(120), nullable=False)

    emotes = db.relationship('Emote', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)
