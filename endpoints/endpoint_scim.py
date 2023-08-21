from base_client import BaseClient

class Scim(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def create_user(self, data, display_output=False):
        """
        Creation of a SCIM User.
        """
        endpoint = "scim/Users"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_users(self, display_output=False):
        """
        Get Scim Users.
        """
        endpoint = "scim/Users"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def replace_user(self, id_value, data, display_output=False):
        """
        Replace existing SCIM record for {id}.
        """
        endpoint = f"scim/Users/{id_value}"
        response = self.put(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_user(self, id_value, display_output=False):
        """
        Get the Scim User.
        """
        endpoint = f"scim/Users/{id_value}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_user(self, id_value, data, display_output=False):
        """
        Update existing SCIM User record by {id}.
        """
        endpoint = f"scim/Users/{id_value}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_user(self, id_value, display_output=False):
        """
        Delete SCIM User record by {id}.
        """
        endpoint = f"scim/Users/{id_value}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_group(self, data, display_output=False):
        """
        Create new SCIM Group.
        """
        endpoint = "scim/Groups"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_groups(self, display_output=False):
        """
        Get SCIM Groups.
        """
        endpoint = "scim/Groups"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def replace_group(self, id_value, data, display_output=False):
        """
        Replace existing SCIM Group for {id}.
        """
        endpoint = f"scim/Groups/{id_value}"
        response = self.put(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_group(self, id_value, display_output=False):
        """
        Get SCIM Group by {id}.
        """
        endpoint = f"scim/Groups/{id_value}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_group(self, id_value, data, display_output=False):
        """
        Update existing SCIM Group record by {id}.
        """
        endpoint = f"scim/Groups/{id_value}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_group(self, id_value, display_output=False):
        """
        Delete SCIM Group record by {id}.
        """
        endpoint = f"scim/Groups/{id_value}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)
