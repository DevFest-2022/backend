import twitter

def _find_likes(user_id: str, max_results: int) -> list[dict]:
    api_endpoint = f"2/users/{user_id}/liked_tweets"
    query_params =  {
        'max_results':  max_results,
        'tweet.fields': {"author_id"}
    }
    return twitter.query(api_endpoint, query_params)["data"]


def _rank_most_liked_users(liked_tweets: list[dict]) -> list[str]:
    user_like_counts = {}
    for tweet in liked_tweets:
        author_id = tweet["author_id"]
        if author_id in user_like_counts:
            user_like_counts[author_id] += 1
        else:
            user_like_counts[author_id] = 1
    
    sorted_user_like_counts = sorted(
        user_like_counts.items(), 
        key=lambda item: item[1], 
        reverse=True)

    return [item[0] for item in sorted_user_like_counts]
    


def _find_user_with_id(user_id: str) -> dict:
    api_endpoint = f"2/users/{user_id}"
    query_params = {
        'user.fields': {
            "username,name,description,profile_image_url,verified"
        }
    }
    return twitter.query(api_endpoint, query_params)

def _find_user_with_handle(handle: str):
    api_endpoint = f"2/users/by/username/{handle}"
    query_params = {
        'user.fields': {
            "id,name,description,profile_image_url,verified"
        }
    }
    json_response = twitter.query(api_endpoint, query_params)
    return json_response

def finalfunction(username):
    searched_user = _find_user_with_handle(username)["data"]
    print(searched_user)
    id = searched_user["id"]
    liked_tweets = _find_likes(user_id=id, max_results=5)
    ranked_users = _rank_most_liked_users(liked_tweets=liked_tweets)

    array = []
    counter = 0
    for x in ranked_users:
        if(counter==5):
            break
        response = _find_user_with_id(x)
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