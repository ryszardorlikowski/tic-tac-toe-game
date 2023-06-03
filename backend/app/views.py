from http import HTTPStatus
from typing import List

from flask_openapi3 import APIBlueprint, Tag

from app.exceptions import PlayerNotFound, PlayerAlreadyExists, GameSessionNotFound
from app.models import db
from app.repositories import PlayerRepository, GameRepository
from app.schemas import PlayerOutputSchema, CreateGameSessionInputSchema, \
    GameSessionOutputSchema, GameResultOutputSchema, SessionIdPathInputSchema, GameMovePathInputSchema, \
    PlayerInputSchema, PlayerStatsSchema, PlayersStatsOutputSchema

api = APIBlueprint('api', __name__, url_prefix='/api')
game_tag = Tag(name='Game', description='Game related operations')


@api.get('/players/<player_name>',
         tags=[game_tag],
         responses={"200": PlayerOutputSchema},
         operation_id="get_player")
def get_player(path: PlayerInputSchema):
    player_repository = PlayerRepository(db.session)
    player = player_repository.get_player(player_name=path.player_name)

    if not player:
        raise PlayerNotFound

    return player.dict(), HTTPStatus.OK


@api.get('/players/statistics',
         tags=[game_tag],
         responses={"200": PlayersStatsOutputSchema},
         operation_id="get_all_players_statistics")
def get_all_players_statistics():
    player_repository = PlayerRepository(db.session)
    return {'results': [row._asdict() for row in player_repository.get_players_stats()]}, HTTPStatus.OK


@api.post('/players',
          tags=[game_tag],
          responses={"200": PlayerOutputSchema},
          operation_id="create_player")
def create_player(body: PlayerInputSchema):
    player_repository = PlayerRepository(db.session)
    player = player_repository.get_player(player_name=body.player_name)

    if player:
        raise PlayerAlreadyExists

    player = player_repository.create_player(player_name=body.player_name)
    return player.dict(), HTTPStatus.CREATED


@api.post('/game-sessions',
          tags=[game_tag],
          responses={"200": GameSessionOutputSchema},
          operation_id="create_game_session")
def create_game_session(body: CreateGameSessionInputSchema):
    game_repository = GameRepository(db.session)
    game_session = game_repository.create_game_session(player_id=body.player_id)

    if not game_session:
        raise GameSessionNotFound

    return game_session.dict(), HTTPStatus.CREATED


@api.get('/game-sessions/<session_id>',
         tags=[game_tag],
         responses={"200": GameSessionOutputSchema},
         operation_id="get_game_session")
def get_game_session(path: SessionIdPathInputSchema):
    game_repository = GameRepository(db.session)
    game_session = game_repository.get_game_session(session_id=path.session_id)

    if not game_session:
        raise GameSessionNotFound

    return game_session.dict(), HTTPStatus.OK


@api.post('/game-sessions/<session_id>/new-game',
          tags=[game_tag],
          responses={"200": GameSessionOutputSchema},
          operation_id="start_new_game")
def start_new_game(path: SessionIdPathInputSchema):
    game_repository = GameRepository(db.session)
    game_session = game_repository.get_game_session(session_id=path.session_id)

    if not game_session:
        raise GameSessionNotFound

    game_session.start_game()
    return game_session.dict(), HTTPStatus.OK


@api.post('/game-sessions/<session_id>/move/<move>',
          tags=[game_tag],
          responses={"200": GameResultOutputSchema},
          operation_id="make_move")
def make_move(path: GameMovePathInputSchema):
    game_repository = GameRepository(db.session)
    game_session = game_repository.get_game_session(session_id=path.session_id)

    if not game_session:
        raise GameSessionNotFound

    result = game_session.play_turn(path.move)
    return {'result': result}, HTTPStatus.OK


@api.post('/game-sessions/<session_id>/credits',
          tags=[game_tag],
          responses={"200": GameSessionOutputSchema},
          operation_id="add_credits")
def add_credits(path: SessionIdPathInputSchema):
    game_repository = GameRepository(db.session)
    game_session = game_repository.get_game_session(session_id=path.session_id)

    if not game_session:
        raise GameSessionNotFound

    game_session.add_credits()
    return game_session.dict(), HTTPStatus.OK
