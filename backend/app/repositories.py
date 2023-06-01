from __future__ import annotations

import datetime

from sqlalchemy.orm import Session
from .models import Player, GameSession, Game, GameResult
from .schemas import PlayerSchema, GameSessionSchema, GameSchema


class PlayerRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_or_create_player(self, player_name: str) -> PlayerSchema:
        player = self.session.query(Player).filter_by(name=player_name).first()
        if not player:
            player = Player(name=player_name)
            self.session.add(player)
            self.session.commit()

        return PlayerSchema(
            id=player.id,
            name=player.name,
        )


class GameRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_game_session(self, player_id: int) -> GameSessionSchema:
        game_session = GameSession(player_id=player_id)
        self.session.add(game_session)
        self.session.commit()

        return GameSessionSchema(
            id=game_session.id,
            credits=game_session.credits,
        )

    def update_game_session_credits(self, session_id: int, credits: int) -> GameSessionSchema:
        game_session = self.session.query(GameSession).filter_by(id=session_id).first()
        game_session.credits = credits
        self.session.commit()

        return GameSessionSchema(
            id=game_session.id,
            credits=game_session.credits,
        )

    def create_game(self, game_session_id: int) -> GameSchema:
        game = Game(game_session_id=game_session_id, start_time=datetime.datetime.now())
        self.session.add(game)
        self.session.commit()
        return GameSchema(
            id=game.id,
            start_time=game.start_time,
            board=[]
        )

    def update_game(self, game_id: int, board: str, result: GameResult | None = None) -> GameSchema:
        game = self.session.query(Game).filter_by(id=game_id).first()

        game.board = board
        if result:
            game.result = result
            game.end_time = datetime.datetime.now()
        self.session.commit()

        return GameSchema(
            id=game.id,
            start_time=game.start_time,
            end_time=game.end_time,
            result=game.result,
            board=list(game.board) if game.board else [],
        )
