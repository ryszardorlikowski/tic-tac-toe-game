from datetime import datetime, timezone

import pytest
from sqlalchemy.orm import Session
from app.models import Player, GameSession, Game, GameResult
from app.repositories import PlayerRepository, GameRepository
from freezegun import freeze_time

from tests.conftest import default_credits, board, result


@pytest.fixture
def player_repository(db_session: Session) -> PlayerRepository:
    return PlayerRepository(db_session)


@pytest.fixture
def game_repository(db_session: Session) -> GameRepository:
    return GameRepository(db_session)


def test_get_or_create_player(player_repository: PlayerRepository, new_player: Player):
    player = player_repository.get_or_create_player(new_player.name)
    assert player.name == new_player.name


def test_create_game_session(game_repository: GameRepository, new_player: Player):
    game_session = game_repository.create_game_session(new_player.id)
    assert game_session.credits == default_credits


def test_update_game_session_credits(game_repository: GameRepository, new_game_session: GameSession):
    game_session = game_repository.update_game_session_credits(new_game_session.id, 100)
    assert game_session.credits == 100


@freeze_time("2023-06-01 20:20:48")
def test_create_game(game_repository: GameRepository, new_game_session: GameSession):
    game = game_repository.create_game(new_game_session.id)
    assert game.start_time.replace(microsecond=0) == datetime(2023, 6, 1, 20, 20, 48)


@freeze_time("2023-06-02 12:34:56")
def test_update_game(game_repository: GameRepository, new_game: GameSession):
    game = game_repository.update_game(new_game.id, board, result)
    assert game.board == list(board)
    assert game.result == result
    assert game.end_time == datetime(2023, 6, 2, 12, 34, 56)
