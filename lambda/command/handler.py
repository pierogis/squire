import os
from typing import Dict, List, Callable, Optional

import openai
import requests

from squire import gpt3

openai.api_key = os.environ.get("OPENAI_API_KEY")


def handle_lyrics_command(options: List[Dict[str, any]]) -> str:
    artist = None
    temperature = None
    for option in options:
        option_name = option.get('name')
        option_value = option.get('value')

        if option_name == 'artist':
            artist = option_value

        elif option_name == 'artistic_license':
            temperature = option_value

    if artist is not None:
        if temperature is not None:
            generated_lyrics = gpt3.generate_lyrics(artist, temperature)
        else:
            generated_lyrics = gpt3.generate_lyrics(artist)
    else:
        raise Exception("No artist option provided")

    return generated_lyrics


def handle_ramble_command(options: Optional[List[Dict[str, any]]]) -> str:
    prompt = ''
    temperature = None
    if options is not None:
        for option in options:
            option_name = option.get('name')
            option_value = option.get('value')

            if option_name == 'prompt':
                prompt = option_value

            elif option_name == 'artistic_license':
                temperature = option_value

    if temperature is not None:
        spiel = gpt3.ramble(prompt, temperature)
    else:
        spiel = gpt3.ramble(prompt)

    if prompt is not None:
        return "{} {}".format(prompt, spiel)
    else:
        return spiel


SLASH_COMMAND_HANDLERS: Dict[str, Callable[[List[Dict[str, any]]], str]] = {
    'lyrics': handle_lyrics_command,
    'ramble': handle_ramble_command,
}


def command(event, context):
    interaction_token = event['interaction_token']
    application_id = event['application_id']
    command_data = event['command_data']

    command_name = command_data.get('name')
    options: List[Dict[str, any]] = command_data.get('options')

    if command_name in SLASH_COMMAND_HANDLERS:
        response_message = SLASH_COMMAND_HANDLERS[command_name](options)

    else:
        raise Exception(f"Slash command '{command_name}' not found")

    if not isinstance(response_message, str):
        raise Exception(f"Response message '{response_message}' is not a string")

    url = f"https://discord.com/api/v8/webhooks/{application_id}/{interaction_token}"

    response_json = {
        "tts": False,
        "content": response_message,
        "embeds": [],
        "allowed_mentions": []
    }

    requests.post(url, json=response_json)
