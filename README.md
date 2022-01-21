# squire

discord bot with gpt3 integration

## install

`pip install squire[.env]`

Including the `[.env]` extra installs `python-dotenv` used to load api key(s) from a `.env` file

## cli

To use the commands standalone (outside discord):

`squire lyrics {artist} --temperature {temperature}`

`squire ramble {artist} --temperature {temperature}`

Provide api keys through the environment/`.env` file (see `.env-template`)
or enter them when prompted

## slash commands

The `lambda` dir contains directions for setting up lambda function that handles slash commands

`/lyrics artist:{artist} artistic_liberty:{artistic_liberty}`

Creates a verse based on `artist`

`/ramble artist:{prompt} artistic_liberty:{artistic_liberty}`

Rambles on, continuing optional `prompt`

Optional value `artistic_liberty` is roughly how creative you want the bot to be (0.0 - 1.0)

## hosting

### lambda

You can use this package as an aws lambda function that will receive events from discord via http

There is a sam template that will create an aws lambda function, lambda layers, and api gateway trigger to handle these
interaction events

You will need to install `aws cli`, `sam` and create an IAM access key on aws, then:

```shell
aws configure
sam build --use-container
sam deploy --guided
```

Finally, [register](#register) the slash command with discord.

#### build

`make build` will use `sam build`, but first remove the .venv directory (if present) since it causes issues with the
docker build.

#### register

`make slash` will call a python module (`slash.py`) that registers slash commands `/lyrics` `/ramble`

Use the `.env-template` and `pip install -r requirements-dev.txt` to provide information needed to register the slash
commands with discord.

`pip install python-dotenv` to install the loader package for this method
(installed by command provided in [install](#install))

### listener

Create an aws instance and run a stinky event listener using the `discord.py` library

`poetry run python squire discord-bot`