import json
import twitter

from collections import Counter

def process_likes(json_data):
    dictionary = {}
    for data in json_data:
        if dictionary.get(data["author_id"]) == None:
            dictionary.update({data["author_id"]: 1})
        else:
            x = dictionary.pop(data["author_id"])
            dictionary.update({data["author_id"]: x+1})

    sorted_dict = dict(sorted(dictionary.items(),
                           key=lambda item: item[1],
                           reverse=True))

    return sorted_dict
    

def id_to_handle(idnum):
    api_endpoint = "2/users/"+str(idnum)
    query_params = {
        'user.fields': {
            "username,name,description,profile_image_url,verified"
        }
    }
    json_response = twitter.query(api_endpoint, query_params)
    return json_response

def handle_to_id(handle):
    api_endpoint = "2/users/by/username/"+handle
    query_params = {
        'user.fields': {
            "id,name,description,profile_image_url,verified"
        }
    }
    json_response = twitter.query(api_endpoint, query_params)
    return json_response

def finalfunction(username):
    id = (handle_to_id(username)["data"]).get("id")
    api_endpoint = "2/users/"+str(id)+"/liked_tweets"
    query_params =  {
        'max_results':  100,
        'tweet.fields': {"author_id"},
        'next_token': {}
    }
    json_response = twitter.query(api_endpoint, query_params)
    dictionary = process_likes(json_response["data"])

    array = []
    counter = 0
    for x in dictionary:
        if(counter==5):
            break
        response = id_to_handle(x)
        temp = {}
        temp.update({"Name": response["data"].get('name')})
        temp.update({"Handle": response["data"].get('username')})
        temp.update({"Photo": response["data"].get('profile_image_url')})
        temp.update({"Bio": response["data"].get('description')})
        array.append(temp)
        counter+=1

    return array
    


if __name__ == "__main__":
    test = finalfunction("ronithhh")
    print(test)