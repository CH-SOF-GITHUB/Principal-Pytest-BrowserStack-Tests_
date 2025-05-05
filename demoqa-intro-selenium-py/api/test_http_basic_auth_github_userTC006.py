"""
HTTPBasicAuth GitHub that requires authentication, such as retrieving public and private information
about users and generate HTTP request exceptions
"""
import os

import requests
from dotenv import load_dotenv, find_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv(find_dotenv())

def test_http_basic_auth_github_user():
    # The Api endpoint
    private_url = "https://api.github.com/userr"

    # declare github_username and token
    github_username = "CH-SOF-GITHUB"
    github_token = os.environ.get("GITHUB_TOKEN")

    # Handling HTTP errors request
    try:
        auth_http_basic = HTTPBasicAuth(github_username, github_token)
        print("\nauth_http_basic:\n", auth_http_basic)
        private_url_response = requests.get(url=private_url, auth=auth_http_basic)

        # assert the status code of response api
        private_url_response.raise_for_status()
        assert private_url_response.status_code == 200
        print("\n******* api status code *******")
        print(private_url_response.status_code)

        # return the response data of api
        print(f"\nHTTPBasicAuth GitHub response:\n{private_url_response.json()}")
        print("\nHTTPBasicAuth GitHub Username and GitHub Token are OK")
    except Exception as e:
        print(str(e))