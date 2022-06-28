import os
import discord
from discord.ext import  commands
from dotenv import load_dotenv
import urllib.request
from urllib import parse,request
import re
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot=commands.Bot(command_prefix='!') #PREFIX

@bot.command()

async def say_hi(ctx,name):
    response='Hi'+ name
    await ctx.send(response)


@bot.command(name='suma')
async def sumar(ctx,num1,num2):
    response=int(num1)+int(num2)
    await ctx.send(response)

@bot.command()
async def youtube(ctx, *,search):
    query_string=parse.urlencode({'search_query': search})
    html_content = request.urlopen('https://www.youtube.com/results?'+query_string)
    search_results=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v='+search_results[0])
#hola

bot.run(TOKEN)





