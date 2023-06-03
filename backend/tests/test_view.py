from datetime import datetime, timedelta


def test_get_player(test_client, player, db_session):
    response = test_client.get(f'/api/players/{player.name}')

    assert response.status_code == 200
    assert response.json['name'] == player.name


def test_create_player(test_client, db_session):
    response = test_client.post('/api/players', json={"player_name": 'Test Player'})

    assert response.status_code == 201
    assert response.json['name'] == 'Test Player'


def test_get_all_players_statistics(test_client, db_session, game_session, player):
    time = datetime.now()
    game_session.start_time = time - timedelta(minutes=1)
    game_session.end_time = time
    game_session.wins = 1
    game_session.losses = 0
    db_session.commit()

    response = test_client.get('/api/players/statistics')
    assert response.status_code == 200

    assert len(response.json['results']) == 1

    player1 = response.json['results'][0]
    assert player1 is not None
    assert player1['player_name'] == player.name
    assert player1['game_duration_seconds'] == 60
    assert player1['wins'] == 1
    assert player1['losses'] == 0


def test_create_game_session(test_client, player, db_session):
    response = test_client.post('/api/game-sessions', json={"player_id": player.id})

    assert response.status_code == 201
    assert response.json['player_id'] == player.id
    assert response.json['board'] is None


def test_get_game_session(test_client, game_session, db_session):
    response = test_client.get(f'/api/game-sessions/{game_session.id}')

    assert response.status_code == 200
    assert response.json['player_id'] == game_session.player_id
    assert response.json['board'] is None


def test_start_new_game(test_client, game_session, db_session):
    response = test_client.post(f'/api/game-sessions/{game_session.id}/new-game')

    assert response.status_code == 200
    assert response.json['board'] == [' '] * 9


def test_make_move(test_client, game_session, db_session):
    game_session.current_board = ' ' * 9
    db_session.commit()
    response = test_client.post(f'/api/game-sessions/{game_session.id}/move/{0}')

    assert response.status_code == 200
    assert response.json['result'] is None


def test_add_credits(test_client, game_session, db_session):
    game_session.credits = 0
    db_session.commit()
    response = test_client.post(f'/api/game-sessions/{game_session.id}/credits')

    assert response.status_code == 200
    assert response.json['credits'] == 10
