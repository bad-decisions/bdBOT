import discord
from discord.ext import commands
import random
class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
        
    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        authorid = message.author.id
        if message.content == 'raa' and authorid == 568078265458229248:
            print ('we got one')
            await message.channel.send("gott'em gud")

    @commands.command(description='Says something')
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(description='Greets you')
    async def hello(self, ctx):
        await ctx.message.delete()
        await ctx.send('hello')

    @commands.command(description='Predicts the future')
    async def future(self, ctx,):
        if ctx.author.id == 241161696561987585:
            await ctx.send("f**k off madoc you're future isn't getting any brighter from doing this")
        else:
            number = random.randint(1,3)
            if number == 1:
                await ctx.send("You're going to live for a bit then die for a bit")
            elif number == 2:
                await ctx.send("You're too dead to predict a future for you")
            elif number == 3:
                await ctx.send("YOU THINK YOU HAVE A FUTURE XD !?!!?!")


    @commands.command(description='Boops member')
    async def boop(self, ctx, member: discord.Member):
        await ctx.message.delete()
        embed = discord.Embed(
            colour = discord.Colour(0xb55ef1)
        )
        embed.set_author(name='Boop!')
        embed.add_field(name='{}'.format(member), value='from {} xx'.format(ctx.author))
        await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(fun(client))
    
