from base_client import BaseClient

class Steering(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_gre_pops(self, display_output=False):
        """
        Get GRE points of presence(POPs) list
        """
        endpoint = "steering/gre/pops"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_gre_pop(self, id, display_output=False):
        """
        Get GRE point of presence(POP)
        """
        endpoint = f"steering/gre/pops/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_gre_tunnels(self, display_output=False):
        """
        Get GRE tunnels list
        """
        endpoint = "steering/gre/tunnels"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)


    def create_gre_tunnel(self, data, display_output=False):
        """
        Create GRE tunnel
        """
        endpoint = "steering/gre/tunnels"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def get_gre_tunnel(self, id, display_output=False):
        """
        Get GRE tunnel
        """
        endpoint = f"steering/gre/tunnels/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_gre_tunnel(self, id, data, display_output=False):
        """
        Update GRE tunnel
        """
        endpoint = f"steering/gre/tunnels/{id}"
        response = self.patch(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def delete_gre_tunnel(self, id, display_output=False):
        """
        Delete GRE tunnel
        """
        endpoint = f"steering/gre/tunnels/{id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_ipsec_pops(self, display_output=False):
        """
        Get IPSec points of presence(POPs) list
        """
        endpoint = "steering/ipsec/pops"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_ipsec_pop(self, id, display_output=False):
        """
        Get GRE point of presence(POP)
        """
        endpoint = f"steering/ipsec/pops/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_ipsec_tunnels(self, display_output=False):
        """
        Get IPSec tunnel
        """
        endpoint = f"steering/ipsec/tunnels"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_ipsec_tunnel(self, data, display_output=False):
        """
        Create IPSec tunnel
        """
        endpoint = "steering/ipsec/tunnels"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def get_ipsec_tunnel(self, id, display_output=False):
        """
        Get IPSec tunnel
        """
        endpoint = f"steering/ipsec/tunnels/{id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_ipsec_tunnel(self, id, data, display_output=False):
        """
        Update IPSec tunnel
        """
        endpoint = f"steering/ipsec/tunnels/{id}"
        response = self.patch(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def delete_ipsec_tunnel(self, id, display_output=False):
        """
        Delete IPSec tunnel
        """
        endpoint = f"steering/ipsec/tunnels/{id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_private_apps(self, display_output=False):
        """
        Get list of private applications
        """
        endpoint = "steering/apps/private"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_private_app(self, data, display_output=False):
        """
        Create a private application
        """
        endpoint = "steering/apps/private"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def delete_private_app(self, private_app_id, display_output=False):
        """
        Delete a private application
        """
        endpoint = f"steering/apps/private/{private_app_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_private_app(self, private_app_id, data, display_output=False):
        """
        Update a private application
        """
        endpoint = f"steering/apps/private/{private_app_id}"
        response = self.put(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def patch_private_app(self, private_app_id, data, display_output=False):
        """
        Patch a private application
        """
        endpoint = f"steering/apps/private/{private_app_id}"
        response = self.patch(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def get_private_app(self, private_app_id, display_output=False):
        """
        Get a private application
        """
        endpoint = f"steering/apps/private/{private_app_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)
    
    def retrieve_policy_in_use_for_private_apps(self, data, display_output=False):
        """
        Retrieve number of policy in use for specified private apps
        """
        endpoint = "steering/apps/private/getpolicyinuse"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def create_tags_for_private_apps(self, data, display_output=False):
        """
        create tags for private apps
        """
        endpoint = "steering/apps/private/tags"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def bulk_update_tags_for_private_apps(self, data, display_output=False):
        """
        bulk update tags to associate with specified private apps
        """
        endpoint = "steering/apps/private/tags"
        response = self.patch(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def bulk_delete_tags_for_private_apps(self, data, display_output=False):
        """
        bulk delete tags for specified private apps
        """
        endpoint = "steering/apps/private/tags"
        response = self.delete(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def get_list_of_private_app_tags(self, display_output=False):
        """
        Get list of private app tags
        """
        endpoint = "steering/apps/private/tags"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_private_app_tag(self, tag_id, display_output=False):
        """
        Get a private app tag based on tag id
        """
        endpoint = f"steering/apps/private/tags/{tag_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_private_app_tag_based_on_id(self, tag_id, data, display_output=False):
        """
        Update a private app tag based on tag id
        """
        endpoint = f"steering/apps/private/tags/{tag_id}"
        response = self.put(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)

    def delete_private_app_tag_based_on_id(self, tag_id, display_output=False):
        """
        Delete a private app tag based on tag id
        """
        endpoint = f"steering/apps/private/tags/{tag_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def retrieve_policy_in_use_for_tags(self, data, display_output=False):
        """
        Retrieve number of policy in use for specified tags
        """
        endpoint = "steering/apps/private/tags/getpolicyinuse"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)