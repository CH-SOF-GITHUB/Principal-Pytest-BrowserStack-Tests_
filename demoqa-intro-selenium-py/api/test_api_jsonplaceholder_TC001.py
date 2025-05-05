import json

from requests import api

"""
Making Get and Post requests using Python language and Python requests Module
"""


def return_json(response):
    observables = response.json()
    # convert json to string
    r = json.dumps(observables)
    # parse it to dict
    loaded_r = json.loads(r)
    return loaded_r


# 1. GET request
def test_api_get_request():
    # The API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # A Get request to the api
    response = api.get(url)

    # verify the status code of the api
    assert response.status_code == 200

    # return the response json
    expected_response = return_json(response)

    # return the type of object and the value of response object
    print("\nType of expected_response:", type(expected_response))
    print(f"\n********* dict of response json : {expected_response} *********")

    # print the first value of response
    res = None
    for k in expected_response.values():
        res = k
        break

    print(f"\nvalue N°1 = {res}")

    # assert the expected value of response
    assert expected_response["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

    # return the message for the final result of test
    print("\ntest get request of api ok")