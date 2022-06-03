<template>
  <router-view />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { OpenAPI } from './api';

OpenAPI.BASE = 'http://localhost:8000';

export default defineComponent({
  name: 'App',
});
</script>
