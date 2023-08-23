from base_client import BaseClient

class UbaDataSvc(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def repeatable_demo(self, data, display_output=False):
        """
        Commands the repeatable demo app to populate the UEBA system with demo data and notfifications.
        """
        endpoint = "ubadatasvc/repeatableDemo"
        response = self.post(endpoint, json=data, display_output=display_output)
        return self._handle_response(response)

    def user_uci(self, data, display_output=False):
        """
        Get single user's confidence index.
        """
        endpoint = "ubadatasvc/user/uci"
        response = self.post(endpoint, data=data, display_output=display_output)
        return self._handle_response(response)
