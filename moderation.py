import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import has_permissions, CheckFailure
authorised = [379194922860937216, 444857307843657739]
class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
      
    @commands.command(description="Clears previous messages")
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount) + 1)
        await ctx.send('Cleared {} messages'.format(amount))
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1)

    @commands.command(description="Kicks member from server")
    @has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None):
            if not member:
                await ctx.send("Please specify a member")
                return
            await member.kick()
            await ctx.send("{} has been kicked".format(member.mention))

    @commands.command(description='Bans member from server')
    @has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member = None):
            if not member:
                await ctx.send("Please specify a member")
                return
            await member.ban()
            await ctx.send("{} has been banned".format(member.mention))

    @commands.command(description='Mutes member')
    @has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, time, units, *, reason):
            m = discord.utils.get(ctx.message.guild.roles, name= 'Mute')
            await member.add_roles(m)
            embed = discord.Embed(
                colour = ctx.author.colour
            )
            embed.set_author(name='{} was muted for {} {}'.format(member, time, units), icon_url=ctx.author.avatar_url)
            embed.add_field(name='Reason:', value = reason)
            await ctx.send(embed=embed)
            if units == "minute" or units == "minutes":
                await asyncio.sleep(int(time) * 60)
            elif units == "hour" or units == "hours":
                await asyncio.sleep(int(time) * 3600)
            await member.remove_roles(m)
            embed = discord.Embed(
                colour = ctx.author.colour
            )
            embed.set_author(name="{} has been unmuted".format(member), icon_url=ctx.author.avatar_url)
            embed.add_field(name='Reason:', value = "Mute of {} {} expired".format(time, units))
            await ctx.send(embed=embed)
           

    @commands.command(description='Unmutes member')
    @has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member, *, reason):
            m = discord.utils.get(ctx.message.guild.roles, name= 'Mute')
            await member.remove_roles(m)
            embed = discord.Embed(
                colour = ctx.author.colour
            )
            embed.set_author(name="{} has been unmuted".format(member), icon_url=ctx.author.avatar_url)
            embed.add_field(name='Reason:', value = reason)
            await ctx.send(embed=embed)
        
                
    @commands.command(description="Sets a channel for delete logs")
    @has_permissions(administrator=True)
    async def set_deletechannel(self, ctx):
        serverid = ctx.guild.id
        channelid = ctx.channel.id
        file_s = open("serverid.txt", 'a')
        file_c = open("channelid.txt", 'a')
        await ctx.send("**Channel {}** for **Server {}** set as delete logs".format(channelid, serverid))
        file_s.write("{} ".format(serverid))
        file_c.write("{} ".format(channelid))
   
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        filed = []
        file = (open("nodel.txt", 'r')).read()
        filed = file.split(',')
        i = 0
        n = 0
        cid = message.channel.id
        for i in range(len(filed) - 1):
            if int(cid) - int(filed[i]) == 0:
                n += 1
                i += 1
            else:
                i += 1
        if n == 0:
            file_s = open("serverid.txt", 'r')
            files = file_s.read()
            serverlist = []
            serverlist = files.split(' ')
            file_c = open("channelid.txt", 'r')
            filec = file_c.read()
            channellist = []
            channellist = filec.split(' ')
            server = message.guild.id
            i = 0
            for i in range(len(serverlist)):
                if str(server) == str(serverlist[i]):
                    channel = self.client.get_channel(int(channellist[i]))
                    await channel.send("**{}** in **{}** >> {}".format(message.author.name, message.channel.name, message.clean_content))
                else:
                    i += 1
            
    @commands.command(description="Sets annoucement channel")
    @has_permissions(administrator=True)
    async def set_announcement(self, ctx):
        channelid = ctx.channel.id
        serverid = ctx.guild.id
        file = open("announcements.txt", 'a')
        servers = open("ancservers.txt", 'a')
        await ctx.send("baddecision announcements set **on** for channel {}".format(channelid))
        file.write("{} ".format(channelid))
        servers.write("{} ".format(serverid))

    @commands.command(description="For dev use only. Makes an annoucement")
    async def upd(self, ctx, *, announcement):
        if ctx.author.id == 379194922860937216:
            file = []
            file = ((open("announcements.txt", 'r')).read()).split(' ')
            i = 0
            for i in range(len(file) - 1):
                channel = self.client.get_channel(int(file[i]))
                embed = discord.Embed(
                    colour = discord.Color(0xffca00)
                )
                embed.set_author(name="baddecisionsBOT Announcement", icon_url=ctx.author.avatar_url)
                embed.add_field(name='Update:', value = announcement)
                await channel.send(embed=embed)
                i += 1
            await ctx.send("Annoucement made")
        else:
            ctx.send("You're not my owner")

    @commands.command(description="Makes an annoucement")
    @has_permissions(administrator=True)
    async def anc(self, ctx, serverid, *, announcement):
            servers = []
            file = []
            file = ((open("announcements.txt", 'r')).read()).split(' ')
            servers = ((open("ancservers.txt", 'r')).read()).split(' ')
            i = 0
            for i in range(len(servers)):
                if serverid == servers[i]:
                    channel = self.client.get_channel(int(file[i]))
                    embed = discord.Embed(
                        colour = discord.Color(0xffca00)
                    )
                    embed.set_author(name="baddecisionsBOT Announcement", icon_url=ctx.author.avatar_url)
                    embed.add_field(name="From {}".format(ctx.author), value = announcement)
                    await channel.send(embed=embed)
                else:
                    i += 1
            channel = self.client.get_channel(int(file[1]))
            await channel.send(embed=embed)
            await ctx.send("Annoucement made")

    @commands.command(description="Sets a channel to be exclded from delete logs")
    @has_permissions(administrator=True)
    async def no_delete(self, ctx):
        file = open("nodel.txt", 'a')
        cid = ctx.channel.id
        file.write("{},".format(cid))
        await ctx.send("Channel {} excluded from delete logs".format(cid))

    @commands.command(description="Turns delete logs on for the channel")
    @has_permissions(administrator=True)
    async def yes_delete(self, ctx):
        filer = []
        filer = ((open("nodel.txt", 'r')).read()).split(',')
        cid = ctx.channel.id
        i = 0
        aha = ''
        for i in range(len(filer)-1):
            if int(cid) - int(filer[i]) == 0:
                del filer[i]
                break
            else:
                i += 1
        i = 0
        for i in range(len(filer)):
            if filer[i] != '':
                aha = aha + filer[i] + ','
                i += 1
            elif filer[i] == '':
                aha = aha + filer[i]
                i += 1
        file = open("nodel.txt", 'w')
        file.write(aha)
        await ctx.send("Channel {} is included in delete logs".format(cid))
            
        
            
def setup(client):
    client.add_cog(moderation(client))
