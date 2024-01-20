import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv()

def create_auth():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
        signature_type="auth_header"
    )
    return auth

def create_tweet(text: str) -> dict:
    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    auth = create_auth()
    return requests.post(url, json=data, auth=auth, headers=headers).json()

def delete_tweet(id: str) -> dict:
    url = f"https://api.twitter.com/2/tweets/{id}"
    headers = {
        "Content-Type": "application/json"
    }
    auth = create_auth()
    return requests.delete(url, auth=auth, headers=headers).json()