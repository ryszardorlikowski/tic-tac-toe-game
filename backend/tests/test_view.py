from datetime import datetime

from flask import url_for
from freezegun import freeze_time

from tests.conftest import default_credits


def test_get_or_create_player(app, test_client, new_player):
    with app.test_request_context():
        url = url_for('api.get_or_create_player', player_name=new_player.name)

    response = test_client.get(url)

    print(response.json)
    assert response.status_code == 200
    assert response.json['name'] == new_player.name

    with app.test_request_context():
        url = url_for('api.get_or_create_player', player_name='no_exits_user')

    response = test_client.get(url)

    assert response.status_code == 200
    assert response.json['name'] == 'no_exits_user'


def test_create_game_session(app, test_client, new_player):
    with app.test_request_context():
        url = url_for('api.create_game_session')

    response = test_client.post(url, json={'player_id': new_player.id})

    assert response.status_code == 201
    assert response.json['credits'] == default_credits


@freeze_time("2023-06-02 12:34:56")
def test_create_game(app, test_client, new_game_session):
    with app.test_request_context():
        url = url_for('api.create_game')

    response = test_client.post(url, json={'game_session_id': new_game_session.id})

    assert response.status_code == 201
    assert response.json['start_time'] == 'Fri, 02 Jun 2023 12:34:56 GMT'
    assert response.json['board'] == []
