/*
AUTH
*/
export interface iGetAccessToken {
  username: string;
  password: string;
  grantType?: string;
  scope?: string;
  clientId?: string;
  clientSecret?: string;
}

export interface iAccessToken {
  accessToken: string;
  tokenType: string;
}

/*
Asset
*/
export interface iAsset {
  id: number;
  assetPath: string;
  contentType: string;
  fileSize: number;
  userId: number;
  fileName: string;
  fileExtension: string;
  thumbnailPath?: string;
  createdAt: string;
  modifiedAt: string;
}

export interface iGetAssets {
  skip?: number;
  limit?: number;
}

export interface iGetAssetById {
  id: number;
}

export interface iValidationError {
  detail: Array<Error>;
}

export interface Error {
  loc: string;
  msg: string;
  type: string;
}
