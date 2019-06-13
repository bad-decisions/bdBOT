#imports
import discord
from discord.ext import commands

#General Setup and Startup
client = commands.Bot(command_prefix="bd-", description='Better than CashewBot. WIP. For enquiries DM baddecisions#4002')
token = "TOKEN HERE"
client.remove_command('help')
@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user.name))
    print(client.user.id)
    game = discord.Game("in the mud")
    await client.change_presence(status=discord.Status.online, activity=game)
     
#load cogs
extensions = ['fun', 'utilities', 'moderation', 'help']
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))
    client.run(token)

