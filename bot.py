import discord
from discord.ext import commands
import json 
import random


with open ('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='{',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["welcome & leave"]))
    await channel.send(f'{member} join!')

@bot.command()
async def helping(ctx):
    await ctx.send(f'這是一個可愛的bot,但它甚麼都不會\n它現在只會:\nhelp:你正在看,不是嗎?\npic:傳一些無聊的圖片\nping:延遲好耶\np.s:製作者正在試圖讓它發出噪音,請趕快阻止他'
)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["welcome & leave"]))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def pic(ctx):
    random_pic = random.choice(jdata["pic"])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)

bot.run(jdata['TOKEN'])