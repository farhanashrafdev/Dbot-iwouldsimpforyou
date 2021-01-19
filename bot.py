import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_Ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hello there baby gurl.")

@client.command()
async def day(ctx):
    await ctx.send("Today is an amazing day")

@client.command()
async def couldyouboostforme(ctx):
    await ctx.send("Read My Name NIGGA")

@client.command()
async def perfect(ctx):
    await ctx.send("Chal hun mera put chuti kr")
    

@client.command()
async def hey(ctx):
    await ctx.send("Chal hun mera put chuti kr")
    
    
@client.command()
async def BC(ctx):
    await ctx.send("Bht Cute")
    
@client.command()
async def banBlackMamba(ctx):
    await ctx.send("User BlackMamba#0468 will be removed after 1 minute")
    
    
client.run(os.environ['BOT_KEY']) 
