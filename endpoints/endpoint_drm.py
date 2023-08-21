from base_client import BaseClient

class DRM(BaseClient):

    def __init__(self, base_url, instance, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.instance = instance
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def list_labels(self, vendor="mip", display_output=False):
        """
        Fetches and returns the list of labels from the DRM SaaS vendor.
        """
        endpoint = f"drm/config/{vendor}/{self.instance}/listlabels/"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)
