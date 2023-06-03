def test_get_player(test_client, player, db_session):
    response = test_client.get(f'/api/players/{player.name}')

    assert response.status_code == 200
    assert response.json['name'] == player.name


def test_create_player(test_client, db_session):
    response = test_client.post('/api/players', json={"player_name": 'Test Player'})

    assert response.status_code == 201
    assert response.json['name'] == 'Test Player'


def test_create_game_session(test_client, player, db_session):
    response = test_client.post('/api/game-sessions', json={"player_id": player.id})

    assert response.status_code == 201
    assert response.json['player_id'] == player.id
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
