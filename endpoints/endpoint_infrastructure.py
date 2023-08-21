from base_client import BaseClient

class Infrastructure(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_publishers(self, display_output=False):
        """
        Get list of publisher objects.
        """
        endpoint = "infrastructure/publishers"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_publisher(self, data, display_output=False):
        """
        Create a publisher.
        """
        endpoint = "infrastructure/publishers"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_publisher(self, publisher_id, display_output=False):
        """
        Delete a publisher.
        """
        endpoint = f"infrastructure/publishers/{publisher_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_publisher(self, publisher_id, data, display_output=False):
        """
        Update a publisher.
        """
        endpoint = f"infrastructure/publishers/{publisher_id}"
        response = self.put(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def patch_publisher(self, publisher_id, data, display_output=False):
        """
        Patch a publisher.
        """
        endpoint = f"infrastructure/publishers/{publisher_id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_publisher(self, publisher_id, display_output=False):
        """
        Get a publisher.
        """
        endpoint = f"infrastructure/publishers/{publisher_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def generate_publisher_registration_token(self, publisher_id, display_output=False):
        """
        Generate and retrieve a token for publisher registration.
        """
        endpoint = f"infrastructure/publishers/{publisher_id}/registration_token"
        response = self.post(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_publisher_upgrade_profiles(self, display_output=False):
        """
        Get list of publisher upgrade profile objects.
        """
        endpoint = "infrastructure/publisherupgradeprofiles"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_publisher_upgrade_profile(self, data, display_output=False):
        """
        Create a publisher upgrade profile.
        """
        endpoint = "infrastructure/publisherupgradeprofiles"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_publisher_upgrade_profile(self, upgrade_profile_id, display_output=False):
        """
        Delete a publisher.
        """
        endpoint = f"infrastructure/publisherupgradeprofiles/{upgrade_profile_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_publisher_upgrade_profile(self, upgrade_profile_id, data, display_output=False):
        """
        Update a publisher upgrade profile.
        """
        endpoint = f"infrastructure/publisherupgradeprofiles/{upgrade_profile_id}"
        response = self.put(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_publisher_upgrade_profile(self, upgrade_profile_id, display_output=False):
        """
        Get a publisher upgrade profile.
        """
        endpoint = f"infrastructure/publisherupgradeprofiles/{upgrade_profile_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)