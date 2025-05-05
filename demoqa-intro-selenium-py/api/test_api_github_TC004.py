import json
import os

from dotenv import load_dotenv, find_dotenv
from requests import get

"""
test github api with get request
"""


def return_json(response):
    observables = response.json()
    # convert json to string
    r = json.dumps(observables)
    # parse it to dict
    loaded_r = json.loads(r)
    return loaded_r


load_dotenv(find_dotenv())

def test_github_get_request_octocat():
    # The Api endpoint
    url = "https://api.github.com/octocat"

    # get request to the api
    token = os.environ.get("GITHUB_TOKEN")

    response = get(url=url, headers={
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    })

    with open('dict.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(response.text)

    # assert the response status code
    assert response.status_code == 200
    print("\n******* api status code *******")
    print(response.status_code)

    # return a message for the final results
    print("\ntest api github octocat ok")