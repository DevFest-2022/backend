import requests

def _auth() -> str: 
    return "AAAAAAAAAAAAAAAAAAAAAAQyawEAAAAApXudbijx8skU%2FTV65uzC0zPZgS8%3DkEjaeYoDHNeEzHgQQCZLD8B6sf3gKuJeHjHIIAzc3x6l5qyKE9"

def _create_headers(bearer_token: str) -> dict[str : str]:
    return {"Authorization": "Bearer {}".format(bearer_token)}

def _create_url(api_endpoint: str) -> str:
    return f"https://api.twitter.com/{api_endpoint}"

def query(api_endpoint: str, query_params: dict):
    bearer_token = _auth()
    headers = _create_headers(bearer_token)
    url = _create_url(api_endpoint)
    response = requests.request("GET", url, headers = headers, params = query_params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()