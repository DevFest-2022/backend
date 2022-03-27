import twitter
from user import User

def _fetch_likes(user_id: str, max_results: int) -> list[dict]:
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
    

def _fetch_user_with_handle(handle: str) -> User:
    api_endpoint = f"2/users/by/username/{handle}"
    query_params = {
        'user.fields': {
            "id,username,name,description,profile_image_url,verified"
        }
    }
    response = twitter.query(api_endpoint, query_params)
    return User.from_json(response["data"])


def _fetch_user_with_id(user_id: str) -> User:
    api_endpoint = f"2/users/{user_id}"
    query_params = {
        'user.fields': {
            "id,username,name,description,profile_image_url,verified"
        }
    }
    response = twitter.query(api_endpoint, query_params)
    return User.from_json(response["data"])


def favorite_users(handle: str, max_processed_tweets: int, max_results: int) -> dict:
    user = _fetch_user_with_handle(handle)
    liked_tweets = _fetch_likes(user_id=user.id, max_results=max_processed_tweets)
    ranked_users = _rank_most_liked_users(liked_tweets=liked_tweets)

    results = []
    for i in range(0, max_results):
        if i >= len(ranked_users):
            return
        
        favorite_user = _fetch_user_with_id(ranked_users[i])
        results.append(favorite_user.export_json())

    return {
        'user': user.export_json(), 
        'results': results
    }

def fetch_high_res_pfp(url):
    newurl = url.replace("_normal", "", 1)
    return newurl