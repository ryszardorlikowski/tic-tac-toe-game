import pytest
from unittest.mock import Mock, MagicMock

from app.repositories import PlayerRepository, GameRepository
from app.models import Player, GameSession


@pytest.fixture(scope='module')
def db_session_mock():
    return MagicMock()


@pytest.fixture(scope='module')
def player_repository(db_session_mock):
    return PlayerRepository(db_session_mock)


@pytest.fixture(scope='module')
def game_repository(db_session_mock):
    return GameRepository(db_session_mock)


def test_get_player(player_repository, db_session_mock):
    player_name = "test_player"

    expected_player = Player(name=player_name)
    db_session_mock.query.return_value.filter_by.return_value.first.return_value = expected_player

    result = player_repository.get_player(player_name)

    db_session_mock.query.assert_called_with(Player)
    db_session_mock.query.return_value.filter_by.assert_called_with(name=player_name)

    assert result == expected_player


def test_create_player(player_repository, db_session_mock):
    player_name = "test_player"

    expected_player = Player(name=player_name)

    result = player_repository.create_player(player_name)

    db_session_mock.add.assert_called()
    db_session_mock.commit.assert_called()

    assert result.name == expected_player.name


def test_get_game_session(game_repository, db_session_mock):
    session_id = 1

    expected_game_session = GameSession(player_id=1)
    db_session_mock.query.return_value.filter_by.return_value.first.return_value = expected_game_session

    result = game_repository.get_game_session(session_id)

    db_session_mock.query.assert_called_with(GameSession)
    db_session_mock.query.return_value.filter_by.assert_called(session_id=session_id)

    assert result == expected_game_session


def test_create_game_session(game_repository, db_session_mock):
    player_id = 1

    expected_game_session = GameSession(player_id=player_id)

    result = game_repository.create_game_session(player_id)

    db_session_mock.add.assert_called()
    db_session_mock.commit.assert_called()

    assert result.player_id == expected_game_session.player_id
