from utils.worlde_history import History

from typing import List

class ValidWords:

    def __init__(self, words_file: str = 'wordle_words.txt') -> set:

        self.valid_words: set = set()

        with open('wordle_words.txt', 'r') as ww:

            for word in ww.readlines():

                self.valid_words.add(word.removesuffix('\n'))

    def is_valid(self, word: str) -> bool:
        return word in self.valid_words
    
    def find_possible(self, history: History) -> list[str]:

        possible: List[str] = []

        # Iterate over words
        for word in self.valid_words:

            word_variables = history.all_variables.copy()

            # Iterate over chars
            for column, char in enumerate(word):

                # char is in invalid charecters do not save word
                if char in history.invalid_letters:

                    break

                # Fixed char not match
                if history.fixed_positions.get(column, char) != char:

                    break

                # Varaible char in position shouldn't be
                if char in history.variable_positons[column]:

                    break

                # If does not contain all variable chars
                word_variables.discard(char)

                if column == 4 and word_variables.__len__() != 0:

                    break


            else:
                possible.append(word)

        return possible