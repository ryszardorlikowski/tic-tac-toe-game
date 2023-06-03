<template>
  <van-row :gutter="200">
    <van-form @submit="onSubmit">
      <van-cell-group inset>
        <van-field
            v-model="playerName"
            label="Player name"
            placeholder="Enter player name"
            :rules="[{ required: true, message: 'Player name is required' }]"/>
      </van-cell-group>
      <div style="margin: 16px;">
        <van-button round block type="primary" native-type="submit">
          Start session
        </van-button>
      </div>
    </van-form>
  </van-row>
  <van-divider/>
  <div style="margin: 16px;">
    <CreatePlayerPopup/>
  </div>
  <div style="margin: 16px;">
    <PlayersStatistics/>
  </div>
</template>

<script setup lang="ts">
import {ref} from "vue";
import CreatePlayerPopup from "../components/CreatePlayerPopup.vue"
import PlayersStatistics from "../components/PlayersStatistics.vue"
import {useGameSessionStore} from "../store/GameSessionStore";
import {showNotify} from "vant";

const gameSessionStore = useGameSessionStore()
const playerName = ref('');
const onSubmit = async () => {
  try {
    await gameSessionStore.fetchPlayer(playerName.value)
  } catch (error: any) {
    showNotify({type: 'danger', message: error?.body?.message});
  }

}
</script>
<style scoped>

</style>