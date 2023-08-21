from base_client import BaseClient

class Incidents(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def get_anomaly(self, anomalyId, display_output=False):
        """
        Get the anomaly by anomalyId.
        """
        endpoint = f"incidents/anomalies/{anomalyId}"
        response = self.get(endpoint, display_output=display_output)
        return self._handle_response(response)

    def allow_anomaly(self, anomalyId, display_output=False):
        """
        It is a generic API to mark anomaly as allowed. For UCI Impact, it will revert the impact ingestion.
        """
        endpoint = f"incidents/anomalies/{anomalyId}/allow"
        response = self.post(endpoint, display_output=display_output) 
        return self._handle_response(response)

    def get_anomalies(self, data, display_output=False):
        """
        Get a list of anomalies. It will return anomalies within 90 days.
        """
        endpoint = "incidents/anomalies/getanomalies"
        params = {'activity': 'ActivityForUciImpactAPI'}
        response = self.post(endpoint, params=params, data=data, display_output=display_output) 
        return self._handle_response(response)

    def get_uci(self, display_output=False):
        """
        Get a list of users confidence index.
        """
        endpoint = "incidents/uba/getuci"
        response = self.post(endpoint, display_output=display_output)
        return self._handle_response(response)

    def user_uci_impact(self, data_payload, display_output=False):
        """
        Trigger the uci compute process after receiving uci impact request.
        """
        endpoint = "incidents/user/uciimpact"
        response = self.post(endpoint, json=data_payload, display_output=display_output)
        return self._handle_response(response)
