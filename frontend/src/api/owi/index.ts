/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export { ApiError } from './core/ApiError';
export { CancelablePromise, CancelError } from './core/CancelablePromise';
export { OpenAPI } from './core/OpenAPI';
export type { OpenAPIConfig } from './core/OpenAPI';

export type { CreateGameSessionInputSchema } from './models/CreateGameSessionInputSchema';
export { GameResult } from './models/GameResult';
export type { GameResultOutputSchema } from './models/GameResultOutputSchema';
export type { GameSessionOutputSchema } from './models/GameSessionOutputSchema';
export type { PlayerInputSchema } from './models/PlayerInputSchema';
export type { PlayerOutputSchema } from './models/PlayerOutputSchema';
export type { PlayersStatsOutputSchema } from './models/PlayersStatsOutputSchema';
export type { PlayerStatsSchema } from './models/PlayerStatsSchema';
export type { UnprocessableEntity } from './models/UnprocessableEntity';

export { GameService } from './services/GameService';
