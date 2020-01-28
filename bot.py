import discord

client = discord.Client()

token = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("!커맨드|")
    await client.change_presence(status=discord.Status.online, activity=game)

# @client.event
# async def on_member_join(member):
#     ts = member.id
#     return ts

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!커맨드":
        await message.channel.send('Hello!')

    if message.content.startswith("!등록"):
        #!등록 다음부터 저장하는 변수 name
        name = message.content[4:len(message.content)]
        #유저 아이디 저장할 변수 & 출력
        member = client.user.id
        await message.channel.send(member)
        #이름을 잘못등록햇을때의 예외처리
        try:
            await message.channel.send(name)
        except:
            await message.channel.send("다시입력")



client.run(token)