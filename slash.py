"""
post a new slash command to a discord endpoint

uses application id and bot token
"""
import os
import json
from typing import Dict

import requests


def post_slash_command(request_json: Dict[str, any], application_id: str, token: str):
    url = f"https://discord.com/api/v8/applications/{application_id}/commands"

    headers = {
        "Authorization": f"Bot {token}"
    }

    response = requests.post(url, headers=headers, json=request_json)

    print(json.loads(response.content))


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError as e:
        pass

    discord_application_id = os.environ.get('DISCORD_APPLICATION_ID')
    discord_token = os.environ.get('DISCORD_BOT_TOKEN')

    if discord_application_id is None:
        discord_application_id = input("discord application id: ")

    if discord_token is None:
        discord_token = input("discord bot token: ")

    lyrics_json = {
        "name": "lyrics",
        "type": 1,
        "description": "sing like this artist",
        "options": [
            {
                "name": "artist",
                "description": "the name of the artist",
                "type": 3,
                "required": True,
            },
            {
                "name": "artistic_license",
                "description": "how creative to make the response",
                "type": 10,
                "required": False,
                "min_value": 0.0,
                "max_value": 1.0,
            }
        ]
    }

    ramble_json = {
        "name": "ramble",
        "type": 1,
        "description": "regale us with a take",
        "options": [
            {
                "name": "prompt",
                "description": "kinda going off of what you said...",
                "type": 3,
                "required": False,
            },
            {
                "name": "artistic_license",
                "description": "how creative to make the response",
                "type": 10,
                "required": False,
                "min_value": 0.0,
                "max_value": 1.0,
            }
        ]
    }

    tweet_json = {
        "name": "tweet",
        "type": 1,
        "description": "what would @{username} think about this",
        "options": [
            {
                "name": "username",
                "description": "twitter handle",
                "type": 3,
                "required": True,
            },
            {
                "name": "artistic_license",
                "description": "how creative to make the response",
                "type": 10,
                "required": False,
                "min_value": 0.0,
                "max_value": 1.0,
            }
        ]
    }

    post_slash_command(lyrics_json, discord_application_id, discord_token)
    post_slash_command(ramble_json, discord_application_id, discord_token)
    post_slash_command(tweet_json, discord_application_id, discord_token)
