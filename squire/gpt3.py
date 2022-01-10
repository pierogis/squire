import openai


def generate_lyrics(
    artist: str,
    temperature: float = 0.8,
    max_tokens: int = 256,
    frequency_penalty: float = 0.9,
) -> str:
    prompt_text = f"Artist: {artist}\n\nLyrics:\n"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
    )

    return response["choices"][0]["text"]


def ramble(
    prompt: str,
    temperature: float = 0.8,
    max_tokens: int = 256,
    frequency_penalty: float = 0.9,
) -> str:
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
    )

    return response["choices"][0]["text"]
