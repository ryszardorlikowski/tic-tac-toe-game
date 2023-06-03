/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreateGameSessionInputSchema } from '../models/CreateGameSessionInputSchema';
import type { GameResultOutputSchema } from '../models/GameResultOutputSchema';
import type { GameSessionOutputSchema } from '../models/GameSessionOutputSchema';
import type { PlayerInputSchema } from '../models/PlayerInputSchema';
import type { PlayerOutputSchema } from '../models/PlayerOutputSchema';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class GameService {

    /**
     * @returns GameSessionOutputSchema OK
     * @throws ApiError
     */
    public static createGameSession({
        requestBody,
    }: {
        requestBody?: CreateGameSessionInputSchema,
    }): CancelablePromise<GameSessionOutputSchema> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/game-sessions',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

    /**
     * @returns GameSessionOutputSchema OK
     * @throws ApiError
     */
    public static getGameSession({
        sessionId,
    }: {
        sessionId: number,
    }): CancelablePromise<GameSessionOutputSchema> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/game-sessions/{session_id}',
            path: {
                'session_id': sessionId,
            },
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

    /**
     * @returns GameSessionOutputSchema OK
     * @throws ApiError
     */
    public static addCredits({
        sessionId,
    }: {
        sessionId: number,
    }): CancelablePromise<GameSessionOutputSchema> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/game-sessions/{session_id}/credits',
            path: {
                'session_id': sessionId,
            },
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

    /**
     * @returns GameResultOutputSchema OK
     * @throws ApiError
     */
    public static makeMove({
        sessionId,
        move,
    }: {
        sessionId: number,
        move: number,
    }): CancelablePromise<GameResultOutputSchema> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/game-sessions/{session_id}/move/{move}',
            path: {
                'session_id': sessionId,
                'move': move,
            },
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

    /**
     * @returns GameSessionOutputSchema OK
     * @throws ApiError
     */
    public static startNewGame({
        sessionId,
    }: {
        sessionId: number,
    }): CancelablePromise<GameSessionOutputSchema> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/game-sessions/{session_id}/new-game',
            path: {
                'session_id': sessionId,
            },
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

    /**
     * @returns PlayerOutputSchema OK
     * @throws ApiError
     */
    public static createPlayer({
        requestBody,
    }: {
        requestBody?: PlayerInputSchema,
    }): CancelablePromise<PlayerOutputSchema> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/players',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

    /**
     * @returns PlayerOutputSchema OK
     * @throws ApiError
     */
    public static getPlayer({
        playerName,
    }: {
        playerName: string,
    }): CancelablePromise<PlayerOutputSchema> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/players/{player_name}',
            path: {
                'player_name': playerName,
            },
            errors: {
                422: `Unprocessable Entity`,
            },
        });
    }

}
