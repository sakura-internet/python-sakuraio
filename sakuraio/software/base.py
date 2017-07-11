import requests
from sakuraio.software.apis import APIMixins


class SakuraIOClient(APIMixins):
    base_url = 'https://api.sakura.io/v1/'
    api_token = None
    api_secret = None

    def __init__(self, api_token, api_secret, base_url=None):
        if api_token is None or api_secret is None:
            Exception('[ERROR] must set api_token and api_secret')

        self.api_token = api_token
        self.api_secret = api_secret

        if base_url is not None:
            self.base_url = base_url

    def do(self, method, path, url_params={}, query_params={}, request_params={}):
        """Request wrapper

        :param string method:
            HTTP Mehod. ``GET`` or ``POST``.

        :param string path:
            Path of URL.

        :return: API response (format JSON)
        """
        headers = {}
        headers["Accept"] = 'application/json'
        auth = (self.api_token, self.api_secret)
        _url = self.base_url + path

        method = method.lower()
        response = None
        if method == 'get':
            response = requests.get(
                _url,
                params=query_params,
                headers=headers,
                auth=auth
                )
        elif method == 'post':
            response = requests.post(
                _url,
                params=query_params,
                data=request_params,
                headers=headers,
                auth=auth
                )
        else:
            raise Exception('[ERROR] Unsupported Method')

        return response.json()

    def auth(self):
        """Test authentication
        """
        return self.do('GET', 'auth')
