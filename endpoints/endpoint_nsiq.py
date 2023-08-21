from base_client import BaseClient

class Nsiq(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def ioc_info(self, hash_value, display_output=False):
        """
        Get single sample information.
        """
        endpoint = f"nsiq/retrohunt/ioc/info?hash={hash_value}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def batch_ioc_info(self, hash_list, display_output=False):
        """
        Get sample information in batch.
        """
        endpoint = "nsiq/retrohunt/ioc/getinfo"
        response = self.post(endpoint, data=hash_list, display_output=display_output)
        return self._handle_response(response)

    def ioc_report(self, hash_value, display_output=False):
        """
        Get sample report.
        """
        endpoint = f"nsiq/retrohunt/ioc/report?hash={hash_value}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_recategorizations(self, display_output=False):
        """
        List the re-categorization requests.
        """
        endpoint = "nsiq/url/recategorizations"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def post_recategorizations(self, data, display_output=False):
        endpoint = "nsiq/url/recategorizations"
        """
        Submit url re-categorization requests.
        """
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def get_recategorization(self, id_value, display_output=False):
        """
        Get the re-categorization request details by id.
        """
        endpoint = f"nsiq/url/recategorizations/{id_value}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_recategorization_url(self, id_value, url_id, display_output=False):
        """
        Get the status of the url under a re-categorization request by id.
        """
        endpoint = f"nsiq/url/recategorizations/{id_value}/urls/{url_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)
