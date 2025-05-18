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
# import asyncio

# model = llm.get_async_model('gpt-4.1-mini')
# async def main():
#     response = model.prompt('A funny walrus joke')
#     async for chunk in response:
#         print(chunk, end='', flush=True)
#     # or just print(await response.text())

# asyncio.run(main())

# # structured data extraction
# import json
# from pydantic import BaseModel

# class Pelican(BaseModel):
#     name: str
#     age: int
#     short_bio: str
#     beak_capacity_ml: float

# model = llm.get_model('gpt-4.1-mini')
# response = model.prompt('Describe a spectacular pelican', schema=Pelican)
# pelican = json.loads(response.text())
# print(pelican)

# calling tools
model = llm.get_model('gpt-4.1-mini')

def lookup_population(country: str) -> int:
    "Returns the current population of the specified fictional country"
    if country == 'Crumpet':
        return 123124
    else:
        return 42

def can_have_dragons(population: int) -> bool:
    "Returns True if the specified population can have dragons, False otherwise"
    return population > 10000

chain_response = model.chain(
    "Can the country of Crumpet have dragons? What about the country of Foo? What about the USA? What about France? Answer with only YES or NO",
    tools=[lookup_population, can_have_dragons],
    stream=False
)
print(chain_response.text())