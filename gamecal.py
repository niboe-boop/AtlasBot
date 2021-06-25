from discord.ext.commands import Cog, command
from discord.ext.tasks import loop

import datetime
import asyncio
from replit import db
from math import floor, ceil

from utils import utils

class Calendar(Cog):

  TIMESCALE = 20

  def __init__(self):
    #self.bot = client
    self.calendar_loop.start()
  
  def cog_unload(self):
    self.cancel()

  def ingameTime():
    """Returns a list of the following
    0: Datetime gamedate 
    1: Int gamedays
    2: Int gamehours
    3: Int irlminutes"""
    gametime = datetime.datetime.now(datetime.timezone.utc) - datetime.datetime.strptime(db["epochreal"], '%Y-%m-%d %H:%M:%S.%f%z')
    irlminutes = gametime.total_seconds()/60
    gamehours = irlminutes/Calendar.TIMESCALE
    gamedays = floor(gamehours/24)
    passedtime = datetime.timedelta(hours=gamehours)
    gamedate = datetime.datetime.strptime(db["epochingame"], '%Y-%m-%d %H') + passedtime
    gamehours = floor(gamehours)%24
    return [gamedate, gamedays, gamehours, irlminutes]

  @command()
  async def time(self, ctx):
    dateinfo = Calendar.ingameTime()
    gamedate = datetime.datetime.strftime(dateinfo[0], "%Y-%m-%d %H:00")
    await ctx.send("It is currently " + gamedate + ". It is " + str(dateinfo[1]) + " ingame days and " + str(dateinfo[2]) + " ingame hours since the epoch.")

  @command()
  async def setepoch(self, ctx, year, month, day, hour):
    if await utils.checkmod(ctx):
      # epochreal is the irl time that the epochdb["key"] = "value" was set. Used for calculating elapsed ingame time.
      # epochingame is the fictional time that the epoch began.
      db["epochreal"] = str(datetime.datetime.now(datetime.timezone.utc))
      db["epochingame"] = f"{year}-{month}-{day} {hour}"
      await ctx.send("Epoch set successfully.")
    else:
      await ctx.send("You don't have permission to use this command.")

  @command()
  async def scheduleevent(self, ctx, year, month, day, hour, message):
    string = f"{year}-{month}-{day}-{hour}"
    db[string] = message
    await ctx.send(f"Scheduled event for {year}-{month}-{day} at {hour}")

  @loop()
  async def calendar_loop(self):
    now = datetime.datetime.now(datetime.timezone.utc)
    nexthour = now + datetime.timedelta(minutes=Calendar.TIMESCALE)
    mins = nexthour.minute
    hour = nexthour.hour
    newmins = floor(mins/Calendar.TIMESCALE) * Calendar.TIMESCALE
    if newmins < 60:
      mins = newmins
    else:
      mins = newmins - 60
      hour += 1

    nexthour = nexthour.replace(hour=hour, minute=mins, second=0, microsecond=0)
    seconds_until = (nexthour - now).total_seconds()

    print(f"printing in {floor(seconds_until/60)} mins and {seconds_until%60} seconds")
    await asyncio.sleep(seconds_until)
    print(datetime.datetime.now())

    gametime = Calendar.ingameTime()
    gametime = gametime[0]

    print(gametime.year)
    print(gametime.month)
    print(gametime.day)
    print(gametime.hour)
    try:
      key = f"{gametime.year}-{gametime.month}-{gametime.day}-{gametime.hour}"
      message = db[key]
      channel = utils.CHANNEL_NEWS
      await channel.send(message)
      del db[key]
    except KeyError:
      print("An ingame hour has passed. There is no new event.")
