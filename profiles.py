from discord.ext.commands import command, Cog

import utils

class Profiles(Cog):
  @command()
  async def profile(ctx, arg1, arg2):
    db_prof = db[profile]
    if arg1 == "list":
      if arg2 == "all":
        pass
      if arg2 == "nat":
        pass
      if arg2 == "org":
        pass
      if arg2 == "ent":
        pass
      if arg2 == null:
        await ctx.message.send("list all/nat/org/ent")
    if arg1 == "view":
      if arg2 == db_prof.keys():
        pass
    if arg1 == "new":
      pass
      #db_prof[arg2] = [0,0,0,0,0]

  @command()
  async def edit(ctx, arg1, arg2, arg3, arg4):
    if arg1 == "profile":
      #if member of profile check here
        pass
    if arg1 == "stats":
      if await utils.checkmod(ctx):
        pass