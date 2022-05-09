<script setup lang="ts">
// const emit = defineEmits(['close']);

const emit = defineEmits<{
  (e: 'close'): void;
}>();
</script>

<template>
  <div
    class="fit column no-wrap justify-start items-start content-start q-pa-md"
  >
    <div class="row items-center justify-evenly">
      <q-btn
        flat
        round
        no-wrap
        color="gray"
        icon="close"
        no-caps
        class=""
        @click="$emit('close')"
      >
      </q-btn>
      <p class="text-subtitle1 text-weight-light">
        {{ $t('info') }}
      </p>
    </div>

    <q-input
      class="full-width q-my-md q-px-sm"
      :label="$t('addADescription')"
      autogrow
      dense
    />

    <q-list class="fit" padding>
      <q-item-label header>{{ $t('details') }}</q-item-label>

      <q-item clickable v-ripple class="q-my-sm">
        <q-item-section avatar>
          <q-icon color="grey" name="today" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Apr 23</q-item-label>
          <q-item-label caption lines="2">Sat, 5:31 PM GMT-0700</q-item-label>
        </q-item-section>
      </q-item>

      <q-item clickable v-ripple class="q-my-sm">
        <q-item-section avatar>
          <q-icon color="grey" name="crop_original" />
        </q-item-section>

        <q-item-section>
          <q-item-label>PXL_20220424_003157621.MP.jpg</q-item-label>
          <q-item-label caption lines="2"
            >12.2MP 4032 × 3024 8.7 MB</q-item-label
          >
        </q-item-section>
      </q-item>
      <q-item clickable v-ripple class="q-my-sm">
        <q-item-section avatar>
          <q-icon color="grey" name="camera" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Google Pixel 3 XL</q-item-label>
          <q-item-label caption lines="2">ƒ/1.8 1/2904.44mm ISO46</q-item-label>
        </q-item-section>
      </q-item>
      <q-item clickable v-ripple class="q-my-sm">
        <q-item-section avatar>
          <q-icon color="grey" name="file_upload" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Uploaded from Android device</q-item-label>
        </q-item-section>
      </q-item>
      <q-item clickable v-ripple class="q-my-sm">
        <q-item-section avatar>
          <q-icon color="grey" name="place" />
        </q-item-section>

        <q-item-section>
          <q-item-label>California</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>
