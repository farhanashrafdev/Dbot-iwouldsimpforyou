import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_Ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hey there Plums :D")

@client.command()
async def day(ctx):
    await ctx.send("Today is an amazing day")


client.run("") #this is where your bot's key code goes in
