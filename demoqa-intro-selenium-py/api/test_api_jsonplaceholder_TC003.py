import json

from requests import api

"""
send request post with params
"""

# Method to return response of api
def return_json(response):
    observables = response.json()
    # convert to string
    r = json.dumps(observables)
    # convert to dic
    loaded_r = json.loads(r)
    return loaded_r


def test_get_api_request_params():
    # the Api of the endpoint
    url = "https://jsonplaceholder.typicode.com/posts/"

    # adding a pyload
    payload = {"id": [1, 2, 3], "userId": 1}
    # get request to the api
    response = api.get(url=url, params=payload)

    # assert the status code the api
    assert response.status_code == 200
    print("\n******* api status code *******")
    print(response.status_code)

    # return the expected response of the api
    expected_response = return_json(response)
    print("\n******* return response api data to send *******")
    print(expected_response)

    # loop through the response with params
    print("\n******* return response api data by id *******")
    i = 0
    while i < len(expected_response):
        print(f"response {i + 1} :\n{expected_response[i]}")
        i += 1
