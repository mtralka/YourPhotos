<script setup lang="ts">
// import { useQuasar } from 'quasar';
import { useUserStore } from 'src/stores/userStore';
import { useAssetStore } from 'src/stores/assetStore';
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';

// const $q = useQuasar();

const userStore = useUserStore();
const assetStore = useAssetStore();
const router = useRouter();

const infiniteScrollContainer = ref(null);

onMounted(async () => {
  // userStore
  //   .login({
  //     username: 'example@example.org',
  //     password: 'example',
  //   })
  //   .then(() => {
  //     userStore.loadAssets({ limit: assetLimit });
  //   })
  //   .then(() => {
  //     infiniteScrollContainer.value.resume();
  //   });
  assetStore.loadAssets({}).then(() => {
    infiniteScrollContainer.value.resume();
  });

  const fakeAssets = [];
  for (let i = 0; i < 30; i++) {
    fakeAssets.push({
      id: i,
      thumbnail: `https://random.imagecdn.app/200/3${i
        .toString()
        .padStart(2, '0')}`,
    });
  }

  assetStore.assets = fakeAssets;
});

function refresh(done) {
  assetStore.refreshAssets().then(() => {
    done();
  });

  if (!infiniteScrollContainer.value) {
    return;
  }
  infiniteScrollContainer.value.reset();
  infiniteScrollContainer.value.resume();
}

function onLoad(index, done) {
  const numberOfAssets = assetStore.getAssets.length;
  const skip = assetStore.calculatePaginationIndex(index);
  assetStore
    .loadAssets({
      skip: skip,
    })
    .then(() => {
      if (assetStore.getAssets.length === numberOfAssets) {
        done(true);
      } else {
        done();
      }
    });
}

const navigateToAsset = (asset, index: number) => {
  assetStore.currentAsset = asset;
  assetStore.currentAssetIndex = index;
  // TODO change to asset id
  // and current album
  router.push({ path: `/m/${asset}` });
};
</script>
<template>
  <q-page class="row items-center justify-evenly">
    <q-pull-to-refresh @refresh="refresh">
      <q-infinite-scroll
        @load="onLoad"
        :offset="500"
        ref="infiniteScrollContainer"
      >
        <div class="row items-center justify-evenly q-gutter-xs">
          <!-- <div v-for="asset in userStore.getAssets" :key="asset.id"> -->
          <!--  // :src="'http://localhost:8000/api/v1/thumbnail/' + asset.id" -->
          <div v-for="(index, asset) in 30" :key="asset">
            <!-- <router-link :to="`/a/${asset}`"> -->
            <!-- style="max-height: 300px; width: 21vw" -->
            <div
              style="min-height: 25vh; min-width: 21vw"
              :id="asset"
              @click="navigateToAsset(asset, index)"
            >
              <!-- :src="`http://placekitten.com/200/300`" -->
              <!-- style="max-height: 300px; width: 21vw" -->
              <q-img
                class="q-pa-sm cursor-pointer"
                :src="`https://random.imagecdn.app/200/3${index
                  .toString()
                  .padStart(2, '0')}`"
                loading="lazy"
                height="100%"
                width="100%"
                no-native-menu
                fit="contain"
              >
                <!-- <div class="text-subtitle2 absolute-top text-center">Title</div> -->
              </q-img>
            </div>
            <!-- </router-link> -->
          </div>
        </div>
      </q-infinite-scroll>
    </q-pull-to-refresh>
  </q-page>
</template>

<!-- <style lang="scss" scoped>
$x: 4;

@for $i from 1 through ($x - 1) {
  .item:nth-child(#{$x}n + #{$i}) {
    order: #{$i};
  }
}

.item:nth-child(#{$x}n) {
  order: #{$x};
}
</style> -->
