import discord
import openai
import os

# Set up OpenAI API key
openai.api_key = "OPENAI-TOKEN"
TOKEN = "DISCORD-TOKEN"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} запущен.')


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        promt = str(message.content)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {
                    "role": "system",
                    "content": "Ты искусственный интеллект, созданный для помощи людям."
                },                            
                {
                    "role": "user",
                    "content": promt
                }
        ],
    ).choices[0].message.content

    print(promt)
    print(response)

    await message.channel.send(response)

client.run(TOKEN)