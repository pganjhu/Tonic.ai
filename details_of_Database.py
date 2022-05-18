"""
Created on Mon Feb  7 11:21:22 2022

@author: pawan
"""
import json
import requests

# Parameters
TONIC_API_KEY = "Hu8*****************************************************5iI1"
TONIC_URL = "http://xyz.abc.mno"
WORKSPACE_NAME = "Gen"

class TonicSession:
    def __init__(self, base_url, api_key):
        self._base_url = base_url
        self._session = requests.Session()
        self._api_key = api_key
        self._session.headers.update({"Authorization": "Apikey {}".format(api_key)})

    def _get_url(self, api_snippet):
        return "{}{}".format(self._base_url, api_snippet)

    def generate_data(self, workspace_id):
        generate_data_url = self._get_url("/api/generateData/start")
        params = {"workspaceId": workspace_id}
        r = self._session.post(generate_data_url, params=params)
        if r.ok:
            print("Data generation started")
        else:
            r.raise_for_status()

    def generate_data_status(self, workspace_id):
        generate_data_status_url = self._get_url("/api/generateData")
        params = {"workspaceId": workspace_id}
        r = self._session.get(generate_data_status_url, params=params)
        if r.ok:
            print(json.dumps(r.json(), indent=2))
        else:
            r.raise_for_status()

    def get_workspaces(self):
        workspace_list_url = self._get_url("/api/workspace")
        r = self._session.get(workspace_list_url)
        if r.ok:
            return r.json()
        else:
            r.raise_for_status()


def find_workspace_id(workspaces_json, workspace_name):
    for workspace in workspaces_json:
        if workspace["workspaceName"] == workspace_name:
            return workspace["id"]
    raise RuntimeError("No Workspace found with name: {}".format(workspace_name))


def main():
    session = TonicSession(TONIC_URL, TONIC_API_KEY)
    workspace_id = find_workspace_id(session.get_workspaces(), WORKSPACE_NAME)
    # Starts a new data generation    session.generate_data(workspace_id)
    # Prints out the current status of the workspace    session.generate_data_status(workspace_id)


if __name__ == "__main__":
    main()
