import pytest
from app.models import GameSession, GameResult, NotAllowedMove, CannotAddCredits, CannotStartNewGame


def test_create_player(player):
    assert player.name == "test_player"


def test_player_dict(player):
    assert player.dict() == {'id': 1, 'name': 'test_player'}


def test_create_game_session(game_session):
    assert game_session.player_id == 1


def test_game_session_dict(game_session):
    result = game_session.dict()
    expected_keys = ['id', 'player_id', 'start_time', 'end_time', 'credits', 'board', 'wins', 'losses', 'draws']
    assert all(key in result for key in expected_keys)


def test_start_game(game_session):
    game_session.start_game()
    assert game_session.credits == 7
    assert game_session.current_board == ' ' * 9


def test_start_game_no_credits(game_session):
    game_session.credits = 2
    with pytest.raises(CannotStartNewGame):
        game_session.start_game()


def test_add_credits(game_session):
    game_session.credits = 0
    game_session.add_credits()
    assert game_session.credits == 10


def test_add_credits_already_has_credits(game_session):
    game_session = GameSession(player_id=1, credits=5)
    with pytest.raises(CannotAddCredits):
        game_session.add_credits()


def test_play_turn(game_session):
    game_session.start_game()
    game_session.play_turn(0)
    assert game_session.current_board[0] == GameSession.SIGN_PLAYER
    assert game_session.current_board[1] == GameSession.SIGN_COMPUTER


def test_play_turn_not_allowed(game_session):
    game_session.start_game()
    game_session.play_turn(0)
    with pytest.raises(NotAllowedMove):
        game_session.play_turn(0)


def test_player_win(game_session):
    game_session.start_game()
    game_session.current_board = 'XX X O OO'
    result = game_session.play_turn(2)

    assert result == GameResult.WON
    assert game_session.wins == 1


def test_player_loss(game_session):
    game_session.start_game()
    game_session.current_board = 'OO X O XX'
    result = game_session.play_turn(4)

    assert result == GameResult.LOST
    assert game_session.losses == 1


def test_player_draw(game_session):
    game_session.start_game()
    game_session.current_board = 'XOXXXOO  '
    result = game_session.play_turn(7)

    assert result == GameResult.DRAW
    assert game_session.draws == 1
