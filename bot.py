import subprocess
import os
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello!' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")

    if '*tts' in ctx.content.lower():
        arg = ctx.content
        arg = arg[4:]
        subprocess.call(['./speech.sh', arg])

    if 'no u' in ctx.content.lower():
        await ctx.channel.send(f"No u, @{ctx.author.name}!")

@bot.command(name='bruh')
async def bruh(ctx):
    subprocess.call(['./speech.sh', 'bruh'])
    await ctx.channel.send('Bruh!')

@bot.command(name='Viper')
async def Viper(ctx):
    await ctx.channel.send('Poop dick?')

@bot.command(name='Chop')
async def Chop(ctx):
    await ctx.channel.send('Russian Troll?')

@bot.command(name='EchineZi')
async def EchineZi(ctx):
    await ctx.channel.send('Hackerman!')

@bot.command(name='adipio')
async def adipio(ctx):
    await ctx.channel.send('ANT!')

if __name__ == "__main__":
    bot.run()
