import os
from enum import Enum
from typing import Dict, List, Callable, Optional

import openai
from nacl.signing import VerifyKey

from squire import gpt3

openai.api_key = os.environ.get("OPENAI_API_KEY")
discord_public_key = os.environ.get("DISCORD_PUBLIC_KEY")


class InteractionType(Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4


class InteractionCallbackType(Enum):
    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8


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


def _verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event['params']['header'].get('x-signature-ed25519')
    auth_ts = event['params']['header'].get('x-signature-timestamp')

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(discord_public_key))
    verify_key.verify(message, bytes.fromhex(auth_sig))


def interaction(event: Dict[str, any], context):
    """
    the actual lambda handler
    """
    _verify_signature(event)

    body = event.get('body-json')

    if InteractionType(body.get("type")) == InteractionType.PING:
        print("pong")
        return {
            "type": InteractionCallbackType.PONG.value,
        }
    else:
        request_data = body.get("data")

        command_name = request_data.get('name')
        options: List[Dict[str, any]] = request_data.get('options')

        if command_name in SLASH_COMMAND_HANDLERS:
            response_message = SLASH_COMMAND_HANDLERS[command_name](options)
            print(response_message)

        else:
            raise Exception(f"Slash command '{command_name}' not found")

        if not isinstance(response_message, str):
            raise Exception(f"Response message '{response_message}' is not a string")

        return {
            "type": InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE.value,
            "data": {
                "tts": False,
                "content": response_message,
                "embeds": [],
                "allowed_mentions": []
            }
        }
