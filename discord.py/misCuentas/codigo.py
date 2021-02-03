import discord
import csv
import time
from discord.ext import commands
bot = commands.Bot(command_prefix='>',description='Este es un bot de ayuda')
@bot.command()
async def cuentas(ctx):
    with open('cuentas.csv', mode='r') as infile:
        reader = csv.reader(infile)
        included_cols = [*range(0,3)]
        msg=[]
        msg.append(await ctx.send('ESTO SERA ELIMINADO EN 10 SEGUNDOS...'))
        for row in reader:
            content = list(row[i] for i in included_cols)
            msg.append(await ctx.send("**"+str(content[0])+"** : "+str(content[1])+"        "+str(content[2])))
        time.sleep(10)
        for t in range(len(msg)):
            await msg[t].delete()
@bot.event
async def on_ready():
    print('Estoy ready papi')
bot.run('miToken')

