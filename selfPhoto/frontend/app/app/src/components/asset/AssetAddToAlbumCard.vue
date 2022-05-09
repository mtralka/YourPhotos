<script setup lang="ts"></script>

<template>
  <q-card>
    <q-card-section class="row items-center q-pb-none">
      <div class="text-h6">{{ $t('addTo') }}</div>
      <q-space />
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>

    <q-card-section>
      <q-list style="min-width: 200x; min-height: 150px">
        <!-- <q-item clickable v-close-popup>
                    <q-item-section>{{ $t('addToAlbum') }}</q-item-section>
                </q-item> -->
        <q-item-label header class="text-uppercase text-subtitle2">{{
          $t('allAlbums')
        }}</q-item-label>

        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-avatar square>
              <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            <q-item-label>Example album name</q-item-label>
            <q-item-label caption lines="2"
              >Jan 12 - Jan 16th * 45 items</q-item-label
            >
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>
