import { defineStore } from 'pinia';
import { Asset, AssetsService, CancelablePromise } from 'src/api';
import { iPagination } from 'src/extraApiModels';
import { useUserStore } from './userStore';
export interface assetState {
  assetBatchSize: number;
  currentAssetIndex: number | undefined;
  // currentAsset: iAsset | undefined;
  assets: Array<Asset>;
}

export const useAssetStore = defineStore('assetStore', {
  state: () =>
    ({
      assetBatchSize: 50,
      currentAssetIndex: undefined,
      // currentAsset: undefined,
      assets: [],
    } as assetState),
  getters: {
    getAssets(state): Array<Asset> | Array<null> {
      return state.assets;
    },
    getCurrentAsset(state): Asset | undefined {
      // return state.currentAsset;
      const asset: Asset | undefined = state.assets.at(
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
    async loadAssets(args: iPagination): Promise<void> {
      const user = useUserStore();

      if (!user.accessToken) {
        console.log('NO ACCESS TOKEN');
        return;
      }

      const assets: CancelablePromise<Asset[]> = await AssetsService.getPaginatedAssets({limit: this.assetBatchSize, ...args})

      console.log("Loaded new assets", assets)
      
      if (!assets) return;

      this.assets = this.assets.concat(assets);
      console.log("New total assets", this.assets.length)
    },
    async refreshAssets(): Promise<void> {
      this.clearAssets();
      this.loadAssets({});
    },
    async setCurrentAssetById(id: string): Promise<void> {
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
      const asset: CancelablePromise<Asset> = AssetsService.getAssetById({id: id})

      if (!asset) {
        // redirect to 404
        return;
      }

      this.assets = [asset];
      // this.currentAsset = asset
      this.currentAssetIndex = 0;
    },
    // iterate asset
    async incrementAsset(step: number): Promise<Asset | undefined> {
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
      return (index - 1) * this.assetBatchSize + this.getAssets.length //  this.assetBatchSize;
    },
    clearAssets() {
      this.assets = [];
    },
  },
});
