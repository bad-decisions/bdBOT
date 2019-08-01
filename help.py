import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command(description='Displays this message')
    async def help(self, ctx, *, request=None):
        embed = discord.Embed(
            colour = ctx.author.colour
        )
        embed.set_author(name='Help', icon_url=ctx.author.avatar_url)
        if not request:
            cog_desc = ''
            for c in self.client.cogs:
                if c != "help":
                    cog_desc = cog_desc + "\n **{}**    {} Commands Available ".format(c, len(self.client.cogs[c].get_commands()))
            embed.add_field(name='Available Categories', value = cog_desc, inline = False)
        else:
            found = False
            for cog in self.client.cogs:
                if cog == request:
                    command_list = ''
                    for command in self.client.cogs[cog].get_commands():
                        if not command.hidden:
                            command_list = command_list + '**{}**    {} \n'.format(command.name, command.description)
                            found = True
                    embed.add_field(name='Commands Available', value=command_list)
            if not found:
                for cog in self.client.cogs:
                    for c in self.client.cogs[cog].get_commands():
                        if c.name == request:
                            embed.set_author(name='Help {}'.format(c.name), icon_url=ctx.author.avatar_url)
                            embed.add_field(name = c.description, value = self.client.command_prefix + c.qualified_name + ' ' + c.signature)
                            found = True
                if not found:
                    embed.add_field(name= 'You fucked up!', value= 'There is nothing matching {}, dimwit'.format(request))
        await ctx.send(embed=embed)
                     
        
def setup(client):
    client.add_cog(help(client))
