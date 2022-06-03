<script setup lang="ts">
import {
  onKeyStroke,
  useIdle,
  useMagicKeys,
  usePageLeave,
  usePointerSwipe,
  whenever,
} from '@vueuse/core';
import { Asset } from 'src/api';
import AssetAddToAlbumCard from 'src/components/asset/AssetAddToAlbumCard.vue';
import AssetInfoDrawer from 'src/components/asset/AssetInfoDrawer.vue';
import AssetMoreOptionsCard from 'src/components/asset/AssetMoreOptionsCard.vue';
import { useAssetStore } from 'src/stores/assetStore';
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const assetStore = useAssetStore();

const route = useRoute();
const router = useRouter();

const assetId = route.params.id;

const rightDrawerOpen = ref(false);
const showAddToAlbum = ref(false);
const container = ref(null);

const keys = useMagicKeys();
const { idle, lastActive } = useIdle(2000); // 5s
const isLeft = usePageLeave();
const { isSwiping, direction } = usePointerSwipe(container);

const assetSource = ref('');

onMounted(() => {
  // console.log("page id", assetId)
  // console.log("current asset", assetStore.getCurrentAsset)

  if (!assetStore.getCurrentAsset) {
    // pull from url
    console.log('undefinde');
    assetStore.setCurrentAssetById(assetId);
  } else if (assetStore.getCurrentAsset.id != assetId) {
    // pull from URL
    console.log('mismatch');
    assetStore.setCurrentAssetById(assetId);
  }
});

/*******
 *
 * Watchers
 *
 *******/

watch(isSwiping, (newValue, oldValue) => {
  if (!newValue) return;

  switch (direction.value) {
    case 'RIGHT':
      if (!hasPreviousAsset.value) return;
      changeAsset(-1);
      break;
    case 'LEFT':
      if (!hasNextAsset.value) return;
      changeAsset(1);
      break;
    // case 'UP':
    //   toggleInfo();
    //   break;
  }
});

/*******
 *
 * Methods
 *
 *******/

const goBack = () => {
  router.go(-1);
};

const toggleInfo = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value;

  // if opening
  // trigger load of metadata
};

const changeAsset = async (step: number) => {
  const newAsset: Asset | undefined = await assetStore.incrementAsset(step);
  // TODO
  if (!newAsset) return;
  router.replace({ path: `/m/${newAsset.id}` });
  // assetStore.setSequentialAsset(step).then(() => {
  //   // router.push({path: `/a/${assetStore.getCurrentAsset.id}`})
  //   // console.log(assetStore.getCurrentAsset);
  //   router.replace({ path: `/m/${assetStore.getCurrentAsset.id}` });
  // });
};

const downloadAsset = () => {
  console.log('downloading');
  if (!window) return;

  // window.open(`${API}/media/${assetStore.getCurrentAsset.id}`, '_blank');

  const url = window.URL.createObjectURL(
    new Blob([`/api/v1/${assetStore.getCurrentAsset.id}/media`])
  );
  const link = document.createElement('a');
  link.href = url;
  console.log(assetStore.getCurrentAsset);
  link.setAttribute(
    'download',
    assetStore.getCurrentAsset?.fileName +
      assetStore.getCurrentAsset?.fileExtension
  );
  document.body.appendChild(link);
  link.click();
};

const addToFavorites = async () => {
  /*
  add assId to favorites

  */
};

const addToTrash = async () => {
  /*
  add assId to trash

  */
};

/*******
 *
 * Computed
 *
 *******/

const hasNextAsset = computed(() => {
  return Boolean(assetStore.assets.at(assetStore.getCurrentAssetIndex + 1));
});

const hasPreviousAsset = computed(() => {
  return assetStore.getCurrentAssetIndex - 1 >= 0
    ? Boolean(assetStore.assets.at(assetStore.getCurrentAssetIndex - 1))
    : false;
});

/*******
 *
 * Keyboard shortcuts
 *
 *******/

onKeyStroke('ArrowRight', (e) => {
  e.preventDefault();
  if (!hasNextAsset.value) return;

  changeAsset(1);
});

onKeyStroke('ArrowLeft', (e) => {
  e.preventDefault();
  if (!hasPreviousAsset.value) return;

  changeAsset(-1);
});

onKeyStroke('i', (e) => {
  e.preventDefault();
  toggleInfo();
});

onKeyStroke('Escape', (e) => {
  e.preventDefault();
  goBack();
});

whenever(keys.shift_d || keys.shift_D, () => {
  downloadAsset();
});
</script>
<template>
  <q-layout view="hHh lpR fFf">
    <q-drawer
      show-if-above
      v-model="rightDrawerOpen"
      side="right"
      bordered
      no-swipe-open
      no-swipe-close
      :width="350"
      behavior="mobile"
    >
      <asset-info-drawer @close="toggleInfo" />
    </q-drawer>
    <q-page-container>
      <div ref="container" class="background">
        <div
          v-show="!idle && !rightDrawerOpen"
          class="absolute toolbar text-white q-py-md fit column no-wrap justify-start items-center"
          :class="[$q.screen.gt.xs ? 'q-px-xl' : '']"
        >
          <div
            class="row no-wrap full-width row justify-end items-center content-center"
            :class="[$q.screen.gt.xs ? 'q-gutter-sm' : 'q-gutter-xs']"
          >
            <!-- 
            ######
            ## Back
            #####
           -->
            <q-btn
              flat
              round
              no-wrap
              color="grey-2"
              icon="arrow_back"
              no-caps
              class="self-start"
              @click="goBack"
              ><q-tooltip>{{ $t('back') }}</q-tooltip>
            </q-btn>
            <q-space />

            <!-- 
            ######
            ## Share
            #####
           -->
            <q-btn
              flat
              round
              no-wrap
              color="grey-2"
              icon="share"
              no-caps
              disabled
              ><q-tooltip>{{ $t('share') }}</q-tooltip>
            </q-btn>

            <!-- 
            ######
            ## Edit
            #####
           -->
            <q-btn
              v-if="$q.screen.gt.xs"
              flat
              disabled
              round
              no-wrap
              color="grey-2"
              icon="edit"
              no-caps
              ><q-tooltip>{{ $t('edit') }}</q-tooltip>
            </q-btn>

            <!-- 
            ######
            ## Zoom
            #####
           -->
            <q-btn
              v-if="$q.screen.gt.xs"
              flat
              round
              no-wrap
              color="grey-2"
              icon="zoom_in"
              no-caps
              ><q-tooltip>{{ $t('zoom') }}</q-tooltip>
            </q-btn>

            <!-- 
            ######
            ## Info
            #####
           -->
            <q-btn
              flat
              round
              no-wrap
              color="grey-2"
              icon="info_outline"
              no-caps
              @click="toggleInfo"
              ><q-tooltip>{{ $t('info') }}</q-tooltip>
            </q-btn>

            <!-- 
            ######
            ## Favorite
            #####
           -->
            <q-btn flat round no-wrap color="grey-2" icon="star_border" no-caps
              ><q-tooltip>{{ $t('favorite') }}</q-tooltip>
            </q-btn>

            <!-- 
            ######
            ## Delete
            #####
           -->
            <q-btn
              flat
              round
              no-wrap
              color="grey-2"
              icon="delete_outline"
              no-caps
              ><q-tooltip>{{ $t('delete') }}</q-tooltip>
            </q-btn>

            <!-- 
            ######
            ## More Options
            #####
           -->
            <q-btn flat round no-wrap color="grey-2" icon="more_vert" no-caps>
              <q-tooltip>{{ $t('moreOptions') }}</q-tooltip>
              <q-menu
                class="q-pb-lg q-px-md q-pt-md"
                style="min-width: 100px"
                anchor="top right"
                self="top right"
              >
                <asset-more-options-card
                  @download="downloadAsset"
                  @addToAlbum="showAddToAlbum = true"
                />
              </q-menu>
            </q-btn>

            <!-- 
            ## Side effects - More Options
           -->
            <q-dialog
              v-model="showAddToAlbum"
              style="min-width: 200x; min-height: 200px"
            >
              <asset-add-to-album-card />
            </q-dialog>
          </div>
          <div
            v-if="$q.screen.gt.xs"
            class="full-height full-width row no-wrap items-center"
            :class="[
              !hasNextAsset && hasNextAsset
                ? 'justify-start'
                : 'justify-between',
            ]"
            style=""
          >
            <button
              class="full-height q-py-md column justify-center"
              style="background: transparent; border: none"
              @click="changeAsset(-1)"
              v-show="hasPreviousAsset"
            >
              <q-btn
                flat
                round
                no-wrap
                color="grey-2"
                icon="keyboard_arrow_left"
                no-caps
                size="lg"
                class="self-start"
              >
              </q-btn>
            </button>
            <q-space />
            <button
              class="full-height q-py-md column justify-center"
              style="background: transparent; border: none"
              @click="changeAsset(1)"
              v-show="hasNextAsset"
            >
              <q-btn
                flat
                round
                no-wrap
                color="grey-2"
                icon="keyboard_arrow_right"
                no-caps
                size="lg"
                class="self-start"
              >
              </q-btn>
            </button>
          </div>
        </div>
        <q-img
          ref="asset"
          img-class="q-pa-md"
          :src="
            assetStore.getCurrentAsset
              ? `http://localhost:8000/api/v1/assets/${assetStore.getCurrentAsset.id}/media`
              : ''
          "
          :placeholder-src="
            assetStore.getCurrentAsset
              ? `http://localhost:8000/api/v1/assets/${assetStore.getCurrentAsset.id}/thumbnail`
              : ''
          "
          loading="eager"
          fetchpriority="high"
          no-native-menu
          fit="contain"
          height="100%"
          width="100%"
        >
        </q-img>
      </div>
    </q-page-container>
  </q-layout>
</template>

<style lang="scss" scoped>
.background {
  width: 100vw;
  height: 100vh;
  background: black;
  overflow: hidden;
}

.toolbar {
  z-index: 100;
}
</style>
