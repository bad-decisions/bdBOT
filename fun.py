import discord
from discord.ext import commands
import random
class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    async def hello(self, ctx):
        await ctx.message.delete()
        await ctx.send('hello')

    @commands.command()
    async def future(self, ctx,):
        number = random.randint(1,4)
        if ctx.author.id == 241161696561987585 or 522124478822744064:
            await ctx.send("f**k off madoc you're future ist getting any brighter from doing this")
        elif number == 1:
            await ctx.send("You're going to live for a bit then die for a bit")
        elif number == 2:
            await ctx.send("You're too dead to predict a future for you")
        elif number == 3:
            await ctx.send("YOU THINK YOU HAVE A FUTURE XD !?!!?!")


    @commands.command()
    async def boop(self, ctx, member: discord.Member):
        await ctx.message.delete()
        await ctx.send("boop {} from {} xx".format(member.mention, ctx.author.mention))

    
def setup(client):
    client.add_cog(Fun(client))
    
