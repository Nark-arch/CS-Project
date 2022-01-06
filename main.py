import discord 
import random 

TOKEN = '...'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.channel.name == 'gab-test-server':
        if user_message.lower() == 'bello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bai':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == 'random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return


        if user_message.lower == '!anywhere':
             await message.channel.send('This can be used anywhere!')
             return





client.run("ODkwODIyMTY4NDI0ODgyMTg2.YU1Yyw.IT_d72UIpUNLfgObDMjQ7g-YQ9c")