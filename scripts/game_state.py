import random
from board import Board

class GameState(object):
    def __init__(self, ctx, words):
        self.ctx = ctx
        self.word = random.choice(words).rstrip().upper()
        print(self.word)
        self.guesses = []
        self.board = Board(self.word)
        self.letters = 'Q W E R T Y U I O P \nA S D F G H J K L\n Z X C V B N M'
        self.game_over = False

    async def guess_word(self, guess):
        """Core guess method"""
        guess = guess.upper()
        if self.game_over:
            await self.ctx.send('Game is over. Enter !wordy to start a new game')
            return
        if not await self._valid_guess(guess):
            return

        self.guesses.append(guess)

        self.board.update(guess)

        board = self.board.output()
        board_string = board[0]
        is_game_complete = board[1]

        await self.ctx.send(board_string)
        if is_game_complete:
            self.game_over = True

    
    async def _valid_guess(self, guess):
        """Check if guess is valid"""
        if len(guess) != 5:
            await self.ctx.send('Guess must be 5 letters long.')
            return False
        elif guess in self.guesses:
            await self.ctx.send('You have already guessed {}'.format(guess))
            return False
        return True
