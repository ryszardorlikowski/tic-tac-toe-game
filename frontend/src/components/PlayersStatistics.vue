<template>
  <van-button type="primary" round block @click="showPopup">Players statistics</van-button>
  <van-popup v-model:show="show" :style="{ padding: '64px',  background: '#dde7f5' }">
    <van-loading v-if="loading" type="spinner"/>
    <div v-else>
      <div v-if="!data?.results.length">
        No players statistics
      </div>
      <div v-else class="player-stats" v-for="player in data?.results">
        <div class="cell"><small>Player name:</small> {{ player.player_name }}</div>
        <div class="cell"><small>Wins:</small> {{ player.wins }}</div>
        <div class="cell"><small>Losses:</small> {{ player.losses }}</div>
        <div class="cell"><small>Draws:</small> {{ player.draws }}</div>
        <div class="cell"><small>Play time:</small> {{ parseInt(player.game_duration_seconds.toString()) }}s</div>
      </div>
    </div>
  </van-popup>
</template>

<script setup lang="ts">
import {ref, watch} from 'vue';
import {GameService, PlayersStatsOutputSchema} from "../api/owi";

const show = ref(false);
const showPopup = () => {
  show.value = true;
};
const data = ref<PlayersStatsOutputSchema | null>(null);
const loading = ref<boolean>(false);
watch(show, async (value) => {
  if (value) {
    loading.value = true;
    data.value = await GameService.getAllPlayersStatistics();
    loading.value = false;
  }
})
</script>

<style scoped>
.player-stats {
  display: flex;
  margin-bottom: 16px;
  min-width: 800px;
  border: 1px solid #000;
}

.cell {
  flex: 1;
  margin: 8px;
}
</style>