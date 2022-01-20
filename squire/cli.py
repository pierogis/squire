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
@click.option('--temperature', default=0.8, help='creativity scale')
def ramble(temperature: float):
    prompt: str = click.prompt('prompt', type=str, default='')

    set_openai_key()

    spiel: str = gpt3.ramble(prompt, temperature=temperature)

    print()
    print("spiel:\n")
    print(prompt + " " + spiel)


@app.command()
@click.option('--temperature', default=0.8, help='creativity scale')
def lyrics(temperature: float):
    artist = click.prompt('artist', type=str)

    set_openai_key()

    generated_lyrics = gpt3.generate_lyrics(artist, temperature=temperature)

    print()
    print("lyrics:\n")
    print(generated_lyrics)


@app.command()
@click.option('--temperature', default=0.8, help='creativity scale')
def discord_bot(temperature: float):
    try:
        from squire import bot

        client = bot.create_client(temperature)

        discord_token = os.environ.get("DISCORD_BOT_TOKEN")

        if discord_token is None:
            discord_token = input("discord token:")

        client.run(discord_token)

    except ImportError as e:
        print("discord.py package not installed: run `pip install squire[discord]`")
