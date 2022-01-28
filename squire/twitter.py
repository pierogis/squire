import os

import tweepy


def create_client(twitter_bearer_token: str) -> tweepy.Client:
    """
    look for twitter bearer token in env (perhaps set by .env file)

    if not found, prompt the user
    """

    return tweepy.Client(twitter_bearer_token)
