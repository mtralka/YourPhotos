<script setup lang="ts">
// const emit = defineEmits(['download', 'addToAlbum']);

const emit = defineEmits<{
  (e: 'download'): void;
  (e: 'addToAlbum'): void;
}>();
</script>
<template>
  <q-list style="min-width: 175px">
    <q-item clickable v-close-popup @click="$emit('download')">
      <q-item-section>{{ $t('download') }}</q-item-section>
      <q-item-section side>
        <span> Shift + D </span>
      </q-item-section>
    </q-item>
    <q-item clickable v-close-popup @click="$emit('addToAlbum')">
      <q-item-section>{{ $t('addToAlbum') }}</q-item-section>
    </q-item>
  </q-list>
</template>
