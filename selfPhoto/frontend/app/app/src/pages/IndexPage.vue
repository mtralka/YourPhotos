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

let fakeAssets = [];
onMounted(async () => {
  //  assetStore.loadAssets({}).then(() => {
  //   infiniteScrollContainer.value.resume();
  // });
  await userStore.login({
    username: 'example@example.org',
    password: 'example',
  });

  await assetStore.refreshAssets();
  console.log(assetStore.getAssets);

  // for (let i = 0; i < 30; i++) {
  //   fakeAssets.push({
  //     id: i,
  //     thumbnail: `https://random.imagecdn.app/199/3${i
  //       .toString()
  //       .padStart(2, '0')}`,
  //   });
  // }
  // assetStore.assets = fakeAssets;
});

// const onLoad = (index, done) => {
//   const numberOfAssets = assetStore.getAssets.length;
//   const skip = assetStore.calculatePaginationIndex(index);

//   console.log("loading new")
//   for (let i = index; i < index + 30; i++) {
//     fakeAssets.push({
//       id: i,
//       thumbnail: `https://random.imagecdn.app/199/3${i
//         .toString()
//         .padStart(2, '0')}`,
//     });
//   }
//   done()
//   assetStore.assets = fakeAssets;
//   // assetStore
//   //   .loadAssets({
//   //     skip: skip,
//   //   })
//   //   .then(() => {
//   //     if (assetStore.getAssets.length === numberOfAssets) {
//   //       done(true);
//   //     } else {
//   //       done();
//   //     }
//   //   });
// };

// const navigateToAsset = (asset, index) => {
//   assetStore.currentAsset = asset;
//   assetStore.currentAssetIndex = index;

//   // TODO
//   router.push({ path: `/m/${asset.id}` });
// };
</script>

<template>
  <div>
    <content-wrapper>
      <asset-gallery :assets="assetStore.getAssets" />
    </content-wrapper>
  </div>
</template>
