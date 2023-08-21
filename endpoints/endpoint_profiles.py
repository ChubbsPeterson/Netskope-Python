from base_client import BaseClient

class Profiles(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_profile(self, profile_id, display_output=False):
        """
        Get single list resource by ID.
        """
        endpoint = f"profiles/lists/{profile_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_profile(self, profile_id, data_payload, display_output=False):
        """
        Partial update on fields, given action will replace to values field.
        """
        endpoint = f"profiles/lists/{profile_id}"
        response = self.patch(endpoint, json=data_payload, display_output=display_output)
        return self._handle_response(response)

    def delete_profile(self, profile_id, display_output=False):
        """
        Delete single list by ID
        """
        endpoint = f"profiles/lists/{profile_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_all_profiles(self, display_output=False):
        """
        Return all list objects, recommended to restrict the fields returned with &fields=id,name,description.
        """
        endpoint = "profiles/lists"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_profile(self, data_payload, display_output=False):
        """
        Create single list resource. Required attributes: Name, Type, and Values. Current list types supported: Domains - List objects which include only domain values and optional comment.
        """
        endpoint = "profiles/lists"
        response = self.post(endpoint, json=data_payload, display_output=display_output)
        return self._handle_response(response)
