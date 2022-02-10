print("hi")
import discord
import os
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from replit import db
from keepalive import keep_alive

client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print("Online")     
    
@client.command()
async def ping(ctx):
  await ctx.send("pong!") 


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  aut = str(message.author)

  if msg.startswith("!shorts"):
    await message.channel.send("stinks")

  if msg.startswith("!check"):
    for key in db.keys():
      await message.channel.send(str(aut) + " has sent " + str(db[key]) + " messages")
  
  if aut in db.keys():
    val = db[aut] + 1
    print("Increasing " + aut +" to "+ str(db[aut]))
    db[aut] = val
  else:
    print("Creating " + aut)
    db[aut] = 1

#keep_alive()
client.run(os.environ['TOKEN'])