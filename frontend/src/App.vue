
<template>
  {{state}}
  {{data}}
</template>
<script setup lang="ts">
import { io } from "socket.io-client";
import {onBeforeMount, reactive, ref} from "vue";
import axios from "axios";
const state = reactive({
  connected: false,
  fooEvents: [],
  barEvents: []
});
const data = ref()

const URL =  import.meta.env.VITE_APP_BACKEND_URL ?? "http://localhost:3000"
console.log(import.meta.env)
const socket = io(URL);
onBeforeMount(async () => {
  data.value = (await axios.get(URL + '/api')).data;
  socket.on("connect", () => {
    state.connected = true;
  });
});
</script>

<style scoped>

</style>
