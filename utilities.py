import discord
from discord.ext import commands
import random
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

def setup(client):
    client.add_cog(utilities(client))
