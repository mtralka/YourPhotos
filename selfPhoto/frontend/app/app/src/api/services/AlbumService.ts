/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Album } from '../models/Album';
import type { AlbumAsset } from '../models/AlbumAsset';
import type { AlbumCreate } from '../models/AlbumCreate';
import type { AlbumUpdate } from '../models/AlbumUpdate';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AlbumService {

    /**
     * Create Album
     * Create a new album
     * @returns Album Successful Response
     * @throws ApiError
     */
    public static createAlbum({
        requestBody,
    }: {
        requestBody: AlbumCreate,
    }): CancelablePromise<Album> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/albums/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get All Albums
     * Get all albums
     * @returns Album Successful Response
     * @throws ApiError
     */
    public static getAllAlbums(): CancelablePromise<Array<Album>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/albums/',
        });
    }

    /**
     * Delete Album
     * Delete an album
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteAlbum({
        id,
    }: {
        id: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/albums/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Album
     * Update an album.
     * @returns Album Successful Response
     * @throws ApiError
     */
    public static updateAlbum({
        id,
        requestBody,
    }: {
        id: string,
        requestBody: AlbumUpdate,
    }): CancelablePromise<Album> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/albums/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Album Info
     * Retrieve album info
     * @returns Album Successful Response
     * @throws ApiError
     */
    public static getAlbumInfo({
        id,
    }: {
        id: string,
    }): CancelablePromise<Album> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/albums/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Add Asset To Album
     * Add assets by UUID to album
     * @returns AlbumAsset Successful Response
     * @throws ApiError
     */
    public static addAssetToAlbum({
        id,
        requestBody,
    }: {
        id: string,
        requestBody: string,
    }): CancelablePromise<AlbumAsset> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/albums/{id}/assets',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Remove Asset
     * Add asset by UUID to album
     * @returns any Successful Response
     * @throws ApiError
     */
    public static removeAsset({
        id,
        assets,
    }: {
        id: string,
        /**
         * List of asset UUIDs you wish to remove from this album
         */
        assets: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/albums/{id}/assets',
            path: {
                'id': id,
            },
            query: {
                'assets': assets,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Album Assets
     * Retrieve album assets
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getAlbumAssets({
        id,
        skip,
        limit = 100,
    }: {
        id: string,
        /**
         * Number of assets to skip
         */
        skip?: number,
        /**
         * Maximum amount of assets to return
         */
        limit?: number,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/albums/{id}/assets',
            path: {
                'id': id,
            },
            query: {
                'skip': skip,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
