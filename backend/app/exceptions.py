class APIError(Exception):
    pass


class CannotStartNewGame(APIError):
    code = 400
    description = "Cannot start new game. Not enough credits."


class CannotAddCredits(APIError):
    code = 400
    description = "Cannot add credits. Credits are not zero."


class GameSessionNotFound(APIError):
    code = 404
    description = "Game session not found."


class NotAllowedMove(APIError):
    code = 400
    description = "Not allowed move."


class PlayerNotFound(APIError):
    code = 404
    description = "Player not found."


class PlayerAlreadyExists(APIError):
    code = 409
    description = "Player already exists."


class NotGameExists(APIError):
    code = 400
    description = "You have to start new game."