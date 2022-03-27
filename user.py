from collections import namedtuple
import json

class User:
    def __init__(self, id: str, name: str, 
                handle: str, bio: str, 
                photo_url: str, is_verified: bool):
        self.id = id
        self.name = name
        self.handle = handle
        self.bio = bio
        self.photo_url = photo_url
        self.is_verified = is_verified
    
    @classmethod
    def from_json(user, json_data: dict):
        return user(
            id=_safely_get_str(json_data, key="id"), 
            name=_safely_get_str(json_data, key="name"), 
            handle=_safely_get_str(json_data, key="username"), 
            bio=_safely_get_str(json_data, key="description"), 
            photo_url=_safely_get_str(json_data, key="profile_image_url"), 
            is_verified=_safely_get_bool(json_data, key="verified"))

    
    def export_json(self) -> dict:
        return {
            "name": self.name,
            "handle": self.handle,
            "bio": self.bio,
            "photo_url": self.photo_url
        }

def _safely_get_str(json_data: dict, key: str) -> str:
    if key in json_data:
        return json_data[key]
    else:
        return ""

def _safely_get_bool(json_data: dict, key: str) -> bool:
    if key in json_data:
        return json_data[key]
    else:
        return False