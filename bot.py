import discord
import datetime
from discord.ext import commands
client = commands.Bot(command_prefix="!")

token = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game('!커맨드 | {0}ms'.format(int(client.latency * 1000)))
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):

    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    nowtime = datetime.datetime.now()

    embed = discord.Embed(color=0x4CC417)  #페라리 레드 - 0xF70D1A

    embed.add_field(name="이름", value=member.name)
    #embed.add_field(name="서버닉네임", value=member.display_name)
    embed.add_field(name="가입일", value=str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일')
    embed.add_field(name='ID', value=member.id)
    embed.set_thumbnail(url=member.avatar_url)

    embed.set_footer(text=str(nowtime.year) + '년 ' + str(nowtime.month) + '월 ' + str(nowtime.day) + '일 | ' + str(nowtime.hour) + ': ' + str(nowtime.minute) + ': ' + str(nowtime.second))

    await member.guild.system_channel.send(embed=embed)


    # guild = member.guild
    # if guild.system_channel is not None:
    #     to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
    #     await guild.system_channel.send(to_send)

    # embed = discord.Embed(color=member.color)
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
    #
    # # embed.add_field(name="Bot?", value=member.bot)
    #
    # await guild.system_channel.send(embed=embed)

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

        #이름 변경


client.run(token)