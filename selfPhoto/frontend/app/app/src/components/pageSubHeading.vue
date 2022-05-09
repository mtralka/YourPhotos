<script setup lang="ts">
const props = defineProps<{
  title?: string;
}>();
</script>

<template>
  <div>
    <div
      class="full-width row no-wrap justify-between items-center q-px-lg q-mt-lg"
    >
      <slot name="left">
        <h1 class="text-subtitle1 text-weight-light">
          {{ title || '' }}
        </h1>
      </slot>

      <div>
        <slot name="right"> </slot>
      </div>
    </div>
    <q-separator class="q-my-md q-mx-lg" />
  </div>
</template>
