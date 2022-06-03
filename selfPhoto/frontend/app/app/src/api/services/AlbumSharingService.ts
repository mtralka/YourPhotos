/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AlbumUser } from '../models/AlbumUser';
import type { AlbumUserUpdate } from '../models/AlbumUserUpdate';
import type { Body_album_sharing_create_album_user_share } from '../models/Body_album_sharing_create_album_user_share';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AlbumSharingService {

    /**
     * Get All Album Shared Users
     * Get all shares for album
     * @returns AlbumUser Successful Response
     * @throws ApiError
     */
    public static getAllAlbumSharedUsers({
        id,
    }: {
        id: string,
    }): CancelablePromise<Array<AlbumUser>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/albums/{id}/shares',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Album User Share
     * Create a new album user share
     * @returns AlbumUser Successful Response
     * @throws ApiError
     */
    public static createAlbumUserShare({
        id,
        requestBody,
    }: {
        id: string,
        requestBody: Body_album_sharing_create_album_user_share,
    }): CancelablePromise<AlbumUser> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/albums/{id}/shares',
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
     * Delete Album User Share
     * Delete an existing album user share
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteAlbumUserShare({
        id,
        userId,
    }: {
        id: string,
        /**
         * User UUID for the user you wish to share this album with
         */
        userId: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/albums/{id}/shares',
            path: {
                'id': id,
            },
            query: {
                'userId': userId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Album User
     * Update an album user.
     * @returns AlbumUser Successful Response
     * @throws ApiError
     */
    public static updateAlbumUser({
        id,
        userId,
        requestBody,
    }: {
        id: string,
        /**
         * User UUID for the user you wish to edit share settings
         */
        userId: string,
        requestBody: AlbumUserUpdate,
    }): CancelablePromise<AlbumUser> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/albums/{id}/shares/{user_id}',
            path: {
                'id': id,
                'user_id': userId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
