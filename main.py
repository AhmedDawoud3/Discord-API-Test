# bot.py
import os
import random
import discord
from discord import member
from dotenv import load_dotenv
from discord.utils import get


text = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye"""
text = text.split("\n")
load_dotenv()
TOKEN = os.getenv('DiscordBotAPI')

client = discord.Client()


@client.event
# async def getUserFromMention(mention):
#     await mention.create_dm()
#     await mention.dm_channel.send(
#         f'Hi welcome to my Discord server!'
#     )
async def on_message(message):
    org = message
    # message.author.id
    message = str(message.content).replace("<@!", "").replace(">", "")
    user = await client.fetch_user(message)
    await user.create_dm()
    for tex in text:
        await user.dm_channel.send(tex)
    # await user.create_dm()
    # await user.dm_channel.send(
    #     f'Hi welcome to my Discord server!'
    # )

# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

client.run(TOKEN)
# client.close()
