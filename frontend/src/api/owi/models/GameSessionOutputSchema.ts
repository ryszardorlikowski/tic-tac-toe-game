/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { GameResult } from './GameResult';

export type GameSessionOutputSchema = {
    board: Array<string>;
    credits: number;
    draws: number;
    end_time?: string;
    id: number;
    losses: number;
    result?: GameResult;
    start_time: string;
    wins: number;
};

