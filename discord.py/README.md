# [DISCORD.PY](https://github.com/Rapptz/discord.py)
![](.img/discord.png)

## Instalación
```
$ pipenv install discord.py
```
## Hola Mundo: (mandas: >ping)(responde: pong)
1. `codigo.py`

	```py
	import discord
	from discord.ext import commands
	bot = commands.Bot(command_prefix='>',description='Este es un bot de ayuda')
	@bot.command()
	async def ping(ctx):
	   await ctx.send('pong')
	@bot.event
	async def on_ready():
	    print('Estoy ready papi')
	bot.run('Mi token')
	```
2. Ejecutar
	```
	$ python codigo.py
	```
3. Interactuamos con el bot  
	![](.img/ping.png)
