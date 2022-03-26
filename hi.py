import json
import twitter

def process_likes(json_data):
    logged_likes = {}
    for data in json_data:
        print(data["author_id"])
    

if __name__ == "__main__":
    api_endpoint = "2/users/166747718/liked_tweets"
    query_params = {
        'max_results':  5,
        'tweet.fields': {"author_id"},
        'next_token': {}
    }
    json_response = twitter.query(api_endpoint, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))