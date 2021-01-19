import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$")

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
async def there?(ctx):
    await ctx.send("Hazir Janab")
    
    
@client.command()
async def there(ctx):
    await ctx.send("Hazir Janab")
    
@client.command()
async def perfect(ctx):
    await ctx.send("Chal hun mera put chuti kr")
client.run("ODAwOTUwNTg2ODUzMDMxOTY3.YAZlXA.x83RaYk0JSnF1ha4ZCuWCQp2z00") #this is where your bot's key code goes in
