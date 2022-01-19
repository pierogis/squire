# squire

discord bot with gpt3 integration

## install

`pip install squire[.env]`

Including the `[.env]` extra installs `python-dotenv` used to load api key(s) from a `.env` file

## cli

To use the commands standalone (outside discord):

`squire lyrics {artist} --temperature {temperature}`

`squire ramble {artist} --temperature {temperature}`

Provide api keys through the environment/.env file (see [configuration](#configuration))
or enter them when prompted

## slash commands

The `lambda` dir contains directions for setting up lambda function that handles slash commands

`/lyrics {artist} artistic_liberty:{artistic_liberty}`

Creates a verse based on `artist`

`/ramble {prompt} artistic_liberty:{artistic_liberty}`

Rambles on, continuing optional `prompt`

Optional value `artistic_liberty` is roughly how creative you want the bot to be (0.0 - 1.0)

## hosting

##### listener

Create an aws instance and run an event listener using the `discord.py` library

`poetry run python squire discord-bot`

##### lambda

Create an aws lambda function, lambda layer, and api gateway trigger to handle discord events

See `lambda` directory for more information

## configuration

To run the bot, it needs access to a discord bot token and an openai token.

Commands will prompt for these keys.

Config can also be provided in a `.env` file at the working directory for local requests/bot hosting.

See/copy `.env-template` for required keys.

`pip install python-dotenv` to install the loader package for this method
(installed by command provided in [install](#install))