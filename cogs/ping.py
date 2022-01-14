import discord
from discord.ext import commands, tasks

class Default(commands.Cog): #creates a class that inherits from commands.cog
    def __init__(self, client): #client created in main passed in
        self.client = client #lets us initialize the client object here

    #events
    @commands.Cog.listener() #creates an event within this cog, its a decorator but mandatory
    async def on_ready(self): #on_ready event that triggers the console message on successful run
        print('We have logged in') #logs a ready message in the console to indicate bot is online
    
    #commands
    @commands.command() 
    async def ping(self, ctx): #command called ping
        await ctx.send('Pong!') #responds with pong when triggered


def setup(client): #sets up the client object
    client.add_cog(Default(client)) #runs a client method and passes this class i.e command into the bot object