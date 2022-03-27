import twitter

def _find_likes(user_id: str, max_results: int):
    api_endpoint = f"2/users/{user_id}/liked_tweets"
    query_params =  {
        'max_results':  max_results,
        'tweet.fields': {"author_id"}
    }
    return twitter.query(api_endpoint, query_params)["data"]

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
    searched_user = (handle_to_id(username)["data"])
    id = searched_user.get("id")
    liked_tweets = _find_likes(user_id=id, max_results=5)
    dictionary = process_likes(liked_tweets)

    array = []
    counter = 0
    for x in dictionary:
        if(counter==5):
            break
        response = id_to_handle(x)
        temp = {}
        temp.update({"name": response["data"].get('name')})
        temp.update({"handle": response["data"].get('username')})
        temp.update({"photo": response["data"].get('profile_image_url')})
        temp.update({"bio": response["data"].get('description')})
        array.append(temp)
        counter+=1

    searched_user_formatted = {}
    searched_user_formatted["name"] = searched_user["name"]
    searched_user_formatted["handle"]= searched_user["username"]
    searched_user_formatted["photo"]= searched_user["profile_image_url"]
    searched_user_formatted["bio"] = searched_user["description"]
    return {'user': searched_user_formatted, 'results': array}
    


if __name__ == "__main__":
    test = finalfunction("ronithhh")
    print(test)