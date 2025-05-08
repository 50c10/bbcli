from enum import Enum
import typer
from client import BitbucketClient

class PermissionLevel(str, Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"

app = typer.Typer(help="CLI to interact with bitbucket api.")

# Client global instance
client = BitbucketClient()

@app.command()
def create_project( project_name: str, description: str, project_key: str):
    """Create a project."""
    client.set_credentials()
    typer.echo(f"Creating project '{project_name}'")
    response = client.create_project(project_name, description, project_key)
    print(response)

@app.command()
def create_repo(project: str, repo_name: str, private: bool = True):
    """Create a repository in a given Project."""
    client.set_credentials()
    typer.echo(f"Creating repo '{repo_name}' on: {project}")
    response = client.create_repository(project, repo_name, is_private=private)
    print(response)

@app.command()
def add_user(user_id: str,repo_name: str, permission: PermissionLevel):
    """
    Add permissions to a user on a repository.
    user_id need be Account ID (ej: 557058:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
    """
    client.set_credentials(use_password=True)
    typer.echo(f"Changing permisions for '{user_id}' on: {repo_name}")
    response = client.add_user(user_id,repo_name, permission)
    print(response)

@app.command()
def remove_user(user_id: str, repo_name: str):
    """
    Remove permissions of user on a repository.
    user_id need be Account ID (ej: 557058:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
    """
    client.set_credentials(use_password=True)
    typer.echo(f"Removing user '{user_id}' from: {repo_name}")
    response = client.remove_user(user_id,repo_name)
    print(response)

@app.command()
def permissions(user_id: str, repo_name: str):
    """
    This function add permission to push without a PR
    """
    client.set_credentials(use_password=True)
    typer.echo(f"Adding permissions to '{user_id}' on: {repo_name}")
    response = client.update_permissions(user_id,repo_name)
    print(response)
