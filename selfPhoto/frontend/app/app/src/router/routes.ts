import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  // {
  //   path: '/',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [{ path: '', component: () => import('pages/IndexPage.vue') }],
  // },
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/IndexPage.vue') }],
  },
  {
    path: '/a/:id',
    component: () => import('layouts/OnlyFooter.vue'),
    children: [{ path: '', component: () => import('pages/AlbumPage.vue') }],
  },
  {
    path: '/albums',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/AlbumsPage.vue') }],
  },
  {
    path: '/explore',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/ExplorePage.vue') }],
  },
  {
    path: '/share',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/SharingPage.vue') }],
  },
  {
    path: '/favorites',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/FavoritesPage.vue') },
    ],
  },
  {
    path: '/m/:id',
    component: () => import('pages/AssetPage.vue'),
  },
  {
    path: '/login',
    component: () => import('layouts/OnlyFooter.vue'),
    children: [
      { path: '', component: () => import('src/pages/LoginPage.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
