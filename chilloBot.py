import discord
import requests
import pprint as pp
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # list of commands  

        if (message.content.lower().startswith("!randpoke")):
            await message.channel.send(getRandPokeCommand(message.content))
        elif (message.content.lower().startswith("!randtype")):
            await message.channel.send(getRandTypeCommand(message.content))

# !randpoke

def getRandPoke():
    id = random.randint(1, 700)
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(url)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        return data['name']

def getRandPokeCommand(content):
    # will call getRandomPoke as much as desired in "content", 20 max, 1 by default
    content=content.replace("!randpoke", "").strip()
    count = 1
    responselist = []
    sep = ", "
    if (content.isnumeric()):
        count=int(content)
        if count>20:
            count = 20
    for i in range(0,count):
        responselist.append(getRandPoke())
    return sep.join(responselist)

# !randtype

def getRandType():
    id = random.randint(1,18)
    url = f"https://pokeapi.co/api/v2/type/{id}/"
    response = requests.get(url)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        return data['name']

def getRandTypeCommand(content):
    # will call getRandomType as much as desired in "content", 1 by default
    content=content.replace("!randtype", "").strip()
    count = 1
    responselist = []
    sep = ", "
    if (content.isnumeric()):
        count=int(content)
        if count>18:
            count = 18
    for i in range(0,count):
        responselist.append(getRandType())
    return sep.join(responselist)

# start bot
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token') # PUT TOKEN HERE