<template>
  <div class="container">
    <Game class="content"  v-if="gameSessionStore.player"/>
    <Home v-else/>
  </div>
</template>
<script setup lang="ts">
import Home from './views/Home.vue'
import Game from './views/Game.vue'
import {useGameSessionStore} from "./store/GameSessionStore";
const gameSessionStore = useGameSessionStore()
</script>

<style>
body{
  background: #89b8f6;
}
.content{
  width: 100vw;
}
</style>
