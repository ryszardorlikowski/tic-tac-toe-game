from __future__ import annotations

from enum import IntEnum

from .exceptions import NotAllowedMove, CannotAddCredits, CannotStartNewGame
from .extensions import db


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class GameResult(IntEnum):
    DRAW = 0
    WON = 1
    LOST = 2


class GameSession(db.Model):
    __tablename__ = 'game_sessions'

    PLAYER_START_CREDITS = 10
    PLAYER_SINGLE_GAME_COST = 3
    SIGN_PLAYER = 'X'
    SIGN_COMPUTER = 'O'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    start_time = db.Column(db.DateTime, nullable=False, default=db.func.now())
    end_time = db.Column(db.DateTime, nullable=True)
    credits = db.Column(db.Integer, default=10)
    current_board = db.Column(db.String(9), nullable=True)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)

    player = db.relationship('Player', backref=db.backref('game_sessions', lazy=True))

    @property
    def board(self) -> list[str] | None:
        return list(self.current_board) if self.current_board else None

    @property
    def wining_combinations(self):
        return [
            self.current_board[0:3],
            self.current_board[3:6],
            self.current_board[6:9],
            self.current_board[0:9:3],
            self.current_board[1:9:3],
            self.current_board[2:9:3],
            self.current_board[0:9:4],
            self.current_board[2:7:2]
        ]

    def end_game(self):
        self.end_time = db.func.now()
        db.session.commit()

    def start_game(self):
        self.current_board = ' ' * 9
        if self._can_start_game():
            self.credits -= self.PLAYER_SINGLE_GAME_COST
            db.session.commit()
        else:
            raise CannotStartNewGame

    def play_turn(self, cell: int):
        self._player_make_move(cell)
        self._computer_make_move()
        result = self._get_result()
        db.session.commit()
        return result

    def add_credits(self):
        if self.credits == 0:
            self.credits = self.PLAYER_START_CREDITS
            db.session.commit()
        else:
            raise CannotAddCredits

    def dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'credits': self.credits,
            'board': self.board,
            'wins': self.wins,
            'losses': self.losses,
            'draws': self.draws
        }

    def _can_start_game(self):
        return self.credits >= self.PLAYER_SINGLE_GAME_COST

    def _get_result(self) -> GameResult | None:
        if [self.SIGN_PLAYER, self.SIGN_PLAYER, self.SIGN_PLAYER] in self.wining_combinations:
            self.wins += 1
            return GameResult.WON
        elif [self.SIGN_COMPUTER, self.SIGN_COMPUTER, self.SIGN_COMPUTER] in self.wining_combinations:
            self.losses += 1
            return GameResult.LOST
        elif ' ' not in self.current_board:
            self.draws += 1
            return GameResult.DRAW
        return None

    def _make_move(self, cell: int, sign: str) -> None:
        if self.current_board[cell] == ' ':
            self.current_board = self.current_board[:cell] + sign + self.current_board[cell + 1:]
            return
        raise NotAllowedMove

    def _player_make_move(self, cell: int):
        return self._make_move(cell, self.SIGN_PLAYER)

    def _computer_make_move(self):
        # TODO: implement better AI :)
        for i in range(9):
            try:
                self._make_move(i, self.SIGN_COMPUTER)
                break
            except NotAllowedMove:
                continue
