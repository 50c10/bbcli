import typer
from client import BitbucketClient
from config import TOKEN

app = typer.Typer(help="CLI to interact with bitbucket api.")

# Client global instance
client = BitbucketClient(token=TOKEN)

@app.command()
def create_project( project_name: str, description: str, project_key: str):
    """Create a project."""
    typer.echo(f"Creating project '{project_name}'")
    project = client.create_project(project_name, description, project_key)
    print(project)

@app.command()
def create_repo(project: str, repo_name: str, private: bool = True):
    """Create a repository in a given Project."""
    typer.echo(f"Creating repo '{repo_name}' on: {project}")
    repo = client.create_repository(project, repo_name, is_private=private)
    print(repo)
