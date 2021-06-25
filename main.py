import os
import discord
from replit import db
from discord.ext import commands

import gamecal
import profiles
from utils import utils

# this is the number of irl minutes per ingame hour.
TIMESCALE = 20

client = utils.CLIENT
client.add_cog(gamecal.Calendar())
client.add_cog(profiles.Profiles())


@client.event
async def on_ready():
    print(f'{client.user} has connected.')
    #if "profile" != db.keys():
    #  db[profile] = {atlas : ["org", "Worldly City of Atlas", ["All Worldly Things"], ["An international congress of all worldly entities, nations, and orginisations.", "_", "_", "_", "_"], "flag link here", [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]}
    utils.init()


@client.command()
async def ping(ctx):
    await ctx.send("Pong! " + str(round(client.latency * 1000)) + "ms")


@client.command()
async def test(ctx):
    if await utils.checkmod(ctx):
        channel = utils.CHANNEL_NEWS
        await channel.send("buh")
    else:
        await ctx.send("You don't have permission to use this command.")


client.run('ODQ1MzM5NjY1NzA4MDg5MzQ0.YKfh6Q.q31lMHLCCGOR75vuFgxVe6pFdCs')

#Things lolo want:
#1. INGAME DATE: 20 irl mins = 1 ingame day
#1. a. ;date or ;d to call the current date/time in game
#1. b. admin ability to reset beginning date reference point
#1. c. certain role ability to schedule a message according to in-game time.

#2. PROFILE/STATS: view/list/new/edit
#2. a. Profiles will probably be in a dictionary in the database dictionary
#2. b. db = {profile : {key-word : ["ent/nat/org", "full name", ["player1"], ["info1","info2","info3"], [stats 1-?], [ratios]]}
#2. c. Only player and mods can edit a persons profile.
#2. d. idk what yet but I want the values and ratios to be able to directed to certain things givening the pts/yr in something like "medical development" to give to some restriction on growth.
#2.

#3. Events! (Ability to plot events/disocveries according to in-game time, development points, and other variables.)
#3. Not necessary but would be very very very very good.
