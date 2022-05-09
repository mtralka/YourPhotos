<script setup lang="ts">
import pageSubHeading from 'src/components/pageSubHeading.vue';
import contentWrapper from 'src/components/contentWrapper.vue';
import assetGallery from 'src/components/assetGallery.vue';
import { useAssetStore } from 'src/stores/assetStore';
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const assetStore = useAssetStore();
const router = useRouter();

let fakeAssets = [];
onMounted(() => {
  for (let i = 0; i < 30; i++) {
    fakeAssets.push({
      id: i,
      thumbnail: `https://random.imagecdn.app/200/3${i
        .toString()
        .padStart(2, '0')}`,
    });
  }
  assetStore.assets = fakeAssets;

  //  assetStore.loadAssets({}).then(() => {
  //   infiniteScrollContainer.value.resume();
  // });
});

// const refresh = (done) => {
//   assetStore.refreshAssets().then(() => {
//     done();
//   });
// };

// const infiniteLoad = (index, done) => {
//   const numberOfAssets = assetStore.getAssets.length;
//   const skip = assetStore.calculatePaginationIndex(index);
//   assetStore
//     .loadAssets({
//       skip: skip,
//     })
//     .then(() => {
//       if (assetStore.getAssets.length === numberOfAssets) {
//         done(true);
//       } else {
//         done();
//       }
//     });
// };

// const handleAssetClick = (asset, index) => {
//   assetStore.currentAsset = asset;
//   assetStore.currentAssetIndex = index;

//   // TODO
//   router.push({ path: `/m/${asset.id}` });
// };
</script>

<template>
  <div>
    <page-sub-heading :title="$t('favorites')" />
    <content-wrapper>
      <asset-gallery :assets="fakeAssets" />
    </content-wrapper>
  </div>
</template>
