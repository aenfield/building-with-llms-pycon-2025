import llm

# model = llm.get_model('gpt-4.1-mini')

# # simple
# response = model.prompt(
#     'A joke about a walrus who lost his shoes'
# )
# print(response.text())

# # streaming
# for chunk in model.prompt(
#     'A joke about a pelican that rides a bicycle, and then explain why the joke is funny',
#     stream=True
# ):
#     print(chunk, end='', flush=True)

# # attachments
# response = model.prompt(
#     'Describe this image',
#     attachments=[
#         llm.Attachment(
#             url='https://static.simonwillison.net/static/2025/two-pelicans.jpg',
#         )
#     ]
# )
# print(response.text())

# # system prompts
# def translate_to_spanish(text):
#     model = llm.get_model('gpt-4.1-mini')
#     response = model.prompt(text, system='Translate this to Spanish')
#     return response.text()

# print(translate_to_spanish("What's the best thing about a pelican?"))

# async support
import asyncio

model = llm.get_async_model('gpt-4.1-mini')
async def main():
    response = model.prompt('A funny walrus joke')
    async for chunk in response:
        print(chunk, end='', flush=True)
    # or just print(await response.text())

asyncio.run(main())