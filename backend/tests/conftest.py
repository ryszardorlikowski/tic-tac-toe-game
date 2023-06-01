from datetime import datetime

import pytest
from flask_sqlalchemy.session import Session

from app import create_app, db as _db
from app.models import Player, GameResult, GameSession, Game

TEST_CONFIG = {
    'TESTING': True,
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
}


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app(TEST_CONFIG)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="function")
def test_client(app):
    return app.test_client()


@pytest.fixture(scope='function')
def db(app, request):
    _db.app = app
    _db.create_all()

    def teardown():
        _db.drop_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def db_session(db, request):
    session = db.session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session


player_name = "test_player"
player_id = 1
session_id = 1
game_id = 1
default_credits = 10
board = "XOXOXOXOX"
result = GameResult.WIN


@pytest.fixture
def new_player(db_session: Session):
    player = Player(name=player_name)
    db_session.add(player)
    db_session.commit()
    return player


@pytest.fixture
def new_game_session(db_session, new_player: Player):
    game_session = GameSession(player_id=player_id)
    db_session.add(game_session)
    db_session.commit()
    return game_session


@pytest.fixture
def new_game(db_session, new_game_session: Player):
    game = Game(game_session_id=new_game_session.id, start_time=datetime.now())
    db_session.add(game)
    db_session.commit()
    return game
