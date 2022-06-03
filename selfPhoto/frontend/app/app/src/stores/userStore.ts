import { defineStore } from 'pinia';
import { Asset, AuthService, Body_auth_login_access_token, CancelablePromise, OpenAPI, Token } from 'src/api';
import { useAssetStore } from './assetStore';
export interface userState {
  accessToken: Token | null;
  assets: Array<Asset> | Array<null>;
}

export const useUserStore = defineStore('userStore', {
  state: () =>
    ({
      accessToken: null,
      assets: [],
    } as userState),
  getters: {
    getAccessToken(state): Token | null {
      return state.accessToken;
    },
    getJWT(state): string | null {
      return state.accessToken?.accessToken || null;
    },
    getAssets(state): Array<Asset> | Array<null> {
      return state.assets;
    },
  },
  actions: {
    async login(args: Body_auth_login_access_token) : Promise<boolean> {
      const accessToken: CancelablePromise<Token> = await AuthService.loginAccessToken({formData: args})
      if (!accessToken) {
        console.log('no access token');
        return false;
      }
      console.log(accessToken.accessToken)

      this.accessToken = accessToken;
      OpenAPI.TOKEN = accessToken.accessToken

      const assetStore = useAssetStore()
      assetStore.loadAssets({})

      return true
    },
    async passwordReset(email: string) {
      return;
    },
    clearAssets() {
      this.assets = [];
    },
  },
});
