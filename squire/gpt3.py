import openai
import tweepy


def generate_lyrics(
        artist: str,
        temperature: float = 0.8,
        max_tokens: int = 256,
        frequency_penalty: float = 0.7,
) -> str:
    prompt_text = f"Artist: {artist}\n\nLyrics:\n"

    response = openai.Completion.create(
        engine="curie",
        prompt=prompt_text,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
    )

    return response["choices"][0]["text"].strip()


def generate_tweet(
        client: tweepy.Client,
        username: str,
        temperature: float = 0.8,
        max_tokens: int = 256,
        frequency_penalty: float = 0.7,
) -> str:
    user = client.get_user(username=username)
    tweets = client.get_users_tweets(user.data.id, exclude=['replies'])
    tweets_string = '\n\n'.join([tweet.text for tweet in tweets.data])
    prompt_text = f"Tweets:\n{tweets_string}\n\nTweet:\n"

    response = openai.Completion.create(
        engine="curie",
        prompt=prompt_text,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
    )

    return response["choices"][0]["text"].strip()


def ramble(
        prompt: str,
        temperature: float = 0.8,
        max_tokens: int = 256,
        frequency_penalty: float = 0.8,
) -> str:
    response = openai.Completion.create(
        engine="babbage",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
    )

    return response["choices"][0]["text"].strip()
