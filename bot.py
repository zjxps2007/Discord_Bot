import discord

client = discord.Client()

token = "NjcxNTg2Nzg3ODA5ODIwNzM0.Xi_GCg.WDTzsjGHcHYE7h9CHh2YVw2vgw8"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!커맨드":
        await message.channel.send('Hello!')

client.run(token)