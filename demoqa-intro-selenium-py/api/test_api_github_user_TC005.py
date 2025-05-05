"""
GitHub REST API that requires Authentication
"""
import os

from dotenv import load_dotenv, find_dotenv
from requests import get

load_dotenv(find_dotenv())

def test_api_github_user():
    # The Api endpoint
    github_username = "CH-SOF-GITHUB"
    auth_token = os.environ.get("GITHUB_TOKEN")
    url = f"https://api.github.com/users/{github_username}"

    # Get request to the api
    private_url_response = get(url=url, headers={
        "Authorization": f"Bearer {auth_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    })

    # assert the status code 200 of response
    assert private_url_response.status_code == 200

    # return the response data
    print(f"\nDefault personal github response:\n{private_url_response.json()}")
