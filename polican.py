import re
import os
import discord
import time
import random
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from discord.ext.tasks import loop

bot = discord.Client()
seznam = []

@bot.event
async def on_ready():
    print('polican konzumovan')
    time_loop.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.find('polican') != -1:
        with open("poli-seznam.txt", "r+") as f:
            for user in message.mentions:
                if f"{str(user.id)}\n" not in f:
                    await message.channel.send(f"{user.mention} just got poličan'd!")
                    f.write(f"{user} {str(user.id)}\n")
                    print(user)
                else:
                    await message.channel.send(f"{user.mention} už poličan užívá")
            f.close

    if message.content.find('polican') != -1:
        if message.content.find('info') != -1:
            await message.add_reaction("🤔")
            mbed = discord.Embed(
                title='Chcete POLIČAN?', description='pokud chcete půlnoční poličan, napište do chatu polican pls\npokd chcete nekoho opoličanovat, napište polican @někdo', colour=discord.Color.red())
            await message.channel.send(embed=mbed)

    if message.content.find('polican') != -1:
        if message.content.find('pls') != -1:
            await message.add_reaction("😋")
            with open("poli-seznam.txt", "r+") as f:
                if f"{str(message.author.id)}\n" not in f:
                    f.write(f"{user} {str(message.author.id)}\n")
                    f.close

    if message.content.find('debug') != -1:
        if message.content.find('pls') != -1:
            await message.add_reaction("😋")
            with open("debug-seznam.txt", "r+") as f:
                for line in f:
                    user = await bot.fetch_user(re.sub('^(.* )',"", line))
                    try:
                        await user.send(file=discord.File('pulnocni_polican.jpg'))                    
                    except:
                        print(f"pohuzel pan {user} si polican zablokoval :(")
                        del(line)
            

    # OGUREC

    if message.content.find('ogurec') != -1:
        with open("gurec-seznam.txt", "r+") as f:
            for user in message.mentions:
                if f"{str(user.id)}\n" not in f:
                    await message.channel.send(f"{user.mention} just got ogurec'd!")
                    f.write(f"{user} {str(user.id)}\n")
                    print(user)
                else:
                    await message.channel.send(f"{user.mention} už ogurec užívá")
            f.close

    if message.content.find('ogurec') != -1:
        if message.content.find('info') != -1:
            await message.add_reaction("🤔")
            mbed = discord.Embed(title='Chcete SALENIJ OGUREC?',
                                 description='pokud chcete půlnoční ogurec, napište do chatu ogurec pls\npokd chcete nekoho ogurcovat, napište ogurec @někdo', colour=discord.Color.green())
            await message.channel.send(embed=mbed)

    if message.content.find('ogurec') != -1:
        if message.content.find('pls') != -1:
            await message.add_reaction("😋")
            with open("gurec-seznam.txt", "r+") as f:
                if f"{user} {str(message.author.id)}\n" not in f:
                    f.write(f"{str(message.author.id)}\n")
                    f.close


@tasks.loop(seconds=60)
async def time_loop():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    if current_time == "00:00":
        with open("poli-seznam.txt", "r+") as f:
            for line in f:
                user = await bot.fetch_user(re.sub('^(.* )',"", line))
                try:
                    await user.send(file=discord.File('pulnocni_polican.jpg'))                    
                except:
                    print(f"pohuzel pan {user} si polican zablokoval :(")
        with open("gurec-seznam.txt", "r+") as f:
            for line in f:
                user = await bot.fetch_user(re.sub('^(.* )',"", line))
                try:
                    await user.send(file=discord.File('ogurec.jpg'))                    
                except:
                    print(f"pohuzel pan {user} si ogurec zablokoval :(")
    #zacatek noveho kodu
    elif random.randrange(0, 4000) == 9:
        InTime = int((current_time).replace(':', ''))
        print(InTime)
        if (InTime > 0) and (InTime < 900):
            await sendMSG('ranni_polican.jpg')
        if (InTime > 900) and (InTime < 1100):
            await sendMSG('dopoledni_polican.jpg')
        if (InTime > 1100) and (InTime < 1300):
            await sendMSG('poledni_polican.jpg')
        if (InTime > 1300) and (InTime < 1700):
            await sendMSG('odpoledni_polican.jpg')
        if (InTime > 1700) and (InTime < 2100):
            await sendMSG('vecerni_polican.jpg')
            
async def sendMSG(policanCas):
    print("random polican expedovan")
    with open("poli-seznam.txt", "r+") as f:
            for line in f:
                user = await bot.fetch_user(re.sub('^(.* )',"", line))
                try:
                    await user.send(file=discord.File(policanCas))                    
                except:
                    print(f"pohuzel pan {user} si polican zablokoval :(")
                return
with open('token.txt') as f:
    for line in f:
        token = line

bot.run(token)
                    

