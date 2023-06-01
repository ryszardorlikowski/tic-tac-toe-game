import datetime
from enum import Enum

from .extensions import db


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class GameSession(db.Model):
    __tablename__ = 'game_sessions'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    credits = db.Column(db.Integer, default=10)

    player = db.relationship('Player', backref=db.backref('game_sessions', lazy=True))


class GameResult(Enum):
    DRAW = 0
    WIN = 1
    LOSS = 2


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    game_session_id = db.Column(db.Integer, db.ForeignKey('game_sessions.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    board = db.Column(db.String(9), nullable=True)
    result = db.Column(db.Enum(GameResult), nullable=True)

    game_session = db.relationship('GameSession', backref=db.backref('games', lazy=True))
