<script setup lang="ts"></script>

<template>
  <q-card
    class="fit column no-wrap justify-start items-center content-center q-pa-md"
    style="min-width: 300px"
  >
    <q-btn round style="overflow: hidden" type="image/png">
      <q-avatar rounded size="104px">
        <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
      </q-avatar>
    </q-btn>
    <q-card-section>
      <div class="text-h6 ellipsis">Matthew Tralka</div>
      <div class="text-grey text-caption">mtralka59@gmail.com</div>
    </q-card-section>
    <q-card-actions
      vertical
      align="center"
      class="q-px-none full-width q-pb-md"
    >
      <q-btn
        outline
        rounded
        color="white"
        text-color="black"
        padding="xs md"
        class="q-mb-sm"
      >
        Manage your Account
      </q-btn>
      <!-- <q-separator  class="full-width" /> -->
      <q-btn outline color="white" text-color="grey" padding="xs md">
        Sign out
      </q-btn>
    </q-card-actions>
    <q-separator class="full-width" />
    <q-card-section
      class="q-pa-none row items-center full-width justify-center"
    >
      <q-btn
        round
        dense
        flat
        color="text-grey-7"
        icon="device_hub"
        class="q-ml-sm q-px-sm"
        ><q-tooltip>Github</q-tooltip>
      </q-btn>
      <p>MIT</p>
    </q-card-section>
  </q-card>
</template>
