import discord
import asyncio
from discord.ext import commands
client = commands.Bot(command_prefix="!")

token = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("!커맨드|")
    await client.change_presence(status=discord.Status.online, activity=game)

# @client.event
# async def on_member_join( ctx, member):

    # embed = discord.Embed(color=member.color,)
    #
    # embed.set_author(name=f"User Info - {member}")
    # embed.set_thumbnail(url=member.avatar_url)
    # embed.set_footer(text="{Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    #
    # embed.add_field(name="ID", value=member.id)
    # embed.add_field(name="Guild name", value=member.display_name)
    #
    # embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    # embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!커맨드":
        await message.channel.send('Hello!')

    if message.content.startswith("!등록"):

        # 유저 아이디 저장할 변수 & 출력
        # tsg = message.author.id
        # await message.channel.send(tsg)

        #!등록 다음부터 저장하는 변수 name
        name = message.content[4:len(message.content)]

        #이름을 잘못등록햇을때의 예외처리
        try:
            await message.channel.send(name)
        except:
            print("다시입력")
            #await message.channel.send("다시입력")

        #권한 변경
        for role in message.guild.roles:
            if role.name.lower() in "생존자":
                if role not in message.author.roles:
                    await message.author.add_roles(role)

client.run(token)