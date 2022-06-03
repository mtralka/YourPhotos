<script setup lang="ts">
import assetGallery from 'src/components/assetGallery.vue';
import contentWrapper from 'src/components/contentWrapper.vue';
import { useAssetStore } from 'src/stores/assetStore';
import { useUserStore } from 'src/stores/userStore';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const assetStore = useAssetStore();
const userStore = useUserStore();
const router = useRouter();

onMounted(async () => {
  if (!userStore.getJWT) {
    await userStore.login({
      username: 'example@example.org',
      password: 'example',
    });
  }

  // if (assetStore.getAssets.length === 0) {
  //   await assetStore.loadAssets({ skip: 0 });
  // }
});

// on refresh
// assetStore.refreshAssets().then(() => {
//     done();
//   });
</script>

<template>
  <div>
    <content-wrapper>
      <asset-gallery :assets="assetStore.getAssets" />
    </content-wrapper>
  </div>
</template>
