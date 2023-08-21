from base_client import BaseClient

class Services(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_cci_app_info(self, display_output=False):
        """
        Get CCI related application information based on the apps/category/ccl/connector/discovered/domain/ids/tag.
        """
        endpoint = "services/cci/app"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_cci_domain(self, display_output=False):
        """
        Get the steering & discovery domains for the application/id.
        """
        endpoint = "services/cci/domain"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_cci_tags(self, display_output=False):
        """
        Get tags for the list of applications/ids.
        """
        endpoint = "services/cci/tags"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def get_bandwidth_control_traffic_class(self, class_id, display_output=False):
        """
        Get bandwidth control traffic class
        """
        endpoint = f"services/bandwidthcontrol/trafficclasses/{class_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_cci_tags(self, data, display_output=False):
        """
        Creates new tag and associate the same to the list of applications/ids.
        """
        endpoint = "services/cci/tags"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def add_cci_tags(self, tag, data, display_output=False):
        """
        Add existing tag to the list of applications/ids.
        """
        endpoint = f"services/cci/tags/{tag}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_pending_bandwidth_changes(self, display_output=False):
        """
        Get bandwidth control pending changes.
        """
        endpoint = "services/bandwidthcontrol/deploy"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def apply_bandwidth_changes(self, data, display_output=False):
        """
        Apply bandwidth control pending changes.
        """
        endpoint = "services/bandwidthcontrol/deploy"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def create_bandwidth_links(self, data, display_output=False):
        """
        Create bandwidth control links.
        """
        endpoint = "services/bandwidthcontrol/links"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_links(self, data, display_output=False):
        """
        Update bandwidth control links.
        """
        endpoint = "services/bandwidthcontrol/links"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    # ... and so on ...

    def get_bandwidth_control_link(self, link_id, display_output=False):
        """
        Get bandwidth control link.
        """
        endpoint = f"services/bandwidthcontrol/links/{link_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_link(self, link_id, data, display_output=False):
        """
        Update a bandwidth control link.
        """
        endpoint = f"services/bandwidthcontrol/links/{link_id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_bandwidth_control_link(self, link_id, display_output=False):
        """
        Delete a bandwidth control link.
        """
        endpoint = f"services/bandwidthcontrol/links/{link_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_bandwidth_control_policies(self, data, display_output=False):
        """
        Create bandwidth control policies.
        """
        endpoint = "services/bandwidthcontrol/policies"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_policies(self, data, display_output=False):
        """
        Update bandwidth control policies.
        """
        endpoint = "services/bandwidthcontrol/policies"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_bandwidth_control_policies(self, data, display_output=False):
        """
        Delete bandwidth control policies.
        """
        endpoint = "services/bandwidthcontrol/policies/deletepolicies"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def list_bandwidth_control_policies(self, data, display_output=False):
        """
        Get bandwidth control policies list.
        """
        endpoint = "services/bandwidthcontrol/policies/getpolicies"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_bandwidth_control_policy(self, policy_id, display_output=False):
        """
        Get bandwidth control policy.
        """
        endpoint = f"services/bandwidthcontrol/policies/{policy_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_policy(self, policy_id, data, display_output=False):
        """
        Update a bandwidth control policy.
        """
        endpoint = f"services/bandwidthcontrol/policies/{policy_id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_specific_bandwidth_control_policy(self, policy_id, display_output=False):
        """
        Delete bandwidth control policies.
        """
        endpoint = f"services/bandwidthcontrol/policies/{policy_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_bandwidth_control_trafficclasses(self, data, display_output=False):
        """
        Create bandwidth control trafficclasses.
        """
        endpoint = "services/bandwidthcontrol/trafficclasses"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_trafficclasses(self, data, display_output=False):
        """
        Update bandwidth control trafficclasses.
        """
        endpoint = "services/bandwidthcontrol/trafficclasses"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def list_bandwidth_control_trafficclasses(self, display_output=False):
        """
        Get bandwidth control trafficclasses list.
        """
        endpoint = "services/bandwidthcontrol/trafficclasses"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def delete_bandwidth_control_trafficclasses(self, data, display_output=False):
        """
        Delete bandwidth control trafficclasses.
        """
        endpoint = "services/bandwidthcontrol/trafficclasses/deleteclasses"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_bandwidth_control_traffic_class(self, class_id, display_output=False):
        """
        Get bandwidth control traffic class.
        """
        endpoint = f"services/bandwidthcontrol/trafficclasses/{class_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_trafficclass(self, class_id, data, display_output=False):
        """
        Update bandwidth control trafficclass.
        """
        endpoint = f"services/bandwidthcontrol/trafficclasses/{class_id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_bandwidth_control_trafficclass(self, class_id, display_output=False):
        """
        Delete bandwidth control traffic class.
        """
        endpoint = f"services/bandwidthcontrol/trafficclasses/{class_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)

    def create_bandwidth_control_traffic_class_rules(self, data, display_output=False):
        """
        Create bandwidth control traffic class rules.
        """
        endpoint = "services/bandwidthcontrol/trafficclassrules"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_traffic_class_rules(self, data, display_output=False):
        """
        Update bandwidth control traffic class rules.
        """
        endpoint = "services/bandwidthcontrol/trafficclassrules"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def list_bandwidth_control_traffic_class_rules(self, data, display_output=False):
        """
        Get bandwidth control traffic class rule list.
        """
        endpoint = "services/bandwidthcontrol/trafficclassrules/getrules"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_bandwidth_control_traffic_class_rules(self, data, display_output=False):
        """
        Delete bandwidth control traffic class rules.
        """
        endpoint = "services/bandwidthcontrol/trafficclassrules/deleterules"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def get_bandwidth_control_traffic_class_rule(self, rule_id, display_output=False):
        """
        Get bandwidth control traffic class rule.
        """
        endpoint = f"services/bandwidthcontrol/trafficclassrules/{rule_id}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def update_bandwidth_control_traffic_class_rule(self, rule_id, data, display_output=False):
        """
        Update a bandwidth control traffic class rule.
        """
        endpoint = f"services/bandwidthcontrol/trafficclassrules/{rule_id}"
        response = self.patch(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def delete_bandwidth_control_traffic_class_rule(self, rule_id, display_output=False):
        """
        Delete a bandwidth control traffic class rule.
        """
        endpoint = f"services/bandwidthcontrol/trafficclassrules/{rule_id}"
        response = self.delete(endpoint, display_output=display_output)
        return self._handle_response(response)
