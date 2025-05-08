import requests
from requests.auth import HTTPBasicAuth
from config import WORKSPACE, PASSWORD, USERNAME, TOKEN

class BitbucketClient:
    def __init__(self, base_url="https://api.bitbucket.org/2.0"):
        self.base_url = base_url
        self.session = requests.Session()

    def set_credentials(self, use_password=None):
        if use_password:
            self.session.auth=HTTPBasicAuth(USERNAME, PASSWORD)
        else:
            self.session.headers.update({"Authorization": f"Bearer {TOKEN}"})

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
        return "Done"


    def create_repository(self, project, repo_name, is_private=True):
        """Create a repository in a given Project."""
        url = f"{self.base_url}/repositories/{WORKSPACE}/{repo_name}"
        payload = {
            "project": {"key": project},
            "is_private": is_private
            }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return "Done"

    def add_user(self, user_id, repo_name, permission):
        """Add user permission to a repo"""
        url = f"{self.base_url}/repositories/{WORKSPACE}/{repo_name}/permissions-config/users/{user_id}"
        payload = {
            "permission": permission.value
        }
        print(self.session.headers)
        response = self.session.put(url, json=payload)
        response.raise_for_status()
        return "Done"

    def remove_user(self, user_id, repo_name):
        """Remove user permission to a repo"""
        url = f"{self.base_url}/repositories/{WORKSPACE}/{repo_name}/permissions-config/users/{user_id}"
        response = self.session.delete(url)
        response.raise_for_status()
        return "Done"

    def update_permissions(self, user_id, repo_name):
        """This function add permission to push without a PR"""
        url = f"{self.base_url}/repositories/{WORKSPACE}/{repo_name}/branch-restrictions"
        payload = {
            "kind": "push",
            "branch_match_kind": "glob",
            "pattern": "master",
            "users": [{"type": "user", "username": user_id}],
        }
        response = self.session.post(url,json=payload)
        response.raise_for_status()
        return response.json