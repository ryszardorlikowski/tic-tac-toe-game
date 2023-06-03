import psycopg2
import pytest
from psycopg2 import extensions

from app import create_app, db as _db, config
from app.models import Player, GameSession

TEST_DATABASE_NAME = 'test_db'

TEST_CONFIG = {
    'TESTING': True,
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': config.SQLALCHEMY_DATABASE_URI.replace('game', TEST_DATABASE_NAME),
}


def create_test_db():
    conn = psycopg2.connect(config.SQLALCHEMY_DATABASE_URI)
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"SELECT datname FROM pg_catalog.pg_database WHERE datname='{TEST_DATABASE_NAME}'")
    result = cursor.fetchone()
    if result is None:
        cursor.execute(f'CREATE DATABASE {TEST_DATABASE_NAME}')
    cursor.close()
    conn.close()


@pytest.fixture(scope='session')
def app(request):
    create_test_db()

    app = create_app(config_override=TEST_CONFIG)

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


@pytest.fixture
def player(db_session):
    player = Player(name="test_player")
    db_session.add(player)
    db_session.commit()
    return player


@pytest.fixture
def game_session(db_session, player):
    game_session = GameSession(player_id=1)
    db_session.add(game_session)
    db_session.commit()
    return game_session
