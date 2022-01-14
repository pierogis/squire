import os
from dotenv import load_dotenv
import click
import openai

import gpt3
import bot


@click.group()
def cli():
    pass


@cli.command()
@click.option('--temperature', default=0.8, help='creativity scale')
def ramble(temperature: float):
    prompt: str = click.prompt('prompt', type=str)
    spiel: str = gpt3.ramble(prompt, temperature=temperature)
    print()
    print("spiel:\n")
    print(prompt + " " + spiel.strip())


@cli.command()
@click.option('--temperature', default=0.8, help='creativity scale')
def lyrics(temperature: float):
    artist = click.prompt('artist', type=str)
    lyrics = gpt3.generate_lyrics(artist, temperature=temperature)
    print()
    print("lyrics:\n")
    print(lyrics.strip())


@cli.command()
@click.option('--temperature', default=0.8, help='creativity scale')
def discord_bot(temperature: float):
    client = bot.create_client(temperature)
    client.run(discord_token)


load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
discord_token = os.getenv("DISCORD_TOKEN")
cli()
