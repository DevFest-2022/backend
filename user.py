from collections import namedtuple

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
    
    def export_json(self) -> dict:
        return {
            "name": self.name,
            "handle": self.handle,
            "bio": self.bio,
            "photo_url": self.photo_url
        }