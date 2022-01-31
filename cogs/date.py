from time import time
from xmlrpc.client import DateTime, _datetime
import discord
import datetime
from discord.ext import commands, tasks
from datetime import date
class date_time(commands.Cog): #creates a class that inherits from commands.cog
    def __init__(self, client): #client created in main passed in
        self.client = client #lets us initialize the client object here
    
    #commands
    @commands.command() 
    async def date(self, ctx): #command called the command name
         date = datetime.datetime.now()
         dat13 = f'{date}'
         today = dat13[0:10]
         await ctx.send(f'Today date is:{today}')


def setup(client): #sets up the client object
    client.add_cog(date_time(client)) #runs a client method and passes this class i.e command into the bot object
