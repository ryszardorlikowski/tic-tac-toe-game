from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models import GameResult


class PlayerPathSchema(BaseModel):
    player_name: str


class PlayerSchema(BaseModel):
    id: int
    name: str


class CreateGameSessionSchema(BaseModel):
    player_id: int


class CreateGameSchema(BaseModel):
    game_session_id: int


class GameSessionSchema(BaseModel):
    id: int
    credits: int


class GameSchema(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime = None
    result: GameResult = None
    board: List[str]
