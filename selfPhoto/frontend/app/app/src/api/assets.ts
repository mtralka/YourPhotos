import { api } from 'boot/axios';
import { iAsset, iGetAssetById, iGetAssets } from './models';

// create asset

/**
 * Get a user's assets
 */
export const getAssets = async (
  args: iGetAssets
): Promise<Array<iAsset> | null> => {
  const params = new URLSearchParams(args);
  let assets: Array<iAsset> | null = null;
  try {
    const { data } = await api.get('/assets', { params: params });
    assets = data;
  } catch (error) {
    // if (api.isAxiosError(error)) {
    //   handleAxiosError(error);
    // } else {
    //   handleUnexpectedError(error);
    // }
    console.log(error);
  }
  return assets;
};

/**
 * Get a asset by ID
 */
// TODO
export const getAssetById = async (
  args: iGetAssetById
): Promise<iAsset | null> => {
  let asset: iAsset | null = null;
  try {
    const { data } = await api.get(`/asset/${args.id}`);
    asset = data;
  } catch (error) {
    // if (api.isAxiosError(error)) {
    //   handleAxiosError(error);
    // } else {
    //   handleUnexpectedError(error);
    // }
    console.log(error);
  }
  return asset;
};

/**
 * Get a user's assets
 */
 export const uploadAssets = async (
  files: any
): Promise<Array<iAsset> | null> => {
 
  const formData = new FormData();

  files.forEach(file => {
    formData.append('assets', file)
  });

  let assets: Array<iAsset> | null = null;
  try {
    const { data } = await api.post('/assets/', formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      }
    });
    assets = data;
  } catch (error) {
    // if (api.isAxiosError(error)) {
    //   handleAxiosError(error);
    // } else {
    //   handleUnexpectedError(error);
    // }
    console.log(error);
  }
  return assets;
};