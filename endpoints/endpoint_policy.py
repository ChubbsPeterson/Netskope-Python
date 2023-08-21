from base_client import BaseClient

class Policy(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_domain_fronting_exception_by_id(self, id, display_output=False):
        """
        Get Domain Fronting exceptions by ID.
        """
        endpoint = f"policy/domainfrontings/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_domain_fronting_exception(self, id, data, display_output=False):
        """
        Update Domain Fronting exceptions.
        """
        endpoint = f"policy/domainfrontings/{id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_domain_fronting_exception_by_id(self, id, display_output=False):
        """
        Delete Domain Fronting exception configuration by ID.
        """
        endpoint = f"policy/domainfrontings/{id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_domain_fronting_exceptions(self, display_output=False):
        """
        Get Domain Fronting exceptions.
        """
        endpoint = "policy/domainfrontings"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_domain_fronting_exception(self, data, display_output=False):
        """
        Create Domain Fronting Exception.
        """
        endpoint = "policy/domainfrontings"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)
    
    def get_npa_policies(self, display_output=False):
        """
        Get list of npa policies.
        """
        endpoint = "policy/npa/rules"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_npa_policy(self, data, display_output=False):
        """
        Create a npa policy.
        """
        endpoint = "policy/npa/rules"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_npa_policy(self, id, display_output=False):
        """
        Delete a npa policy.
        """
        endpoint = f"policy/npa/rules/{id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def patch_npa_policy(self, id, data, display_output=False):
        """
        Patch a npa policy.
        """
        endpoint = f"policy/npa/rules/{id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_npa_policy(self, id, display_output=False):
        """
        Get a npa policy.
        """
        endpoint = f"policy/npa/rules/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    # ... Continuing with the rest of the endpoints ...

    def get_all_url_lists(self, display_output=False):
        """
        Get all applied and pending URL lists.
        """
        endpoint = "policy/urllist"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_url_list(self, data, display_output=False):
        """
        Create a new URL list.
        """
        endpoint = "policy/urllist"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def upload_url_list_config(self, file_path, display_output=False):
        """
        Upload multiple configurations via a JSON file.
        """
        endpoint = "policy/urllist/file"
        with open(file_path, 'rb') as file:
            response = self.post(endpoint, files={"file": file}, display_output=display_output)
        return self._handle_response(response)

    def get_url_list_by_id(self, id, display_output=False):
        """
        Get URL list by ID.
        """
        endpoint = f"policy/urllist/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def replace_url_list(self, id, data, display_output=False):
        """
        Replace a URL list configuration.
        """
        endpoint = f"policy/urllist/{id}"
        response = self.put(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_url_list(self, id, display_output=False):
        """
        Delete a URL list.
        """
        endpoint = f"policy/urllist/{id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def patch_url_list(self, id, action, data=None, display_output=False):
        """
        Patch URL list.
        """
        endpoint = f"policy/urllist/{id}/{action}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def apply_pending_url_changes(self, display_output=False):
        """
        Apply pending URL list changes.
        """
        endpoint = "policy/urllist/deploy"
        response = self.post(endpoint, display_output=display_output)
        return self._handle_response(response)