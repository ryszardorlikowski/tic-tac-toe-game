from .extensions import socketio, db
from .repositories import GameRepository


@socketio.on('update_session_end_time')
def update_end_time_handler(data):
    game_repository = GameRepository(db.session)
    game_session = game_repository.get_game_session(session_id=data['session_id'])
    game_session.update_end_time()
