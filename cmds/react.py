import discord
from discord.ext import commands
from core.classes import Cog_Extention
import random
import json

with open ('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
class React(Cog_Extention):
    
    #圖片
    @commands.command()
    async def pic(self,ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)
        
def setup(bot):
    bot.add_cog(React(bot))