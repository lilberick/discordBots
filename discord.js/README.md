# [DISCORD.JS](https://discord.js.org/#/)
![](.img/discordjs.png)
# Instalación
```
$ npm install discord.js
```
# Hola mundo: (input=ping)(output=pong)

```js
const Discord = require('discord.js');
const client = new Discord.Client();
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});
client.login('token');
```  

![](.img/pinpong.png)
