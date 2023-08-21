from base_client import BaseClient

class Platform(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_all_roles(self, display_output=False):
        """
        Find all predefined roles.
        """
        endpoint = "platform/roles"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_role_by_id(self, role_id, display_output=False):
        """
        Predefined role by id.
        """
        endpoint = f"platform/roles/{role_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_all_v2_roles(self, display_output=False):
        """
        All predefined v2 roles.
        """
        endpoint = "platform/rolesv2"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_v2_role_by_id(self, role_id, display_output=False):
        """
        Get predefined v2 roles by id.
        """
        endpoint = f"platform/rolesv2/{role_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_all_custom_roles(self, display_output=False):
        """
        Get all custom roles.
        """
        endpoint = "platform/customroles"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_custom_role(self, data, display_output=False):
        """
        Create custom role.
        """
        endpoint = "platform/customroles"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def update_custom_role(self, data, display_output=False):
        """
        Update custom role.
        """
        endpoint = "platform/customroles"
        response = self.put(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_custom_role_by_id(self, role_id, display_output=False):
        """
        Get custom role by id.
        """
        endpoint = f"platform/customroles/{role_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def delete_custom_role_by_id(self, role_id, display_output=False):
        """
        Delete custom role by id.
        """
        endpoint = f"platform/customroles/{role_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_admin_domains(self, display_output=False):
        """
        Get a list of admin domains.
        """
        endpoint = "platform/adminaccessdomains"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_all_idp_accounts(self, display_output=False):
        """
        Get a list of all IDP accounts configured for SSO.
        """
        endpoint = "platform/ssoconfig/idpaccounts"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_idp_account(self, data, display_output=False):
        """
        Create a new IDP account for SSO.
        """
        endpoint = "platform/ssoconfig/idpaccounts"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def update_idp_account(self, id_value, data, display_output=False):
        """
        Partial update an existing IDP account for SSO.
        """
        endpoint = f"platform/ssoconfig/idpaccounts/{id_value}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_idp_account(self, id_value, display_output=False):
        """
        Delete an existing IDP account for SSO.
        """
        endpoint = f"platform/ssoconfig/idpaccounts/{id_value}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)
