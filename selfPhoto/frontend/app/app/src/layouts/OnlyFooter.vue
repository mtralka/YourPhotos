<script setup lang="ts"></script>

<template>
  <q-layout view="hHh lpR fFf">
    <!-- <q-header reveal bordered class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          Title
        </q-toolbar-title>
      </q-toolbar>
    </q-header> -->

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="bg-white text-black">
      <q-toolbar>
        <q-toolbar-title>
          <!-- <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar> -->
          <!-- <div>YourPhotos</div> -->

          <!-- List with lang selection, then on right help, privacy, terms -->
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>
