from utils.worlde_history import History
from utils.score import scoring

from typing import List

class ValidWords:

    def __init__(self, words_file: str = 'wordle_words.txt') -> set:

        self.valid_words: set = set()

        with open('wordle_words.txt', 'r') as ww:

            for word in ww.readlines():

                self.valid_words.add(word.removesuffix('\n'))

    def is_valid(self, word: str) -> bool:
        return word in self.valid_words
    
    def score_possible(self, history) -> list[list[str, float]]:

        possible_words = self.find_possible(history)

        word_score = []

        scorer = scoring()

        for word in possible_words:

            word_score.append(scorer.frequency_score(word))

        sorted_words = sorted(list(zip(possible_words, word_score)), key=lambda word: word[1], reverse=True)
    
        return sorted_words
    
    def find_explore_words(self, history: History) -> list[str]:
        """
        Find non valid words that can help find letters
        """

        possible: List[str] = []

        # Iterate over words
        for word in self.valid_words:

            # Iterate over chars
            for column, char in enumerate(word):

                # char is in invalid charecters do not save word
                if char in history.invalid_letters:

                    break

                if char in history.fixed_positions.values():

                    break

                if char in history.all_variables:

                    break

            else:

                possible.append(word)

        scorer = scoring()

        scores = []

        for word in possible:

            scores.append(scorer.frequency_score(word))

        sorted_words = sorted(list(zip(possible, scores)), key=lambda word: word[1], reverse=True)
    
        return sorted_words

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