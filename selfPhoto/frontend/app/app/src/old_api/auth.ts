import { api } from 'boot/axios';

/**
 * Get a user's JWT access token
 */
export const getAccessToken = async (args: iLogin): Promise<iAccessToken | null> => {
  const params = new URLSearchParams(args);
  let accessToken: iAccessToken | null = null;
  try {
    const { data } = await api.post('/login/access-token', params);
    accessToken = data;
  } catch (error) {
    // if (api.isAxiosError(error)) {
    //   handleAxiosError(error);
    // } else {
    //   handleUnexpectedError(error);
    // }
    console.log(error);
  }
  return accessToken;
};
