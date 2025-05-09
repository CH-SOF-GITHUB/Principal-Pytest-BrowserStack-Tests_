import http.client
import json


def test_http_client_books():
    # The Api endpoint
    url = "demoqa.com"

    # add a connection http client
    connection = http.client.HTTPSConnection(url)

    # declare headers, json data
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImNoX2RlbW9xYSIsInBhc3N3b3JkIjoiQWRtaW4xMjM0ISIsImlhdCI6MTc0NjgxMTM0Mn0.MVE9dmo6gn-8dqvb_ERXe_XmAB-Nd_gtHb3eGu4MlUw"
    }
    json_data = {
        "userId": "02d3c08a-ed76-4ead-9c7f-c9b25abd5b65",
        "collectionOfIsbns": [
            {
                "isbn": "9781491950296"
            }
        ]
    }
    data = json.dumps(json_data)
    connection.request("POST", url="/BookStore/v1/Books", body=data, headers=headers)

    # print the response status code and response body
    HTTPResponse = connection.getresponse()
    print("\n add_books status code: ", HTTPResponse.getcode())
    print("\n add_books response body: " + HTTPResponse.read().decode())
