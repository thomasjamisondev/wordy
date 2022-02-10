import random

class GameState(object):
    def __init__(self, ctx, words):
        self.ctx = ctx
        self.word = random.choice(words).rstrip().upper()
        self.prev_guesses = []
        self.attempts_made = 0
        self.letters = 'Q W E R T Y U I O P \nA S D F G H J K L\n Z X C V B N M'

    async def guess_word(self, guess):
        guess = guess.upper()
        if len(guess) != 5:
            await self.ctx.send('Guess must be 5 letters long.')
        elif guess in self.prev_guesses:
            await self.ctx.send('You have already guessed {}'.format(guess))
            return

        o = ''
        for l1, l2 in zip(guess, self.word):
            o += '['
            if l1 == l2:
                o += l1
            else:
                o += ' '
            o += ']'
        self.attempts_made += 1
        self.prev_guesses.append(guess)
        await self.ctx.send(o)
        if self.attempts_made == 6:
            await self.ctx.send('Game Over')