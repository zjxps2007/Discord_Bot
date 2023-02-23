import discord
import datetime
from discord.ext import commands

client = commands.Bot(command_prefix="!")
token = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game('!도움 | {0}ms'.format(int(client.latency * 1000)))
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    guild = member.guild
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0x4CC417, description="✅{0.mention} 님이 서버에 입장하였습니다.".format(member)) #페라리 레드 - 0xF70D1A ✅ ❌

    embed.set_author(name='{0} ({1})'.format(member, member.id), icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text='{0.name}'.format(guild))

    embed.add_field(name="계정 생성일", value=str(date.year) + '-' + str(date.month) + '-' + str(date.day), inline=False)

    await guild.system_channel.send(embed=embed)  # 원하는 서버에 메세지 보낼려면 client.get_channel(channel_Id) / 서버설정 시스템에 보내려면 그대로

@client.event
async def on_member_remove(member):
    guild = member.guild

    embed = discord.Embed(color=0xF70D1A, description='❌{0.mention} 님이 서버에서 퇴장하였습니다.'.format(member))

    embed.set_author(name='{0} ({1})'.format(member, member.id), icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text='{0.name}'.format(guild))

    await guild.system_channel.send(embed=embed)
    

# @client.event
# async def on_voice_state_update(member):
#     guild = member.guild
#     voicstate = discord.VoiceState
#
#     if voicstate.self_mute:
#         embed = discord.Embed(color=0x4CC417, description="✅{0.mention} 님이 서버에 입장하였습니다.".format(member))
#         await guild.system_channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("!정보"):
        await message.channel.send('도움말!')

    if message.content.startswith("!등록"):

        tsg = int(message.author.id)
        username = message.guild.get_member(tsg)
        member = discord.Member
        guild = message.guild
        name = str(message.content[3:len(message.content)]) #!등록 다음부터 저장하는 변수 name

        if message.content == "!등록":
            embed = discord.Embed(color=0xFFFF05, description="!등록 \'[서버]닉네임\'으로 등록해주세요!")
            embed.set_footer(text='{0.name}'.format(guild))
            await message.channel.send(embed=embed)
        else:
            #embed = discord.Embed(color=0xF70D1A, description='❌{0.mention} 님이 서버에서 퇴장하였습니다.'.format(member))
            embed = discord.Embed(color=0xF244A4, description='등록 되었습니다.')
            embed.set_author(name='{0} ({1})'.format(username, tsg), icon_url=message.author.avatar_url)
            embed.set_footer(text='{0.name}'.format(guild))

            for role in message.guild.roles:
                if role.name.lower() in "생존자":
                    if role not in message.author.roles:
                        await message.author.add_roles(role)
                        await member.edit(username, nick=name)
                        await client.get_channel(674885852517892106).send(embed=embed)

client.run(token)
