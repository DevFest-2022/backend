import json
import twitter

def process_likes(json_data):
    #dict = {}
    #for data in json_data:
    #    dict.update({data["author_id"]: 1})
    
    #ids = dict.keys()
    #print(ids)

    #for x in ids:
    #    length = len(dict.fromkeys(x, 1))

    ls = []
    for data in json_data:
        ls.append(data["author_id"])
    dictionary = Counter(ls)
    print(dictionary)

if __name__ == "__main__":
    api_endpoint = "2/users/166747718/liked_tweets"
    query_params = {
        'max_results':  5,
        'tweet.fields': {"author_id"},
        'next_token': {}
    }
    json_response = twitter.query(api_endpoint, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))