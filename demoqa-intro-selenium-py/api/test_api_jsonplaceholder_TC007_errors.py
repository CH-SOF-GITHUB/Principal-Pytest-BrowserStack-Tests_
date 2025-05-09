import requests


def test_handling_http_error():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/postz"
    try:
        # Attempt to Get Data from provided endpoint
        response = requests.get(url=url)
        # method to return an HTTPError object when an error occurs during the process
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"\n\nHttp error: {str(e)}")


def test_handling_error_too_many_redirects():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url=url)
        response.raise_for_status()
    except requests.exceptions.TooManyRedirects as e:
        print(f"\n\n error is: {str(e)}")


def test_request_session_1():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        session = requests.Session()
        session.max_redirects = 3
        response = session.get(url=url)
        response.raise_for_status()
    except requests.exceptions.TooManyRedirects as e:
        print(f"\n\n error is: {str(e)}")


def test_request_session_2():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        session = requests.Session()
        session.allow_redirects = False
        response = session.get(url=url)
    except requests.exceptions.TooManyRedirects as e:
        print(f"\n\n error is: {str(e)}")


def test_request_error_connection():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url=url)
    except requests.exceptions.ConnectionError as e:
        print(f"\n\n error is: {str(e)}")


def test_request_http_timeout():
    # The Api endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url=url, timeout=0.0001)
    except requests.exceptions.Timeout as e:
        print(f"\n\n error is: {str(e)}")


