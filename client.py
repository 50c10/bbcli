import requests
from config import WORKSPACE

class BitbucketClient:
    def __init__(self, base_url="https://api.bitbucket.org/2.0", token=None):
        self.base_url = base_url
        self.session = requests.Session()
        
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        else:
            raise ValueError("You need a valid token to autenticate.")

    def create_project(self, project_name, description, project_key):
        """Create a project."""
        url = f"{self.base_url}/workspaces/{WORKSPACE}/projects"
        payload = {
                "key": project_key,
                "name": project_name,
                "description": description
            }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()


    def create_repository(self, project, repo_name, is_private=True):
        """Create a repository in a given Project."""
        url = f"{self.base_url}/repositories/{WORKSPACE}/{repo_name}"
        payload = {
            "project": {"key": project},
            "is_private": is_private
            }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()
