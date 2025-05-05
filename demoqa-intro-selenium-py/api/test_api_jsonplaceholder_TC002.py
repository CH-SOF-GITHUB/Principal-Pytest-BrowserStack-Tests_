import json

from requests import api

"""
send request api with post
"""


# Method to return response of api
def return_json(response):
    observables = response.json()
    # convert to string
    r = json.dumps(observables)
    # convert to dic
    loaded_r = json.loads(r)
    return loaded_r


# Data to be sent
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}


def test_api_post_request():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # Post request to the api
    response = api.post(url=url, json=data)

    # assert the status code of response == 201
    assert response.status_code == 201
    print("\n******* api status code *******")
    print(response.status_code)

    # return the expected response of the api
    expected_response = return_json(response)
    print("\n******* return response api data to send *******")
    print(expected_response)

    # get request to the api
    get_response = api.get(url="https://jsonplaceholder.typicode.com/posts")
    print("\n******* return response api data [] *******")
    print(return_json(get_response))
