from flask import Blueprint, jsonify
from pydantic import BaseModel
from flask_openapi3 import OpenAPI, APIBlueprint, Tag

api = APIBlueprint('api', __name__, url_prefix='/api')
game_tag = Tag(name='Game', description='Game related operations')


class GameResponse(BaseModel):
    test: int
    test2: str


@api.get('/',
         tags=[game_tag],
         responses={"200": GameResponse},
         operation_id="get_test")
def index():
    return jsonify({'test': 1, 'test2': 2})

