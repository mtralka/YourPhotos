<script setup lang="ts">
import assetGallery from 'src/components/assetGallery.vue';
import contentWrapper from 'src/components/contentWrapper.vue';
import pageSubHeading from 'src/components/pageSubHeading.vue';
import { useAssetStore } from 'src/stores/assetStore';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const assetStore = useAssetStore();
const router = useRouter();

onMounted(() => {
  // load favorite assets
});
</script>

<template>
  <div>
    <page-sub-heading :title="$t('favorites')" />
    <content-wrapper>
      <asset-gallery :assets="[]" />
    </content-wrapper>
  </div>
</template>
