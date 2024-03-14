import os
import requests
import json

def get_random_cat(api_key):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data[0]['url']
    else:
        print("Failed to fetch cat image:", response.status_code)
        return None

# Example usage
cat_api_key = os.getenv("CAT_API_KEY")
if cat_api_key:
    cat_url = get_random_cat(cat_api_key)
    if cat_url:
        print("Here's your random cat image:", cat_url)
else:
    print("Please set the CAT_API_KEY environment variable.")