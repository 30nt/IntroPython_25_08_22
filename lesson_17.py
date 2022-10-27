import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

auth = OAuth1(API_KEY, API_SECRET)
endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
print(response.json())

# полиморфизм

value_1 = ["2", ]
value_2 = ["3", ]

result = value_1 + value_2
print(result)

class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __repr__(self):
        return f"(({self.x0}, {self.y0}), ({self.x1}, {self.y1}))"

    def __add__(self, other):
        x0 = min(self.x0, other.x0)
        y0 = min(self.y0, other.y0)
        x1 = max(self.x1, other.x1)
        y1 = max(self.y1, other.y1)
        return Bbox(x0, y0, x1, y1)


bbox_1 = Bbox(0, 2, 2, 3)
bbox_2 = Bbox(1, 1, 5, 7)

bbox_3 = bbox_1 + bbox_2

print(bbox_1, bbox_2, bbox_3)
