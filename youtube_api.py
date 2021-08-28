import discord
from discord.ext import commands
from os import environ
from dotenv import load_dotenv
import youtube_dl

load_dotenv()
#to push
key = environ['API_KEY']
prefix='.'
players=[]

bot = commands.Bot(command_prefix=prefix)

async def connect_vc(message):
    if message.author.voice:
        channel = message.author.voice.channel
        print(channel.id)
        await channel.connect(reconnect=True)
    else:
        await message.channel.send('you aren\'t in a voice channel')


@bot.event
async def on_ready():
    game=discord.Game(name='Testing API')
    await bot.change_presence(status=discord.Status.idle,activity=game)
    print(f'Logged in as {bot.user}\nLatency: {bot.latency}')

@bot.command(name='hi')
async def on_command(message):
    await message.channel.send('Hi')

@bot.command(name='connect')
async def on_command(message):
    await connect_vc(message)

@bot.command(name='play', usage='<song name>')
async def on_command(message,song_url):
    guild = message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytdl_player(song_url)
    players[guild.id] = player
    player.start
bot.run(key)