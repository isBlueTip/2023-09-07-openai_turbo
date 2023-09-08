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


# async def transcribe_voice_message(audio) -> tuple:  # typing wtf?!
#     try:
#         response = await openai.ChatCompletion.acreate(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0,
#             max_tokens=1024,
#         )
#         return response['choices'][0]['message']['content'], response['usage']['total_tokens']
#     except Exception as e:
#         logging.error(e)
#         return ()


# response = await openai.ChatCompletion.acreate(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"},
#     ],
#     temperature=0,
#     max_tokens=1024,
# )
