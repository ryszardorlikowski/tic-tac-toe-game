<template>
  <div class="container">
    <van-grid :column-num="3" class="board">
      <van-grid-item class="cell" icon="circle" v-for="(sign, index) in board" @click="makeMove(index)"
                     :style="sign!==' ' || lockBoard && {'pointer-events': 'none', 'cursor': 'not-allowed'}">
        <van-icon name="circle" v-if="sign==='O'"/>
        <van-icon name="cross" v-if="sign==='X'"/>
      </van-grid-item>
    </van-grid>
    <van-button v-if="lockBoard" round type="primary" @click="startNewGame">
      Start new game
    </van-button>
  </div>
  <van-popup v-model:show="showResultPopup" :closeable="false" :style="{ padding: '64px',  background: '#3880e0' }">
    <div class="result">
      You
      <span v-if="gameResult?.result === 0">draw! </span>
      <span v-if="gameResult?.result === 1">win! </span>
      <span v-if="gameResult?.result === 2">lose! </span>
    </div>
    <van-button v-if="lockBoard" round type="primary" @click="showResultPopup=false">
      Close
    </van-button>
  </van-popup>

  <van-popup v-model:show="showCreditsPopup" :closeable="false" :style="{ padding: '64px',  background: '#3880e0' }">
    <div class="result">
      You don't have enough credits to play
    </div>
    <van-button v-if="lockBoard" round type="primary" @click="backToHome">
      Back to home
    </van-button>
    <van-button v-if="lockBoard" round type="primary" @click="showCreditsPopup=false">
      Close
    </van-button>
  </van-popup>
</template>

<script setup lang="ts">
import {PropType, ref} from "vue";
import {useGameSessionStore} from "../store/GameSessionStore";
import {showNotify} from "vant";
import {GameResultOutputSchema} from "../api/owi";

const showResultPopup = ref(false)
const showCreditsPopup = ref(false)
const lockBoard = ref(true)
const gameResult = ref<GameResultOutputSchema | null>(null)
defineProps({
  board: Object as PropType<Array<string>>
})
const gameSessionStore = useGameSessionStore()
const startNewGame = async () => {
  showResultPopup.value = false;
  try {
    await gameSessionStore.startNewGame()
    showNotify({type: 'success', message: 'New game started'});
    lockBoard.value = false;
  } catch (error: any) {
    showCreditsPopup.value = true;
    showNotify({type: 'danger', message: error?.body?.message});
  }

}

const backToHome = () => {
  gameSessionStore.resetSession();
}

const makeMove = async (index: number) => {
  gameResult.value = await gameSessionStore.makeMove(index);
  await gameSessionStore.refreshGameSession();
  if (gameResult.value.result === 0 ||
      gameResult.value.result === 1 ||
      gameResult.value.result === 2) {
    showResultPopup.value = true
    lockBoard.value = true
  }
}

</script>
<style scoped>
.board {
  max-width: 600px;
}

.container {
  min-height: 600px;
  display: flex;
  justify-content: start;
  align-items: center;
  flex-direction: column;
}

.cell {
  padding: 5px;
  height: 200px;
  width: 200px;
  font-size: 150px;
  cursor: pointer;
}

.cell:hover {
  background: #e6e6e6;
}

.result {
  margin-bottom: 15px;
  font-size: 30px;
  color: white;
  text-align: center;
}
</style>