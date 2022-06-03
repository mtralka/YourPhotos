<script setup lang="ts">
import { Asset, AssetsService, CancelablePromise } from 'src/api';
// import { useAssetStore } from 'src/stores/assetStore';
import { ref, watch } from 'vue';
const computerUpload = ref(null);
const files = ref(null);

// const assetStore = useAssetStore();

const handleComputerUpload = () => {
  computerUpload.value.pickFiles();
};

watch(files, async (newValue, oldValue) => {
  const newAssets: CancelablePromise<Asset[]> =
    await AssetsService.createAssets({ formData: { assets: newValue } });
  console.log('new assets', newAssets);
  // assetStore.assets.concat(newAssets);
});
</script>

<template>
  <q-list class="fit" dense>
    <q-item-label header class="text-uppercase">{{
      $t('uploadfrom')
    }}</q-item-label>
    <q-item
      clickable
      v-ripple
      class="text-subtitle1 text-weight-normal"
      @click="handleComputerUpload"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="computer" />
      </q-item-section>
      <q-item-section class="q-pa-sm">{{ $t('computer') }}</q-item-section>
    </q-item>
    <q-file
      name="assets"
      ref="computerUpload"
      multiple
      v-model="files"
      style="display: none"
    />
  </q-list>
</template>
