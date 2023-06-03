<template>
  <van-button type="primary" round block @click="showPopup">Create new player</van-button>
  <van-popup v-model:show="show" :style="{ padding: '64px',  background: '#dde7f5' }">
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
          Create player
        </van-button>
      </div>
    </van-form>
  </van-popup>
</template>

<script setup lang="ts">
import {ref} from 'vue';
import {useGameSessionStore} from "../store/gameSessionStore";
import {showNotify} from 'vant';

const gameSessionStore = useGameSessionStore()
const show = ref(false);
const showPopup = () => {
  show.value = true;
};
const playerName = ref('');
const onSubmit = async () => {
  try {
    await gameSessionStore.createPlayer(playerName.value);
    showNotify({ type: 'success', message: 'Player created' });
    show.value = false;
  } catch (error: any) {
    showNotify({ type: 'danger', message: error?.body?.message });
  }
}
</script>

<style scoped>

</style>