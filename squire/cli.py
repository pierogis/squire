import os

import click
import openai

from squire import gpt3


def set_openai_key():
    """
    look for openai key in env (perhaps set by .env file)

    if not found, prompt the user
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if openai_api_key is None:
        openai_api_key = input("openai api key:")

    openai.api_key = openai_api_key


@click.group()
def app():
    pass


@app.command()
@click.option('--prompt', default=None)
@click.option('--temperature', default=0.8, help='creativity scale')
def ramble(prompt: str, temperature: float):
    if prompt is None:
        prompt = click.prompt('prompt', type=str, default='')

    set_openai_key()

    spiel: str = gpt3.ramble(prompt, temperature=temperature)

    print()
    print("spiel:\n")
    print(prompt + " " + spiel)


@app.command()
@click.option('--artist', default=None)
@click.option('--temperature', default=0.8, help='creativity scale')
def lyrics(artist: str, temperature: float):
    if artist is None:
        artist = click.prompt('artist', type=str)

    set_openai_key()

    generated_lyrics = gpt3.generate_lyrics(artist, temperature=temperature)

    print()
    print("lyrics:\n")
    print(generated_lyrics)


@app.command()
@click.option('--username', default=None)
@click.option('--temperature', default=0.8, help='creativity scale')
def tweet(username: str, temperature: float):
    try:
        from squire import twitter

        if username is None:
            username = click.prompt('username', type=str)

        twitter_bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
        if twitter_bearer_token is None:
            twitter_bearer_token = input("twitter bearer token:")

        client = twitter.create_client(twitter_bearer_token)

        set_openai_key()

        generated_tweets = gpt3.generate_tweet(client, username, temperature=temperature)

        print()
        print("tweets:\n")
        print(generated_tweets)

    except ImportError as e:
        print("tweepy package not installed: run `pip install squire[twitter]`")


@app.command()
@click.option('--temperature', default=0.8, help='creativity scale')
def discord_bot(temperature: float):
    try:
        from squire import discord

        client = discord.create_client(temperature)

        discord_token = os.environ.get("DISCORD_BOT_TOKEN")

        if discord_token is None:
            discord_token = input("discord token:")

        client.run(discord_token)

    except ImportError as e:
        print("discord.py package not installed: run `pip install squire[discord]`")
