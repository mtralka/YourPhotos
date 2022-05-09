import { api } from 'boot/axios';
import { defineStore } from 'pinia';
import { getAssets } from 'src/api/assets';
import { getAccessToken } from 'src/api/auth';
import {
  iAccessToken,
  iAsset, iGetAccessToken, iGetAssets
} from 'src/api/models';

export interface userState {
  accessToken: iAccessToken | null;
  assets: Array<iAsset>;
}

export const useUserStore = defineStore('userStore', {
  state: () =>
    ({
      accessToken: null,
      assets: [],
    } as userState),
  getters: {
    getAccessToken(state): iAccessToken | null {
      return state.accessToken;
    },
    getJWT(state): string | null {
      return state.accessToken?.accessToken || null;
    },
    getAssets(state): Array<iAsset> | Array<null> {
      return state.assets;
    },
  },
  actions: {
    async login(args: iGetAccessToken) : Promise<boolean> {
      console.log("ere")
      const accessToken: iAccessToken | null = await getAccessToken(args);
      if (!accessToken) {
        console.log('no access token');
        return false;
      }
      console.log(accessToken.accessToken)
      api.defaults.headers.common['Authorization'] =
        'Bearer ' + accessToken.accessToken;
      this.accessToken = accessToken;

      return true
    },
    async passwordReset(email: string) {
      return;
    },
    async loadAssets(args: iGetAssets) {
      if (!this.accessToken) {
        console.log('NO ACCESS TOKEN');
        return;
      }
      const assets: Array<iAsset> | null = await getAssets(args);
      console.log(assets);
      this.assets = this.assets.concat(assets);
      // this.assets = assets
    },
    clearAssets() {
      this.assets = [];
    },
  },
});
