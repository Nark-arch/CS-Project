from multiprocessing.sharedctypes import Value
from sqlite3 import Timestamp
import discord
import datetime
from discord.ext import commands, tasks
from googlesearch import search 
from datetime import date
from urllib.parse import urlparse

class google(commands.Cog): #creates a class that inherits from commands.cog
    def __init__(self, client): #client created in main passed in
        self.client = client #lets us initialize the client object here
    
    #commands
    @commands.command() 
    async def google(self, ctx, query):

        query = ctx.message.content
        resultlist=[ ]
        domainlist=[ ]

        await ctx.channel.send(f"Here are the links related to your query <@{ctx.author.id}> !")
        async with ctx.typing():
            for j in search(query, tld="co.in", num=6, stop=6, pause=0, safe="on"): 
                resultlist.append(j)
                
        def domainlis():
                    for os in range(5):
                        p = urlparse(f'{resultlist[os]}').netloc
                        domainlist.append(p)
        domainlis()

        embeded = discord.Embed(title="Search Results", description=f"Search completed for {ctx.message.content}")
        embeded.set_thumbnail(url=ctx.author.avatar_url)
        embeded.add_field(name="Result 1", value=f"[{domainlist[0]}]({resultlist[0]})")  
        embeded.add_field(name="Result 2", value=f"[{domainlist[1]}]({resultlist[1]})")
        embeded.add_field(name="Result 3", value=f"[{domainlist[2]}]({resultlist[2]})")
        embeded.add_field(name="Result 4", value=f"[{domainlist[3]}]({resultlist[3]})")
        embeded.add_field(name="Result 5", value=f"[{domainlist[4]}]({resultlist[4]})")
        embeded.add_field(name="Result 6", value=f"[{domainlist[4]}]({resultlist[5]})")

        await ctx.send(embed=embeded)
        #await ctx.send(f"Search complete{resultlist[0]} {resultlist[1]} {resultlist[2]}")


def setup(client): #sets up the client object
    client.add_cog(google(client)) #runs a client method and passes this class i.e command into the bot object
