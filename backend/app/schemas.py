from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models import GameResult


class PlayerInputSchema(BaseModel):
    player_name: str


class PlayerOutputSchema(BaseModel):
    id: int
    name: str


class CreateGameSessionInputSchema(BaseModel):
    player_id: int


class SessionIdPathInputSchema(BaseModel):
    session_id: int


class GameMovePathInputSchema(BaseModel):
    session_id: int
    move: int


class GameResultOutputSchema(BaseModel):
    result: GameResult = None


class GameSessionOutputSchema(BaseModel):
    id: int
    credits: int
    start_time: datetime
    end_time: datetime = None
    result: GameResult = None
    board: List[str]
    wins: int
    losses: int
    draws: int
