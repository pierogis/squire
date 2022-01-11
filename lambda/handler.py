
import os
import json

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

import squire

discord_token = os.environ.get("DISCORD_TOKEN")

RESPONSE_TYPES = {
    "PONG": 1,
    "ACK_NO_SOURCE": 2,
    "MESSAGE_NO_SOURCE": 3,
    "MESSAGE_WITH_SOURCE": 4,
    "ACK_WITH_SOURCE": 5
}


def _verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event['params']['header'].get('x-signature-ed25519')
    auth_ts = event['params']['header'].get('x-signature-timestamp')

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(discord_token))
    verify_key.verify(message, bytes.fromhex(auth_sig)
                      )  # raises an error if unequal


def _ping_pong(body):
    return body.get("type") == 1


def interaction(event, context):
    print(f"event {event}")
    
    # verify the signature
    try:
        _verify_signature(event)
    except Exception as e:
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")

    body = event.get('body-json')
    if _ping_pong(body):
        return {"type": 1}

    return {
        "type": RESPONSE_TYPES['MESSAGE_NO_SOURCE'],
        "data": {
            "tts": False,
            "content": body,
            "embeds": [],
            "allowed_mentions": []
        }
    }
