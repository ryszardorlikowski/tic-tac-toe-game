<template>
  <van-cell-group class="card" inset border>
    <van-cell title="Credits" :value="sessionInfo?.credits"/>
    <van-cell title="Wins" :value="sessionInfo?.wins"/>
    <van-cell title="Losses" :value="sessionInfo?.losses"/>
    <van-cell title="Draws" :value="sessionInfo?.draws"/>
    <van-cell title="Duration" :value="timeDifference"/>
    <van-button round type="primary" :disabled="sessionInfo?.credits!==0" @click="addCredits">
      Add credits
    </van-button>
  </van-cell-group>

</template>

<script setup lang="ts">
import {GameSessionOutputSchema} from "../api/owi";
import { onMounted, onUnmounted, PropType, ref} from "vue";
import {useGameSessionStore} from "../store/GameSessionStore";
const gameSessionStore = useGameSessionStore();
const props = defineProps({
  sessionInfo: Object as PropType<GameSessionOutputSchema>
})
const timeDifference = ref('0s');
let intervalId: any;



onMounted(() => {
  calculateDifference();
  intervalId = setInterval(calculateDifference, 1000);
});

onUnmounted(() => {
  clearInterval(intervalId);
});

const calculateDifference = () => {
  if (!props.sessionInfo) return;
  const date: Date = new Date(props.sessionInfo.start_time);
  const now: Date = new Date();
  let difference: number = now.getTime() - date.getTime();
  difference = difference / 1000; // calculate difference in seconds
  timeDifference.value = parseInt(difference.toString()) + 's';
};

const addCredits = () => {
  gameSessionStore.addCredits();
}
</script>
<style>

</style>
<style scoped>
.card{
  padding: 10px;
  width: 150px;
}

:deep(.van-cell__value){
  font-weight: bolder;
  font-size: 15px!important;
  color: #1989fa;
}
</style>