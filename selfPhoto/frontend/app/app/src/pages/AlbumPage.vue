<script setup lang="ts">
import { onKeyStroke } from '@vueuse/core';
import assetGallery from 'src/components/assetGallery.vue';
import contentWrapper from 'src/components/contentWrapper.vue';
import { useAssetStore } from 'src/stores/assetStore';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const assetStore = useAssetStore();

const route = useRoute();
const router = useRouter();

const albumId = route.params.id;

let fakeAssets = [];
onMounted(async () => {
  /*
  assetStore.loadAssets({
      album:albumId
  }).then(() => {
    infiniteScrollContainer.value.resume();
  });
  */
  await assetStore.refreshAssets();
  // assetStore.clearAssets();

  // for (let i = 0; i < 30; i++) {
  //   fakeAssets.push({
  //     id: i,
  //     thumbnail: `https://random.imagecdn.app/198/3${i
  //       .toString()
  //       .padStart(2, '0')}`,
  //   });
  // }
});

onKeyStroke('Escape', (e) => {
  e.preventDefault();
  router.go(-1);
});
</script>
<template>
  <div>
    <q-header class="bg-white text-grey-8" height-hint="64">
      <q-toolbar
        class="row no-wrap full-width row justify-end items-center content-center"
        style="height: 64px"
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
          color="gray"
          icon="arrow_back"
          no-caps
          @click="$router.go(-1)"
          ><q-tooltip>{{ $t('back') }}</q-tooltip>
        </q-btn>

        <q-space />

        <div>
          <!-- 
                ######
                ## Add Photos
                #####
            -->
          <q-btn
            flat
            dense
            round
            no-wrap
            color="gray"
            icon="add_photo_alternate"
            no-caps
            class="q-ml-sm q-px-md"
          >
            <q-tooltip>{{ $t('addPhotos') }}</q-tooltip>
          </q-btn>

          <!-- 
                ######
                ## Download Photos
                #####
            -->
          <q-btn
            round
            dense
            flat
            color="text-grey-7"
            icon="cloud_download"
            class="q-ml-sm q-px-md"
            ><q-tooltip>{{ $t('download') }}</q-tooltip>
          </q-btn>

          <!-- 
                ######
                ## Share
                #####
            -->
          <q-btn
            round
            dense
            flat
            color="text-grey-7"
            icon="share"
            class="q-ml-sm q-px-md"
            ><q-tooltip>{{ $t('settings') }}</q-tooltip>
          </q-btn>
        </div>

        <q-separator vertical inset class="q-mx-md" />

        <!-- 
            ######
            ## Account Card
            #####
           -->
        <q-btn round flat @click="showAccountDialog = !showAccountDialog">
          <q-avatar size="26px">
            <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
          </q-avatar>
          <q-tooltip>{{ $t('account') }}</q-tooltip>
          <q-menu class="" anchor="top right" self="top right">
            <account-card />
          </q-menu>
        </q-btn>
      </q-toolbar>
    </q-header>
    <content-wrapper>
      <div
        class="full-width column no-wrap justify-start items-start content-start q-pb-xl q-pt-xl q-pl-md"
      >
        <div class="q-pb-lg">
          <h1 class="text-h3 q-pb-sm">Fake album title {{ albumId }}</h1>
          <p class="q-pr-xs text-caption text-grey-6">Apr 10th</p>
        </div>
        <div
          class="full-width row no-wrap justify-start items-start content-center q-gutter-xs"
        >
          <q-skeleton type="circle" size="36px" v-for="user in 3" :key="user" />
        </div>
      </div>
      <asset-gallery :assets="assetStore.getAssets" />
    </content-wrapper>
  </div>
</template>
