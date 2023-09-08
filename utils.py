import logging

import openai

import config

openai.api_key = config.GPT_35_TURBO_API_KEY


async def generate_text_response(prompt) -> tuple:  # typing wtf?!
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=1024,
        )
        return response["choices"][0]["message"]["content"], response["usage"]["total_tokens"]
    except Exception as e:
        logging.error(e)
        return ()
