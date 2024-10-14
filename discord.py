import discord
from discord.ext import commands

stop = False
bot = commands.Bot(command_prefix="%")

@bot.event
async def on_ready():
    print(""" 
           ********************************************
           *                                          *
           *                                          *         
           *                                          * 
           *           Alarm Bot Is Enable            *
           *                                          *         
           *                                          * 
           *                                          *
           *             Author Is TPxJ               *         
           *                                          * 
           *                                          *
           *                                          *         
           *                                          * 
           ********************************************
           """)

@bot.command()
async def ping(ctx, member:discord.Member , time: int):
    print(time)
    global stop
    for i in range(1 , time+1):
        await ctx.channel.send(member.mention)
        if stop == True:
            stop = False
            break

@bot.command()
async def stop(ctx):
    global stop
    stop = True


bot.run("YourToken")