/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Asset } from './Asset';

export type User = {
    email?: string;
    isActive?: boolean;
    isSuperuser?: boolean;
    fullName?: string;
    id?: string;
    assets?: Array<Asset>;
};

