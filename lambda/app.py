import os
from enum import Enum

import openai
from chalice import Chalice
from nacl.signing import VerifyKey

import squire

app = Chalice(app_name='squire')

openai.api_key = os.environ.get("OPENAI_API_KEY")
discord_token = os.environ.get("DISCORD_TOKEN")


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
    verify_key = VerifyKey(bytes.fromhex(discord_token))
    verify_key.verify(message, bytes.fromhex(auth_sig))


@app.route('/', methods=['POST'], cors=True)
def interaction(event, context):
    print(f"event {event}")

    _verify_signature(event)

    body = event.get('body-json')
    if body.get("type") == ResponseType.pong:
        return {
            "type": ResponseType.PONG,
        }
    else:
        return {
            "type": ResponseType.message_no_source,
            "data": {
                "tts": False,
                "content": body.get("data").get('content'),
                "embeds": [],
                "allowed_mentions": []
            }
        }
