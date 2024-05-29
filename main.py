import discord
import asyncio
import random 
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Conectado como {self.user} (ID: {self.user.id})')

    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('hola'):
            await message.channel.send("Holi")
        if message.content.startswith('chao'):
            await message.channel.send("\\\U0001f642")
        if message.content.startswith('$me das unas contraseña'):
            await message.channel.send("claro tu contraseña es: " +gen_pass(10))
        if message.content.startswith('$help'):
            await message.channel.send("Aqui te proporciono la lista de comandos hasta ahora:")
            await message.channel.send("guess: Para que juegues con el bot a adivinar un numero del 1 al 10")
            await message.channel.send("coin: el bot tirara una moneda ya siendo cara o cruz")
            await message.channel.send("hola: te devuelve el saludo")
            await message.channel.send("$me das una contraseña: te proporciona una contraseña de 10 digitos")
            await message.channel.send("chao: el bot te esperara para recibir mas comandos con felicidad")
        # No me funcionaba el import asi que traslade la funcion aca     
        def flipcoin():
            flip = random.randint(0,2)
            if flip == 0:
                return "Cara"
            else: 
                return "Cruz"
        if message.content.startswith("coin"):
            await message.channel.send(flipcoin())
        if message.content.startswith('guess'):
            await message.channel.send('Adivina un numero entre el 1 y 10.')
        
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                 guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'losiento, tomo mucho tiempor pero la respuesta era {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('La has acertado!!!!!')
            else:
                await message.channel.send(f'Oops. Era {answer}.')
     
client = MyClient(intents=intents)
client.run("Mi token") 
