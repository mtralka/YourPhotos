<script setup lang="ts">
import { ref } from 'vue';
import AccountCard from 'src/components/mainLayout/AccountCard.vue';
import UploadCard from 'src/components/mainLayout/UploadCard.vue';
import LeftMenuDrawer from 'src/components/mainLayout/LeftMenuDrawer.vue';
import { useQuasar } from 'quasar';

const $q = useQuasar();

const showAccountDialog = ref(false);

const computerUpload = ref(null);
const leftDrawerOpen = ref(false);
const leftDrawerMiniState = ref(true);

const search = ref('');
const storage = ref(0.26);
function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

const leftDrawerClick = (e) => {
  if (leftDrawerMiniState.value) {
    leftDrawerMiniState.value = false;
  }
  e.stopPropagation();
};
</script>

<template>
  <q-layout view="hHh lpR fFf" class="bg-grey-1">
    <q-header class="bg-white text-grey-8" height-hint="64">
      <q-toolbar class="GPL__toolbar" style="height: 64px">
        <q-btn
          v-if="!$q.screen.gt.xs"
          flat
          dense
          round
          @click="toggleLeftDrawer"
          aria-label="Menu"
          icon="menu"
          class="q-mr-md"
        />

        <q-toolbar-title
          v-if="$q.screen.gt.sm"
          shrink
          class="row items-center no-wrap"
        >
          <!-- <img
            src="https://cdn.quasar.dev/img/layout-gallery/logo-google.svg"
          /> -->
          <span class="q-ml-sm">
            <!-- <span style="text-shadow: 2px 1px 0 #1db980; color: #a732fc"
              >Y</span
            >
            <span style="text-shadow: 2px 1px 0 #1db980; color: #a732fc"
              >o</span
            >
            <span style="text-shadow: 2px 1px 0 #1db980; color: #a732fc"
              >u</span
            >
            <span style="text-shadow: 2px 1px 0 #1db980; color: #a732fc"
              >r</span
            > -->Your Photos</span
          >
        </q-toolbar-title>

        <q-space />

        <!-- 
            ######
            ## Search
            #####
           -->
        <q-input
          class="GPL__toolbar-input"
          dense
          hide-bottom-space
          standout="bg-grey-5"
          v-model="search"
          :placeholder="$t('search')"
        >
          <template v-slot:prepend>
            <q-icon v-if="search === ''" name="search" />
            <q-icon
              v-else
              name="clear"
              class="cursor-pointer"
              @click="search = ''"
            />
          </template>
        </q-input>

        <q-space v-if="$q.screen.gt.xs" />

        <div class="q-gutter-sm row items-center no-wrap">
          <!-- 
            ######
            ## Upload Card
            #####
           -->
          <q-btn
            v-if="$q.screen.gt.xs"
            flat
            dense
            round
            no-wrap
            color="gray"
            icon="upload"
            no-caps
            :label="$q.screen.gt.sm ? 'Upload' : ''"
            class="q-ml-sm q-px-md"
          >
            <q-tooltip>{{ $t('upload') }}</q-tooltip>
            <q-menu
              class="q-pb-lg q-px-md q-pt-md"
              style="min-width: 300px"
              anchor="top right"
              self="top right"
            >
              <upload-card />
            </q-menu>
          </q-btn>

          <!-- 
            ######
            ## Help
            #####
           -->
          <q-btn
            v-if="$q.screen.gt.xs"
            round
            dense
            flat
            color="text-grey-7"
            icon="help_outline"
            class="q-ml-sm q-px-md"
            ><q-tooltip>{{ $t('help') }}</q-tooltip>
          </q-btn>

          <!-- 
            ######
            ## Settings Card
            #####
           -->
          <q-btn
            v-if="$q.screen.gt.xs"
            round
            dense
            flat
            color="text-grey-7"
            icon="settings"
            class="q-ml-sm q-px-md"
            ><q-tooltip>{{ $t('settings') }}</q-tooltip>
          </q-btn>

          <q-space v-if="$q.screen.gt.xs" />
          <!-- <q-btn round dense flat color="text-grey-7" icon="apps">
            <q-tooltip>{{$t('dashboard')}}</q-tooltip>
          </q-btn> -->
          <!-- <q-btn round dense flat color="grey-8" icon="notifications">
            <q-badge color="red" text-color="white" floating> 2 </q-badge>
            <q-tooltip>Notifications</q-tooltip>
          </q-btn> -->

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
        </div>
      </q-toolbar>
      <q-separator />
    </q-header>
    <q-drawer
      v-model="leftDrawerOpen"
      @mouseover="leftDrawerMiniState = false"
      @mouseout="leftDrawerMiniState = true"
      :mini="$q.screen.gt.sm ? false : leftDrawerMiniState"
      :breakpoint="599"
      :mini-to-overlay="$q.screen.gt.sm ? false : true"
      :mini-width="70"
      :width="250"
      show-if-above
      no-swipe-close
      no-swipe-open
    >
      <!-- :class="[leftDrawerMiniState ? 'q-pr-none' : 'q-pr-md']" -->
      <left-menu-drawer />
    </q-drawer>

    <q-page-container class="GPL__page-container">
      <router-view class="q-mt-lg" />

      <!-- <q-page-sticky v-if="$q.screen.gt.sm" expand position="left">
        <div class="fit q-pt-xl q-px-sm column">
          <q-btn
            round
            flat
            color="grey-8"
            stack
            no-caps
            size="26px"
            class="GPL__side-btn"
          >
            <q-icon size="22px" name="photo" />
            <div class="GPL__side-btn__label">Photos</div>
          </q-btn>

          <q-btn
            round
            flat
            color="grey-8"
            stack
            no-caps
            size="26px"
            class="GPL__side-btn"
          >
            <q-icon size="22px" name="collections_bookmark" />
            <div class="GPL__side-btn__label">Albums</div>
          </q-btn>

          <q-btn
            round
            flat
            color="grey-8"
            stack
            no-caps
            size="26px"
            class="GPL__side-btn"
          >
            <q-icon size="22px" name="assistant" />
            <div class="GPL__side-btn__label">Assistant</div>
            <q-badge
              floating
              color="red"
              text-color="white"
              style="top: 8px; right: 16px"
            >
              1
            </q-badge>
          </q-btn>

          <q-btn
            round
            flat
            color="grey-8"
            stack
            no-caps
            size="26px"
            class="GPL__side-btn"
          >
            <q-icon size="22px" name="group" />
            <div class="GPL__side-btn__label">Sharing</div>
          </q-btn>

          <q-btn
            round
            flat
            color="grey-8"
            stack
            no-caps
            size="26px"
            class="GPL__side-btn"
          >
            <q-icon size="22px" name="import_contacts" />
            <div class="GPL__side-btn__label">Photo books</div>
          </q-btn>
        </div>
      </q-page-sticky> -->
    </q-page-container>
  </q-layout>
</template>

<style lang="sass">
.GPL
  &__toolbar
    height: 64px
  &__toolbar-input
    width: 50%
  &__drawer-item
    line-height: 24px
    border-radius: 0 24px 24px 0
    margin-right: 12px
    .q-item__section--avatar
      padding-left: 12px
      .q-icon
        color: #5f6368
    .q-item__label:not(.q-item__label--caption)
      color: #3c4043
      letter-spacing: .01785714em
      font-size: .875rem
      font-weight: 500
      line-height: 1.25rem
    &--storage
      border-radius: 0
      margin-right: 0
      padding-top: 24px
      padding-bottom: 24px
  &__side-btn
    &__label
      font-size: 12px
      line-height: 24px
      letter-spacing: .01785714em
      font-weight: 500
  @media (min-width: 1024px)
    &__page-container
      padding-left: 94px
  @media (max-width: 1024px)
    &__toolbar-input
      width: 55%
</style>
