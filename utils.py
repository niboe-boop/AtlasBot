"""This is a class for basic functions useful in many places"""
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.Bot(command_prefix=";", intents=intents)

class utils():
  CLIENT = client
  CHANNEL_NEWS = 0

  def init():
    utils.CHANNEL_NEWS = client.get_channel(845793967395962932)

  """" checkmod returns true if user has Admin role. For technical reasons you must put "await" before it to use it without issue."""
  async def checkmod(ctx):
    ismod = False
    for r in ctx.author.roles:
      if r.name == "Admin":
        ismod = True
        break
    return ismod