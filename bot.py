import discord

client = discord.Client()

token = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("!커맨드")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!커맨드":
        await message.channel.send('Hello!')

    if message.content.startswith("!등록"):
        name = message.content[4:len(message.content)]
        Id = client.user.id
        await message.channel.send(Id)
        try:
            await message.channel.send(name)
        except:
            #print("다시 입력")
            await message.channel.send("다시입력")




# @client.evet
# async def on_member_join(member):



client.run(token)