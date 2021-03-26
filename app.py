import discord
import os
import names
import random

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

name_messages = [
    "I have selected only the finest names for you, aged in an oak barrel: ",
    "Do these names tickle your fancy? ",
    "Peep your eyes upon these bitchin' nombres! ",
    "What shall I call you, worm?",
    "Your destiny lies in the names below... Choose wisely."
]

@client.event
async def on_ready():
    print('We have logged in!')

# This runs every time a message is posted in the channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$names'):
        
        name_message = "_**" + random.choice(name_messages) + "**_" + '\n'

        new_names = []
        for i in range(5):
            new_name = names.get_full_name()
            new_names.append(new_name)
        names_string = "`" + ", ".join(new_names) + "`"

        await message.channel.send(name_message + names_string)

client.run(os.environ.get('TOKEN'))
