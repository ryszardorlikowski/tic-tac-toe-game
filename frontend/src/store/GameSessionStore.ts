import {defineStore} from 'pinia'
import {GameService, GameSessionOutputSchema, PlayerOutputSchema} from "../api/owi";

interface IGameSessionState {
    player: null | PlayerOutputSchema
    board: string[],
    session: null | GameSessionOutputSchema
}

export const useGameSessionStore = defineStore('gameSessionStore', {
    state: (): IGameSessionState => ({
        player: null,
        board: [],
        session: null,
    }),
    actions: {
        async fetchPlayer(playerName: string) {
            this.player = await GameService.getPlayer({playerName})
        },
        async createPlayer(playerName: string) {
            await GameService.createPlayer({requestBody: {player_name: playerName}})
        },
        async joinGameSession() {
            if (!this.player) {
                throw new Error('No player found')
            }
            this.session = await GameService.createGameSession({requestBody: {player_id: this.player.id}})
        },
        async refreshGameSession() {
            if (!this.session) {
                throw new Error('No session found')
            }
            this.session = await GameService.getGameSession({sessionId: this.session.id})
            console.log(this.session)
        },
        async startNewGame() {
            if (!this.session) {
                throw new Error('No session found')
            }
            this.session = await GameService.startNewGame({sessionId: this.session.id})
        },
        makeMove(move: number) {
            if (!this.session) {
                throw new Error('No session found')
            }
            return GameService.makeMove({
                sessionId: this.session.id,
                move: move
            });
        },
        resetSession() {
            this.player = null
            this.session = null
            this.board = []
        },
        async addCredits() {
            if (!this.session) {
                throw new Error('No session found')
            }
            this.session = await GameService.addCredits({sessionId: this.session.id})
        }

    },
})