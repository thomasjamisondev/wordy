from enum import Enum

class LetterStatus(Enum):
    CORRECT = 1
    INCORRECT = 2
    MISPLACED = 3

class Board(object):
    def __init__(self, word):
        self.word = word
        self.board_guesses = {}

    def update(self, guess):
        self.board_guesses[guess] = []
        corrects_and_misplaceds_seen = [] # keep record to not show misplaced letters more than once
        for l1, l2 in zip(guess, self.word):
            if l1 == l2:
                self.board_guesses[guess].append(LetterStatus.CORRECT)
                corrects_and_misplaceds_seen.append(l1)
            elif l1 in self.word and l1 != l2 and l1 not in corrects_and_misplaceds_seen:
                self.board_guesses[guess].append(LetterStatus.MISPLACED)
                corrects_and_misplaceds_seen.append(l1)
            else:
                self.board_guesses[guess].append(LetterStatus.INCORRECT)

    def output(self):
        """Return board and if game complete"""
        output = ''
        is_game_complete = False
        for board_guess, letter_statuses in self.board_guesses.items():
            if LetterStatus.INCORRECT not in letter_statuses and LetterStatus.MISPLACED not in letter_statuses:
                is_game_complete = True
            for letter, letter_status in zip(board_guess, letter_statuses):
                if letter_status == LetterStatus.CORRECT:
                    output += '[**{}**]'.format(letter)
                elif letter_status == LetterStatus.MISPLACED:
                    output += '[{}]'.format(letter)    
                else:
                    output += '[ ]'
            output += '\n'
            
        blank_rows = 6 - len(self.board_guesses)
        for x in range(blank_rows):
            output += '[  ][  ][  ][  ][  ]\n'
        return output, is_game_complete


