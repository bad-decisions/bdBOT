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
    async def offline(self,ctx):
        if ctx.author.id == 379194922860937216:
            await ctx.message.delete()
            await ctx.send("baddecisionsBOT offline. До свидания")
        else:
            await ctx.send("you are not authorised to use this command")

    @commands.command()
    async def online(self,ctx):
        if ctx.author.id == 379194922860937216:
            await ctx.message.delete()
            await ctx.send("baddecisionsBOT online! Привет")
        else:
            await ctx.send("you are not authorised to use this command")
    
def setup(client):
    client.add_cog(Moderation(client))
