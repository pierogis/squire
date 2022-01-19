# lambda

### build

You can run this package as an aws lambda function
that will receive events from discord via http

`make` or `make all` within `lambda` (this directory) will call the following `make` commands

 - `make lambda`
 - `make layers` 

These make commands will build requisite
lambda layers and function package inside a docker container

### deploy

Upload the artifacts in `dist` to lambda function
and `layers/dist` to 4 lambda layers

The lambda function should use the layers in the following
order:
 1. numpy
 2. pandas
 3. openai
 4. pynacl

Follow [these](https://oozio.medium.com/serverless-discord-bot-55f95f26f743)
directions for configuring your discord bot, api gateway

[Repo from article](https://github.com/oozio/discord_aws_bot_demo)

Maybe at some point this could be automated with SAM and `make deploy`

Add `OPENAI_API_KEY`, and `DISCORD_PUBLIC_KEY`
environment variables to the lambda function

### register

`make slash` will call a python module (`slash.py`) that registers slash commands `/lyrics` `/ramble`

Use the `.env-template` and `pip install -r requirements-dev.txt` to provide information
needed to register the slash commands with discord