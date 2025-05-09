import http.client
import json

import requests


def returnJson(response):
    r = response.json()
    j = json.dumps(r)
    data = json.loads(j)
    return data


def test_api_demoqa_login():
    # The Api Endpoint
    url = "https://demoqa.com/Account/v1/Login"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "userName": "ch_demoqa",
        "password": "Admin1234!"
    }
    # Send Post request with BasicHttpRequest
    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()
        print("\nresponse status code: ", response.status_code)
        print("\nresponse data: ", returnJson(response))
    except Exception as e:
        print(f"\n\n error is {str(e)}")


def test__http_client_login():
    # The Api endpoint
    url = "https://demoqa.com"
    try:
        connection = http.client.HTTPSConnection("demoqa.com")
        headers = {"Content-Type": "application/json"}
        data = {
            "userName": "ch_demoqa",
            "password": "Admin1234!"
        }
        json_data = json.dumps(data)
        connection.request('POST', '/Account/v1/Login', json_data, headers)
        response = connection.getresponse()
        print(f"\n\n Connection status code: {response.getcode()}")
        print(f"\n\n Connection response: {response.read().decode()}")
    except Exception as e:
        print(f"\n error is {str(e)}")
