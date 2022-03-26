import requests
import json

def auth() -> str: 
    return "AAAAAAAAAAAAAAAAAAAAAAQyawEAAAAApXudbijx8skU%2FTV65uzC0zPZgS8%3DkEjaeYoDHNeEzHgQQCZLD8B6sf3gKuJeHjHIIAzc3x6l5qyKE9"

def create_headers(bearer_token: str):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    search_url = "https://api.twitter.com/2/users/166747718/liked_tweets" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {
        'max_results':  max_results,
        'tweet.fields': {"author_id"},
        'next_token': {}
    }
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
    
def process_likes(json_data):
    logged_likes = {}
    for data in json_data:
        print(data["author_id"])
    

if __name__ == "__main__":
    bearer_token = auth()
    headers = create_headers(bearer_token)
    keyword = "xbox lang:en"
    start_time = "2021-03-01T00:00:00.000Z"
    end_time = "2021-03-31T00:00:00.000Z"
    max_results = 5
    
    url = create_url(keyword, start_time,end_time, max_results)
    json_response = connect_to_endpoint(url[0], headers, url[1])
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    process_likes(json_response["data"])