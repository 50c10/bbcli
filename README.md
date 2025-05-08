# bbcli

This is a tool to interact with the Bitbucket API.

## Installation

### Requirements
- Python

### Install Packages

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### Create environment variables:
```bash
export BITBUCKET_TOKEN="access token"
export BITBUCKET_WORKSPACE="workspace"
export BITBUCKET_USERNAME="username"
export BITBUCKET_PASSWORD="password"
```

Note:
the bitbucket password is created following the next doc https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/

### Run the script

to use the tool just need to execute the next command. the cli will show all the options available

```bash
main.py --help
```