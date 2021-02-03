# Mis Cuentas: 
Mostrar usuarios y password de mis cuentas
## Ejecución
1. `codigo.py`

	```py
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
	```
2. `cuentas.csv`

	```
	"GMAIL","migmail.com@gmail.com","password1"
	"PORKBUN","midominio.com@gmail.com","password2"
	"GITHUB","migithub.com@gmail.com","password3"
	"AWS","miaws.com@gmail.com","password4"
	```
3. Ejecución
	```
	$ python codigo.py
	```
