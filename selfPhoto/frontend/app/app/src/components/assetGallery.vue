<script setup lang="ts">
import { API } from 'src/api/';
import { useAssetStore } from 'src/stores/assetStore';
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';

const assetStore = useAssetStore();
const router = useRouter();

const props = defineProps<{
  assets: Array<any>;
  title?: string;
  infiniteScrollOffset?: number;
}>();

const emit = defineEmits<{
  (e: 'infiniteScrollLoad', index: number, done: any): void;
  (e: 'assetClicked', asset: any, index: number): void;
  (e: 'refresh', done: any): void;
}>();

const infiniteScrollContainer = ref(null);

onMounted(() => {
  // setTimeout(() => {
  //   infiniteScrollContainer.value.reset();
  //   infiniteScrollContainer.value.resume();
  //   // infiniteScrollContainer.value.trigger();
  // }, 100);
  // infiniteScrollContainer.value.reset();
});

/*******
 *
 * Watchers
 *
 *******/

watch(props.assets, () => {
  infiniteScrollContainer.value.resume();
});

/*******
 *
 * Methods
 *
 *******/

/**
 * Refresh pipeline triggered by pull-to-refresh
 */
const handleRefresh = (done: any) => {
  emit('refresh', done);

  assetStore.refreshAssets().then(() => {
    done();
  });

  if (!infiniteScrollContainer.value) {
    return;
  }
  infiniteScrollContainer.value.reset();
  infiniteScrollContainer.value.resume();
};

/**
 * Loading pipeline triggered by hitting infinite-scroll threshold
 */
const handleInfiniteScrollLoad = (index: number, done: any) => {
  emit('infiniteScrollLoad', index, done);

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
};

/**
 * Clicked asset pipeline
 */
const handleAssetClick = (asset: any, index: number) => {
  emit('assetClicked', asset, index);

  assetStore.currentAsset = asset;
  assetStore.currentAssetIndex = index;

  // TODO
  router.push({ path: `/m/${asset.id}` });
};
</script>

<template>
  <q-page class="row items-center justify-evenly">
    <q-pull-to-refresh @refresh="handleRefresh">
      <q-infinite-scroll
        @load="handleInfiniteScrollLoad"
        :offset="infiniteScrollOffset || 500"
        ref="infiniteScrollContainer"
      >
        <div class="row items-center justify-evenly q-gutter-xs q-pb-md">
          <div v-for="(asset, index) in assets" :key="asset.id">
            <div
              style="min-width: max(16vw, 100px)"
              :id="asset.id"
              @click="handleAssetClick(asset, index)"
            >
              <!-- :src="asset.thumbnail" -->
              <q-img
                class="q-pa-sm cursor-pointer"
                :src="`${API}/thumbnail/${asset.id}`"
                loading="lazy"
                height="100%"
                width="100%"
                no-native-menu
                alt="TODO"
                fit="cover"
                ratio="1"
              >
                <template #loading>
                  <q-skeleton
                    height="100%"
                    width="100%"
                    square
                    animations="fade"
                  />
                </template>
              </q-img>
            </div>
          </div>
        </div>
      </q-infinite-scroll>
    </q-pull-to-refresh>
  </q-page>
</template>
