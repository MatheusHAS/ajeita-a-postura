import discord
import asyncio
import random
import os

TOKENDISCORD = str(os.environ.get('TOKENDISCORD'));
client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='380827346082594817') #discordia ID
    while not client.is_closed:
        members = []
        for server in client.servers:
            for member in server.members:
                if str(member.status) == "online" or str(member.status) == "dnd": 
                    members.append(member)
        randmember = random.choice(members)
        print(randmember.id)
        messages = ["Salve {0}, e a postura, como tá?",
                    "Ajeita essa postura {0}.",
                    "Já vi várias coisas tortas, mas essa postura do {0}, é novidade."]
        await client.send_message(channel, random.choice(messages).format(randmember.mention))
        await asyncio.sleep(3600)

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Bem vindo {0.mention} ao {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logado como')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.loop.create_task(my_background_task())
client.run(TOKENDISCORD);
