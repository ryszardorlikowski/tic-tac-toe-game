from http import HTTPStatus

from flask_openapi3 import APIBlueprint, Tag

from app import db
from app.repositories import GameRepository, PlayerRepository
from app.schemas import PlayerSchema, GameSessionSchema, CreateGameSessionSchema, PlayerPathSchema, CreateGameSchema, \
    GameSchema

api = APIBlueprint('api', __name__, url_prefix='/api')
game_tag = Tag(name='Game', description='Game related operations')


@api.get('/players/<player_name>',
         tags=[game_tag],
         responses={"200": PlayerSchema},
         operation_id="get_or_create_player")
def get_or_create_player(path: PlayerPathSchema):
    player_repository = PlayerRepository(db.session)
    player = player_repository.get_or_create_player(player_name=path.player_name)

    return player.dict(), HTTPStatus.OK


@api.post('/game-sessions',
          tags=[game_tag],
          responses={"200": GameSessionSchema},
          operation_id="create_game_session")
def create_game_session(body: CreateGameSessionSchema):
    game_repository = GameRepository(db.session)
    game_session = game_repository.create_game_session(player_id=body.player_id)
    return game_session.dict(), HTTPStatus.CREATED


@api.post('/games',
          tags=[game_tag],
          responses={"200": GameSchema},
          operation_id="create_game")
def create_game(body: CreateGameSchema):
    game_repository = GameRepository(db.session)
    game = game_repository.create_game(game_session_id=body.game_session_id)
    return game.dict(), HTTPStatus.CREATED
