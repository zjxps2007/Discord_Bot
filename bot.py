import asyncio
import discord

app = discord.Client()

token = "NjcwMTA5OTc0MDI1ODYzMTc5.XisIUg.H4PFWZJvWnLop8O5HxtC7N4C_gg"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")

    #app.change_presence(game=discord.Game(name="반갑습니다. :D", type=1))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!커맨드":
        embed = discord.Embed(color=0xfff000)
        embed.set_footer(text="등록되었습니다.")

        await message.channel.send(embed=embed)

app.run(token)