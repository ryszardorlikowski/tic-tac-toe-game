from __future__ import annotations

from datetime import datetime

from sqlalchemy import func, and_, cast, extract
from sqlalchemy.dialects.postgresql import INTERVAL
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

    def get_players_stats(self):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return self.session.query(
            GameSession.player_id,
            Player.name.label('player_name'),
            func.sum(GameSession.wins).label('wins'),
            func.sum(GameSession.losses).label('losses'),
            func.sum(GameSession.draws).label('draws'),
            func.sum(extract('epoch', GameSession.end_time - GameSession.start_time)).label('game_duration_seconds')
        ).join(Player).filter(
            and_(GameSession.start_time >= today)
        ).group_by(
            GameSession.player_id, Player.name
        ).all()


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
