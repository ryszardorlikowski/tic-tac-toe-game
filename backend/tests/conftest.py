import pytest

from app import create_app, db as _db

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


