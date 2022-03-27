from concurrent.futures import process
from time import process_time
import twitter
import json

def find_timeline(user_id: int):
    api_endpoint = f"2/users/{user_id}/tweets"
    query_params = {
        'tweet.fields': {"referenced_tweets"},
        'expansions': {"referenced_tweets.author_id"}
    }
    json_response = twitter.query(api_endpoint, query_params)
    return json_response

def process_timeline(json_data):
    logged_tweets = {}
    print(json_data)
    for tweet in json_data:
        try:
            referenced_tweets = tweet["referenced_tweets"]
            print(referenced_tweets)
            for referenced_tweet in referenced_tweets:
                if referenced_tweet["author_id"] in logged_tweets:
                    logged_tweets["author_id"] += 1
                else:
                    logged_tweets["author_id"] = 1
        except:
            continue
    
    return logged_tweets

if __name__ == "__main__":
    json_response = find_timeline(166747718)
    processed_timeline = process_timeline(json_response["data"])
    print(json.dumps(processed_timeline, indent=4))