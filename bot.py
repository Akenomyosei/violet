import discord
from discord.ext import commands
import json 
import random
import os

with open ('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='{',intents=intents)
bot.remove_command("help")


#終端機印出訊息
@bot.event
async def on_ready():
    print(">>bot is ready<<")

#伺服器端印出訊息(垃圾。)
@bot.event
async def on_ready_message(ctx):
    await ctx.send(f">>Bot is online<<")

#歡迎訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["welcome & leave"]))
    await channel.send(f'{member} join!')

#help(以後轉標準模式)
@bot.command()
async def help(ctx):
    await ctx.send(f'這是一個可愛的bot,但它甚麼都不會\n它現在只會:\nhelp:你正在看,不是嗎?\npic:傳一些無聊的圖片\nping:延遲好耶\np.s:製作者正在試圖讓它發出噪音,請趕快阻止他'
)

#離開訊息
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["welcome & leave"]))
    await channel.send(f'{member} leave!')

@bot.command()
async def load(ctx,extention):
    bot.load_extension(f'cmds.{extention}')
    await ctx.send(f'Loaded {extention} done')
    
@bot.command()
async def unload(ctx,extention):
    bot.unload_extension(f'cmds.{extention}')
    await ctx.send(f'Un-Loaded {extention} done')
    
@bot.command()
async def reload(ctx,extention):
    bot.reload_extension(f'cmds.{extention}')
    await ctx.send(f'Re-Loaded {extention} done')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
    
