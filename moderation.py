import discord
from discord.ext import commands
import time
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command()
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount) + 1)
        await ctx.send('Cleared {} messages'.format(amount))
        time.sleep(10)
        await ctx.channel.purge(limit=1)

    @commands.command()
    async def kick(self, ctx, member: discord.Member = None):
        if ctx.author.id != 379194922860937216 or 444857307843657739:
            await ctx.send("You are not good enough")
        else:
            if not member:
                await ctx.send("Please specify a member")
                return
            await member.kick()
            await ctx.send("{} has been kicked".format(member.mention))

    @commands.command()
    async def ban(self, ctx, member: discord.Member = None):
        if ctx.author.id != 379194922860937216 or 444857307843657739:
            await ctx.send("You are not good enough")
        else:
            if not member:
                await ctx.send("Please specify a member")
                return
            await member.ban()
            await ctx.send("{} has been banned".format(member.mention))

def setup(client):
    client.add_cog(Moderation(client))
