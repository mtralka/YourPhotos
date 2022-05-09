<script setup lang="ts">
import { useSettingsStore, eAlbumSortMethod } from 'src/stores/settingsStore';
import { computed } from 'vue';
import pageSubHeading from 'src/components/pageSubHeading.vue';
import contentWrapper from 'src/components/contentWrapper.vue';

const settingsStore = useSettingsStore();
</script>

<template>
  <div>
    <page-sub-heading :title="$t('albums')">
      <template v-slot:right>
        <q-btn
          round
          dense
          outlined
          flat
          color="text-grey-7"
          icon="add_box"
          class="q-ml-sm q-px-md"
          ><q-tooltip>{{ $t('createAlbum') }}</q-tooltip>
        </q-btn>

        <q-btn
          dense
          outlined
          flat
          no-caps
          color="text-gray-7"
          icon="swap_vert"
          class="q-ml-sm q-px-sm"
          :label="$t(settingsStore.getAlbumSortMethod)"
        >
          <q-menu
            class="q-pb-lg q-px-md q-pt-md"
            style="min-width: 100px"
            anchor="top right"
            self="top right"
          >
            <q-list style="min-width: 100px">
              <q-item
                clickable
                v-close-popup
                v-for="method in Object.values(eAlbumSortMethod)"
                :key="method"
                @click="settingsStore.albumSortMethod = method"
              >
                <q-item-section>{{ $t(method) }}</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
      </template>
    </page-sub-heading>
    <content-wrapper>
      <div class="row items-center justify-between q-gutter-md">
        <div
          v-for="album in 20"
          :key="album"
          class="col-5 col-sm-3 col-md-2 column no-wrap justify-start items-center content-start q-gutter-sm cursor-pointer"
          @click="$router.push(`/a/${album}`)"
        >
          <q-img
            src="https://cdn.quasar.dev/img/mountains.jpg"
            loading="lazy"
            no-native-menu
            alt="TODO"
            fit="cover"
            ratio="1"
            :img-style="{ borderRadius: '10px' }"
          >
            <template #loading>
              <q-skeleton
                height="100%"
                width="100%"
                animations="fade"
                style="{borderRadius: '10px'"
              />
            </template>
          </q-img>
          <div>
            <div class="text-body2 text-weight-normal text-left">
              Fake Album Name
            </div>
            <div class="text-caption text-weight-light grey-6 text-center">
              34 items - Shared
            </div>
          </div>
        </div>
      </div>
    </content-wrapper>
  </div>
</template>
