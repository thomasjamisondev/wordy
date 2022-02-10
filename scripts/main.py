import os
from discord.ext import commands
from game_state import GameState
from words import get_words

bot = commands.Bot(command_prefix='!')
bot.words = get_words()
bot.game_state = None

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command(name = 'wordy')
async def wordy(ctx):
        bot.game_state = None
        # create new game state
        await ctx.channel.send('Game started!')
        bot.game_state = GameState(ctx.channel, bot.words)

@bot.command(name = 'guess')
async def guess_word(ctx, guess):
    if bot.game_state and not bot.game_state.game_over:
        await bot.game_state.guess_word(guess)
    else:
        await ctx.channel.send('Game is over')



TOKEN = os.environ['bot_token']
bot.run(TOKEN)
