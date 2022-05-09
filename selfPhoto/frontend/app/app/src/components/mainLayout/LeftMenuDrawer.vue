<script setup lang="ts"></script>

<template>
  <q-list class="q-pt-lg q-pr-md">
    <!-- <q-item-label header>{{ $t('details') }}</q-item-label> -->

    <q-item
      clickable
      v-ripple
      class="q-my-sm"
      to="/"
      active-class="bg-blue-2 text-blue-10 text-weight-medium round-right w-90"
    >
      <q-item-section avatar>
        <q-icon name="crop_original" />
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ $t('photos') }}</q-item-label>
      </q-item-section>
    </q-item>

    <q-item
      clickable
      v-ripple
      class="q-my-sm"
      to="/explore"
      active-class="bg-blue-2 text-blue-10 text-weight-medium round-right w-90"
    >
      <q-item-section avatar>
        <q-icon name="search" />
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ $t('explore') }}</q-item-label>
      </q-item-section>
    </q-item>

    <q-item
      clickable
      v-ripple
      class="q-my-sm"
      to="/share"
      active-class="bg-blue-2 text-blue-10 text-weight-medium round-right w-90"
    >
      <q-item-section avatar>
        <q-icon name="people" />
      </q-item-section>

      <q-item-section>
        <q-item-label class="text-subtitle1">{{ $t('share') }}</q-item-label>
      </q-item-section>
    </q-item>

    <q-item-label header>{{ $t('library') }}</q-item-label>

    <q-item
      clickable
      v-ripple
      class="q-my-sm"
      to="/favorites"
      active-class="bg-blue-2 text-blue-10 text-weight-medium round-right w-90"
    >
      <q-item-section avatar>
        <q-icon name="star_border" />
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ $t('favorites') }}</q-item-label>
      </q-item-section>
    </q-item>

    <q-item
      clickable
      v-ripple
      class="q-my-sm"
      to="/albums"
      active-class="bg-blue-2 text-blue-10 text-weight-medium round-right w-90"
    >
      <q-item-section avatar>
        <q-icon name="photo_album" />
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ $t('albums') }}</q-item-label>
      </q-item-section>
    </q-item>

    <q-item
      clickable
      v-ripple
      class="q-my-sm"
      to="/trash"
      active-class="bg-blue-2 text-blue-10 text-weight-medium round-right w-90"
    >
      <q-item-section avatar>
        <q-icon name="delete_outline" />
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ $t('trash') }}</q-item-label>
      </q-item-section>
    </q-item>
  </q-list>
</template>

<style scoped>
.round-right {
  border-radius: 0 45px 45px 0;
}

.round-full {
  border-radius: 45px 45px 45px 45px;
}

.w-90 {
  width: 90%;
}

.q-item:hover {
  border-radius: 0 45px 45px 0 !important;
  /* width: 90%; */
}
</style>
