import { defineStore } from 'pinia';
import { getAssetById, getAssets as getAssetsAPI } from 'src/api/assets';
import { iAsset, iGetAssets } from 'src/api/models';
import { useUserStore } from './userStore';

export interface assetState {
  assetBatchSize: number;
  currentAssetIndex: number | undefined;
  // currentAsset: iAsset | undefined;
  assets: Array<iAsset>;
}

export const useAssetStore = defineStore('assetStore', {
  state: () =>
    ({
      assetBatchSize: 20,
      currentAssetIndex: undefined,
      // currentAsset: undefined,
      assets: [],
    } as assetState),
  getters: {
    getAssets(state): Array<iAsset> | Array<null> {
      return state.assets;
    },
    getCurrentAsset(state): iAsset | undefined {
      // return state.currentAsset;
      const asset: iAsset | undefined = state.assets.at(
        state.currentAssetIndex
      );

      // if (asset === undefined){
      //   return undefined
      // }
      // return asset
      return asset;
    },
    getCurrentAssetIndex(state): number | undefined {
      return state.currentAssetIndex;
    },
  },
  actions: {
    /*
      loadAllAssets
    */
    async loadAssets(args: iGetAssets): Promise<void> {
      const user = useUserStore();

      if (!user.accessToken) {
        console.log('NO ACCESS TOKEN');
        return;
      }

      const assets: Array<iAsset> | null = await getAssetsAPI({
        limit: this.assetBatchSize,
        ...args,
      });

      console.log(assets, "assets loaded in store")

      if (!assets) return;

      this.assets = this.assets.concat(assets);
    },
    async refreshAssets(): Promise<void> {
      this.clearAssets();
      this.loadAssets({});
    },
    async setCurrentAssetById(id: number): Promise<void> {
      // if (!this.getAssets){
      //   return
      // }
      // console.log(this.getAssets)
      // const assetIndex = this.getAssets.findIndex(e => e.id == id)
      // console.log("fond indx", assetIndex)
      // if (assetIndex === -1) {
      //   console.log("None found")
      //   return
      // }
      console.log('loading asset from API');
      const asset: iAsset | null = await getAssetById({ id: id });

      if (!asset) {
        // redirect to 404
        return;
      }

      this.assets = [asset];
      // this.currentAsset = asset
      this.currentAssetIndex = 0;
    },
    // iterate asset
    async incrementAsset(step: number): Promise<iAsset | undefined> {
      const newIndex = this.getCurrentAssetIndex
        ? this.getCurrentAssetIndex + step
        : 0 + step;

      if (newIndex < 0) {
        return undefined;
      }

      if (newIndex > this.getAssets.length) {
        return undefined;
      }

      this.currentAssetIndex = newIndex;

      return this.getCurrentAsset;
    },
    async setSequentialAsset(step: number): Promise<void> {
      if (this.getCurrentAssetIndex === undefined) {
        console.log('No index, finding');
        // return;
        this.currentAssetIndex = 0;
      }

      const newIndex = this.getCurrentAssetIndex + step;

      if (newIndex < 0) {
        return;
      }

      const newAsset: iAsset | undefined = this.assets.at(newIndex);

      if (newAsset === undefined) {
        return;
      }

      this.currentAssetIndex = newIndex;
      // this.currentAsset = newAsset;

      // console.log(this.getCurrentAssetIndex, this.getCurrentAsset);
    },
    calculatePaginationIndex(index: number): number {
      return index * this.assetBatchSize + this.assetBatchSize;
    },
    clearAssets() {
      this.assets = [];
    },
  },
});
