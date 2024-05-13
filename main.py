//feliciaxxx bot source code
//please give credit😏
import nextcord
import requests
import asyncio
import datetime
from nextcord.ext import commands
from nextcord.ext.commands.core import has_permissions
from nextcord.ext import tasks
from nextcord.ext.commands import DefaultHelpCommand

intent = nextcord.Intents.all()

bot = commands.Bot(command_prefix="-", intents=intent)
apikey = "E99l9NOctud3vmu6bPne"
madeby = "YourName"

presences = [
    nextcord.Activity(name="Feliciaa", type=nextcord.ActivityType.watching),
    nextcord.Activity(name="FellAlexandra", type=nextcord.ActivityType.listening),
]

current_index = 0

@tasks.loop(seconds=15)
async def change_presence():
    global current_index
    await bot.change_presence(activity=presences[current_index])
    current_index = (current_index + 1) % len(presences)


@bot.event
async def on_ready():
    change_presence.start()
    print(f"{bot.user.name} Your Bot Now Is Online By @pxhira666")

@bot.slash_command(name="hydrogen", description="gets your hydrogen key")
async def hydrogen(ctx, link: str):
        hwid = link.replace("https://gateway.platoboost.com/a/2569?id=", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-hydrogen/?hwid={hwid}&api_key={apikey}")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ hydrogen Key", url=link, colour=0xff0000)
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/924722337981530132/73e6c24fec92005c5521b58bcd8c9e5d.webp?size=128")
        embed.set_footer(text="Made By {madeby}")
        await ctx.send(embed=embed)

@bot.slash_command(name="codex", description="gets your codex key")
async def codex(ctx, link: str):
        hwid = link.replace("https://mobile.codex.lol/?token=", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-codex/?token={hwid}&api_key=api key")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ Codex Key", colour=0xff0000)
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1217863434519973909/1223625451545563246/codexx.png?ex=661a8901&is=66081401&hm=30863126bf2d9b7d1df0340ef0631c0cbdc5d36b7214592f4faf6adce0ec5b71&=&format=webp&quality=lossless&width=978&height=978")
        embed.set_footer(text="Made By FellAlexandra")
        await ctx.send(embed=embed)

@bot.slash_command(name="arceus", description="gets your arceus key")
async def arceus(ctx, link: str):
        hwidd = link.replace("https://spdmteam.com/key-system-1?hwid=", "")
        hwid = hwidd.replace("&zone=Europe/Rome&os=android", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-arceusx/?hwid={hwid}&api_key=api key")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ Arceus Key", colour=0xff0000)  # Define embed here
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1217863434519973909/1223626225625464893/Arceus-X-NEO-Logo.png?ex=661a89ba&is=660814ba&hm=7ed62e1a264d3914c27976cc0385d034bba7a926323e3894ad57aa8739287f7f&")
        embed.set_footer(text="Made By FellAlexandra")
        await ctx.send(embed=embed)

@bot.slash_command(name="hoho", description="gets your hoho hub key")
async def hoho(ctx, link: str):
        hwid = link.replace("https://hohohubv-ac90f67762c4.herokuapp.com/api/getkeyv2?hwid=", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-hohohubv/?hwid={hwid}&api_key=api key")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ Hoho Key", colour=0xff0000)
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1217863434519973909/1223625452103401592/hoho.jpg?ex=661a8901&is=66081401&hm=d9113229a580f4bcf13b3843a9523e1f09c72fa42dc0a2249e56fd9b40ce215e&=&format=webp&width=978&height=978")
        embed.set_footer(text="Made By FellAlexandra")
        await ctx.send(embed=embed)

@bot.slash_command(name="delta", description="gets your delta key")
async def delta(ctx, link: str):
        hwid = link.replace("https://gateway.platoboost.com/a/8?id=", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-delta/?hwid={hwid}&api_key=api key")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ Delta Key", url=link, colour=0xff0000)
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1217863434519973909/1223625451860267162/deltaa.jpg?ex=661a8901&is=66081401&hm=9037596b5e0209832fd6b1791ff39793d2c2c5799dd75f2d0ca2c7b45ddcb5f2&=&format=webp&width=480&height=480")
        embed.set_footer(text="Made By FellAlexandra")
        await ctx.send(embed=embed)

@bot.slash_command(name="trigon", description="gets your trigon key")
async def trigon(ctx, link: str):
        hwid = link.replace("https://trigonevo.com/getkey/?hwid=", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-trigon/?hwid={hwid}&api_key=api key")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ Trigon Key", url=link, colour=0xff0000)
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1217863434519973909/1223625452350869594/trigon.jpg?ex=661a8901&is=66081401&hm=ba3a5494031f2271f1fa987ac67d4e131b9b094aa167c78468b1180dda2dfee3&=&format=webp&width=450&height=450")
        embed.set_footer(text="Made By FellAlexandra")
        await ctx.send(embed=embed)

@bot.slash_command(name="vega", description="gets your vegax key")
async def vegax(ctx, link: str):
        hwidd = link.replace("https://pandadevelopment.net/getkey?service=vegax&hwid=", "")
        hwid = hwidd.replace("&provider=linkvertise", "")
        await ctx.send("getting your key..")
        response = requests.get(f"https://stickx.top/api-vegax/?hwid={hwid}&api_key=api key")
        newresponse = response.text.replace("key", "")
        n = newresponse.replace('{"":"', "")
        nn = n.replace('"}', "")
        embed = nextcord.Embed(title="ðŸ”‘ Your key has been bypassed.", url=link, colour=0xa700f5)
        embed.set_author(name="Key Bypassed!")
        embed.add_field(name="Hold to copy", value=nn, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1217863434519973909/1223625715409354802/vegax.png?ex=661a8940&is=66081440&hm=9112e53acdaf44414483365f845142204d3589a84abf16a6e329bebd142ab37f&")
        embed.set_footer(text="Made By FellAlexandra")
        await ctx.send(embed=embed)

bot.run("your bot token asf")
