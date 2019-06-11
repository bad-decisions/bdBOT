import discord
from discord.ext import commands

#General Setup and Startup
client = commands.Bot(command_prefix="bd-", description='Better than CashewBot. WIP. For enquiries DM baddecisions#4002')
token = "NTg0ODE3OTIwNTU5ODA4NzA2.XPQdeA.APqN5PSmpHvwFOA0eTft8hPDauY"
@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user.name))
    print(client.user.id)
    game = discord.Game("in the mud")
    await client.change_presence(status=discord.Status.online, activity=game)

#load cogs
extensions = ['fun', 'utilities', 'moderation']
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))
    client.run(token)

#gott'em gud
@client.event
async def on_message(message):
    author = message.author
    authorid = message.author.id
    if message.content == 'raa' and authorid == 568078265458229248:
        print ('we got one')
        await message.channel.send("gott'em gud")
