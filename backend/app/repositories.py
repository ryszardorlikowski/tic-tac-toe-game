from __future__ import annotations

from sqlalchemy.orm import Session

from .models import Player, GameSession


class PlayerRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_player(self, player_name: str) -> Player:
        return self.session.query(Player).filter_by(name=player_name).first()

    def create_player(self, player_name: str) -> Player:
        player = Player(name=player_name)
        self.session.add(player)
        self.session.commit()
        return player


class GameRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_game_session(self, session_id: int) -> GameSession | None:
        return self.session.query(GameSession).filter_by(id=session_id).first()

    def create_game_session(self, player_id: int) -> GameSession:
        game_session = GameSession(player_id=player_id)
        self.session.add(game_session)
        self.session.commit()

        return game_session
