import { defineStore } from 'pinia';

export enum eAlbumSortMethod {
  MostRecent = 'mostRecentPhoto',
  LastModified = 'lastModified',
  AlbumTitle = 'albumTitle',
}

export interface settingsStore {
  albumSortMethod: eAlbumSortMethod;
}

export const useSettingsStore = defineStore('settingsStore', {
  state: () =>
    ({
      albumSortMethod: eAlbumSortMethod.MostRecent,
    } as settingsStore),
  getters: {
    getAlbumSortMethod(state): eAlbumSortMethod {
      return state.albumSortMethod;
    },
  },
  actions: {},
});
