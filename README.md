# squire

discord bot with gpt3 integration

## commands

`/lyrics {artist} --temperature {temperature}`

Creates a verse based on `artist`

`/ramble {prompt} --temperature {temperature}`

Rambles on, continuing optional `prompt`

Optional value `temperature` is roughly how creative you want the bot to be (0.0 - 1.0)

## cli

`python -m squire lyrics`

`python -m squire ramble`

Requires that the environment/.env file contains api keys (see configuration)

## hosting

##### listener
Create an aws instance and run an event listener using the `discord.py` library

`poetry run python squire discord-bot`

##### lambda
Create an aws lambda function, lambda layer, and api gateway trigger to handle discord events

See `lambda` for more information

## configuration
This bot needs access to a discord bot token and an openai token.

Config can be provided in a `.env` folder at the working directory.

See `.env-template` for required keys.