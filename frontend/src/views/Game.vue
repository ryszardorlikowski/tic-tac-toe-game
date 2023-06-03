<template>
  <van-row gutter="20">
    <van-col span="8">
      <GameSessionInfo class="content" v-if="gameSessionStore.session" :session-info="gameSessionStore.session"/>
    </van-col>
    <van-col span="16">
      <GameBoard class="content" v-if="gameSessionStore.session" :board="gameSessionStore.session.board"/>
    </van-col>
  </van-row>
</template>

<script setup lang="ts">
import {onBeforeMount, onBeforeUnmount} from "vue";
import {useGameSessionStore} from "../store/GameSessionStore";
import GameSessionInfo from "../components/GameSessionInfo.vue";
import GameBoard from "../components/GameBoard.vue";
import {io} from "socket.io-client";
import {OpenAPI} from "../api/owi";

let socketInterval: any
const socket = io(OpenAPI.BASE);
const gameSessionStore = useGameSessionStore()
onBeforeMount(async () => {
  await gameSessionStore.joinGameSession()
  socketInterval = setInterval(() => {
    socket.emit('update_session_end_time', {session_id: gameSessionStore.session?.id});
  }, 1000)
})

onBeforeUnmount(() => {
  clearInterval(socketInterval);
})
</script>

<style scoped>
.content {
  max-width: 100%;
}
</style>