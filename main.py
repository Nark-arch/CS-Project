import contextlib
from inspect import Arguments
import discord
import os
from discord import Message
from discord import member
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from discord.flags import Intents
TOKEN = '...'

intents = discord.Intents.default() #discord intents for technical reasons permission access to portions of the api etc.
intents.members = True
client = commands.Bot(command_prefix = '.', Intents = intents)#set bot prefix

for filename in os.listdir('./cogs'): #returns list of filenames in the cogs folder
    if filename.endswith('.py'): #checks if the files end with .py
        client.load_extension(f'cogs.{filename[:-3]}') #loads the filename after minusing the last 3 characters using splice i.e removes .py

#loads command
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension} <@{ctx.author.id}>')

#reloads command
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension} <@{ctx.author.id}>')

#unloads command
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension} <@{ctx.author.id}>')

client.run("ODkwODIyMTY4NDI0ODgyMTg2.YU1Yyw.IT_d72UIpUNLfgObDMjQ7g-YQ9c") #main token of the bot, is basically our password to discords api