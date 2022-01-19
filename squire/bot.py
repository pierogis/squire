from discord import Client, Message
from squire import gpt3


def create_client(temperature: float) -> Client:
    client = Client()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message: Message):
        if message.author == client.user:
            return

        if message.content.startswith("/lyrics"):
            args = message.content.split(" ", 2)
            try:
                if len(args) > 1:
                    artist = args[1]
                    await message.add_reaction('🥟')
                    try:
                        lyrics = gpt3.generate_lyrics(
                            artist, temperature=temperature)
                        await message.reply(lyrics)
                    except Exception as e:
                        print(e)
                        await message.remove_reaction('🥟', client.user)
                        await message.add_reaction('🤷')
                        await message.reply("That didn't work")
                else:
                    await message.remove_reaction('🥟')
                    await message.reply("Try providing an artist next time")

            except Exception as e:
                print(e)

        if message.content.startswith("/ramble"):
            args = message.content.split(" ", 2)
            try:
                if len(args) > 1:
                    prompt = args[1]
                else:
                    prompt = ""
                await message.add_reaction('🥟')
                try:
                    lyrics = gpt3.ramble(prompt, temperature=temperature)
                    await message.reply(prompt + lyrics)
                except Exception as e:
                    print(e)
                    await message.remove_reaction('🥟', client.user)
                    await message.add_reaction('🤷')
                    await message.reply("That didn't work")

            except Exception as e:
                print(e)

    return client
