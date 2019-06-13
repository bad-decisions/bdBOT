import discord
from discord.ext import commands
import time
authorised = [379194922860937216, 444857307843657739]
class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None


    @commands.command(description="Clears previous messages")
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount) + 1)
        await ctx.send('Cleared {} messages'.format(amount))
        time.sleep(5)
        await ctx.channel.purge(limit=1)


    @commands.command(description="Kicks member from server")
    async def kick(self, ctx, member: discord.Member = None):
        if ctx.author.id != 379194922860937216 or 444857307843657739:
            await ctx.send("You are not good enough")
        else:
            if not member:
                await ctx.send("Please specify a member")
                return
            await member.kick()
            await ctx.send("{} has been kicked".format(member.mention))

    @commands.command(description='Bans member from server')
    async def ban(self, ctx, member: discord.Member = None):
        if ctx.author.id != 379194922860937216 or 444857307843657739:
            await ctx.send("You are not good enough")
        else:
            if not member:
                await ctx.send("Please specify a member")
                return
            await member.ban()
            await ctx.send("{} has been banned".format(member.mention))

    @commands.command(description='Mutes member')
    async def mute(self, ctx, member: discord.Member):
        m = discord.utils.get(ctx.message.guild.roles, name= 'Mute')
        await member.add_roles(m)
        await ctx.send("{} has been muted".format(member.mention))

    @commands.command(description='Unmutes member')
    async def unmute(self, ctx, member: discord.Member):
        m = discord.utils.get(ctx.message.guild.roles, name= 'Mute')
        await member.remove_roles(m)
        await ctx.send("{} has been unmuted".format(member.mention))
            

    

def setup(client):
    client.add_cog(moderation(client))
