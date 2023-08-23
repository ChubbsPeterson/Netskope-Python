import json
import requests
from requests.exceptions import RequestException

EMOJI_RED = "🔴"

class BaseClient:

    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url
        self.headers = headers if headers else {}
        self.timeout = timeout
        self.session = requests.Session()

    def _url(self, endpoint):
        """
        Form the full URL for a given endpoint.
        """
        return f"{self.base_url}/{endpoint}"

    def _handle_response(self, response):
        """
        Helper function to handle response and errors.
        """
        if response and isinstance(response, dict):
            if 'error' not in response:
                if 'status' in response and response['status'] == 'error':
                    print(f"{EMOJI_RED}  Error in response. JSON: {response}")
                    return response
                else:
                    return response
        return {'message': "Unexpected response format or error occurred.", 'status': 'error'}


    def _request(self, method, endpoint, headers=None, **kwargs):
        """
        Unified request method.
        :param method: HTTP verb like GET, POST, etc.
        :param endpoint: API endpoint to call.
        :param kwargs: Additional arguments passed to requests.session.request.
        :return: JSON response or None in case of errors.
        """
        try:
            display_output = kwargs.pop('display_output', False)

            headers = headers or self.headers

            response = self.session.request(method, self._url(endpoint), headers=headers, **kwargs)
            response.raise_for_status()
            json_response = response.json()

            if 'application/json' in response.headers.get('Content-Type', ''):
                json_response = response.json()

                if display_output:
                    print(json.dumps(json_response, indent=4))

                return json_response
            else:
                return {'message': "Response is not in JSON format.", 'status': 'error'}

        except RequestException as e:
            print(f"{EMOJI_RED}  Error on {method.upper()} request: {e}")
            return None

    def get(self, endpoint, params=None, headers=None, display_output=False):
        return self._request('GET', endpoint, headers=headers, params=params, display_output=display_output)

    def post(self, endpoint, data=None, headers=None, files=None, display_output=False):
        return self._request('POST', endpoint, headers=headers, json=data, files=files, display_output=display_output)

    def put(self, endpoint, data=None, headers=None, display_output=False):
        return self._request('PUT', endpoint, headers=headers, json=data, display_output=display_output)

    def delete(self, endpoint, display_output=False):
        return self._request('DELETE', endpoint, display_output=display_output)

    def patch(self, endpoint, data=None, headers=None, display_output=False):
        return self._request('PATCH', endpoint, headers=headers, json=data, display_output=display_output)
