from base_client import BaseClient

class ATP(BaseClient):

    def __init__(self, base_url, auth_token, headers=None, timeout=10):
        super().__init__(base_url, headers, timeout)
        self.headers.update({
            'Netskope-Api-Token': auth_token,
            'accept': 'application/json'
        })

    def file_scan(self, file_path, file_type, display_output=False):
        """
        API to submit a file for scan by Netskope sandbox(supported file types: .exe, file size: up to 16MB, up to 1000 files per day).
        """
        endpoint = "atp/scans/filescan?scantype=sandbox"
        files = {'file': (file_path.split('/')[-1], open(file_path, 'rb'), file_type)}

        response = self.post(endpoint, headers=self.headers, files=files, display_output=display_output)
        return self._handle_response(response)

    def get_scan_report(self, jobid, display_output=False):
        """
        Get analysis report of a file submitted for scan by sandbox, Using jobid returned in filescan request (Up to 10,000 requests per day).
        """
        endpoint = f"atp/scans/reports/{jobid}"
        response = self.get(endpoint, headers=self.headers, display_output=display_output)
        return self._handle_response(response)
