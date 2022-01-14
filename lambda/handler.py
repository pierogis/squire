import os
from enum import Enum

import openai
from nacl.signing import VerifyKey

import squire

openai.api_key = os.environ.get("OPENAI_API_KEY")
discord_token = os.environ.get("DISCORD_TOKEN")
discord_public_key = os.environ.get("DISCORD_PUBLIC_KEY")


class ResponseType(Enum):
    pong = 1
    ack_no_source = 2
    message_no_source = 3
    message_with_source = 4
    ack_with_source = 5


def _verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event['params']['header'].get('x-signature-ed25519')
    auth_ts = event['params']['header'].get('x-signature-timestamp')

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(discord_public_key))
    verify_key.verify(message, bytes.fromhex(auth_sig))


def interaction(event, context):
    print(f"event: {event}")

    _verify_signature(event)

    body = event.get('body-json')
    if ResponseType(body.get("type")) == ResponseType.pong:
        return {
            "type": ResponseType.pong.value,
        }
    else:
        return {
            "type": ResponseType.message_no_source.value,
            "data": {
                "tts": False,
                "content": body.get("data").get('content'),
                "embeds": [],
                "allowed_mentions": []
            }
        }
