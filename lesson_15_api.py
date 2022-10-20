import requests

url = "http://api.forismatic.com/api/1.0/"

for key in range(10):
    params = {
        "method": "getQuote",
        "format": "json",
        "key": key,
        "lang": "en"
    }
    response = requests.get(url, params=params)
    print(response.json()["quoteText"])
