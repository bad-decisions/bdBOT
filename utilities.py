import discord
from discord.ext import commands
import random
import asyncio
class utilities(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command(description='Displays client latency')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(description='Picks a random scale')
    async def scale(self,ctx):
        key = random.randint(0,6)
        keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        actl = random.randint(0,2)
        actls = ['#', '♭', 'n']
        tnty = random.randint(0,2)
        tntys = ['Major', 'Minor', 'Modal']
        embed = discord.Embed(
            colour = ctx.author.colour
        )
        embed.set_author(name='Random Scale', icon_url=ctx.author.avatar_url)
        if actls[actl] != 'n':
            embed.add_field(name='Your scale is...', value = f'{keys[key]} {actls[actl]} {tntys[tnty]}')
        else:
            embed.add_field(name='Your scale is...', value = f'{keys[key]} {tntys[tnty]}')
        await ctx.send(embed=embed)

    @commands.command(description='Sets a timer for a specific amount of time in seconds')
    async def timer(self, ctx, length, *, units):
        t = int(length)
        await ctx.send("Setting timer for {} {}".format(t, units))
        i = 0
        if units == "seconds" or units == "second":
            for i in range(t):
                i += 1
                await asyncio.sleep(1)
        elif units == "minute" or units == "minutes":
            for i in range(t):
                i += 1
                await asyncio.sleep(60)
        elif units == "century" or units == "centuries":
            await ctx.send("fuck off")
        elif units == "hour" or units == "hours":
            for i in range(t):
                i += 1
                await asyncio.sleep(3600)
        await ctx.send("Timer finished")

    @commands.command(description='Logs a formal complaint to be processed')
    async def complain(self, ctx, *, complaint):
        await ctx.message.delete()
        await ctx.send("Logging complaint")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            colour = ctx.author.colour
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name='A complaint has been made:', value = complaint)
        await ctx.send(embed=embed)

    

def setup(client):
    client.add_cog(utilities(client))
