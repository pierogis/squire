import json
import os
from enum import Enum
from typing import Dict

import boto3 as boto3
from nacl.signing import VerifyKey

discord_public_key = os.environ.get("DISCORD_PUBLIC_KEY")
command_lambda_arn = os.environ.get("COMMAND_LAMBDA_ARN")


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


def _verify_signature(event):
    raw_body = event["rawBody"]
    auth_sig = event['params']['header']['x-signature-ed25519']
    auth_ts = event['params']['header']['x-signature-timestamp']

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(discord_public_key))
    verify_key.verify(message, bytes.fromhex(auth_sig))


def interaction(event: Dict[str, any], context):
    """
    the actual lambda handler
    """
    _verify_signature(event)

    body = event['body']

    if InteractionType(body["type"]) == InteractionType.PING:
        print("pong")
        return {
            "type": InteractionCallbackType.PONG.value,
        }
    else:
        command_data = body['data']
        interaction_token = body['token']
        application_id = body['application_id']

        payload = {
            "interaction_token": interaction_token,
            "command_data": command_data,
            "application_id": application_id,
        }

        client = boto3.client("lambda")

        client.invoke(
            FunctionName=command_lambda_arn,
            InvocationType='Event',
            Payload=json.dumps(payload)
        )

        return {
            "type": InteractionCallbackType.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE.value,
        }
