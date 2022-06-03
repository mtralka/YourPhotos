/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Asset } from '../models/Asset';
import type { Body_assets_create_assets } from '../models/Body_assets_create_assets';
import type { Exif } from '../models/Exif';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AssetsService {

    /**
     * Create Assets
     * Create new assets
     * @returns Asset Successful Response
     * @throws ApiError
     */
    public static createAssets({
        formData,
    }: {
        formData: Body_assets_create_assets,
    }): CancelablePromise<Array<Asset>> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/assets',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Paginated Assets
     * Return multiple assets controled by skip and limit
     * @returns Asset Successful Response
     * @throws ApiError
     */
    public static getPaginatedAssets({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<Array<Asset>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/assets',
            query: {
                'skip': skip,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Asset By Id
     * Return an asset by ID
     * @returns Asset Successful Response
     * @throws ApiError
     */
    public static getAssetById({
        id,
    }: {
        id: string,
    }): CancelablePromise<Asset> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/assets/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Media
     * Return an asset's media
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getMedia({
        id,
    }: {
        id: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/assets/{id}/media',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Thumbnail
     * Return an asset's thumbnail
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getThumbnail({
        id,
    }: {
        id: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/assets/{id}/thumbnail',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Exif
     * Return an asset's exif data
     * @returns Exif Successful Response
     * @throws ApiError
     */
    public static getExif({
        id,
    }: {
        id: string,
    }): CancelablePromise<Exif> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/assets/{id}/exif',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
