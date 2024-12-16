import os, numpy as np

class scoring:

    def __init__(self) -> None:

        # Find the frequency of each charecter
        self.letter_frequency = self.get_frequencies()

        pass

    def frequency_score(self, word: str) -> float:
        """
        Average frequency of the words corrected for repeats

        (sum(freq) / 5) * (set(letter).len / letters.len)
        """

        sum_freq: int = 0

        for letter in [*word]:

            sum_freq += self.letter_frequency[letter]

        return (sum_freq / (5 * self.letter_frequency['total'])) * (set([*word]).__len__() / word.__len__())
    
    def get_frequencies(self, folder: str = 'stats', filepath: str = 'frequencies.txt') -> dict[str, int]:

        counts: dict[str, int] = {}

        total: int = 0

        if os.path.exists(f'{folder}/{filepath}'):

            with open(f'{folder}/{filepath}', 'r') as sv:

                for letter, num in [line.split(':') for line in sv.read().split('/n')]:

                    counts[letter] = num

                    total += num
                
            counts['total'] = total
        
            return counts

        letters = []

        with open('wordle_words.txt', 'r') as ww:
            
            for word in ww.read().split('\n'):

                letters.extend([*word])

        for letter, num in zip(*np.unique(letters, return_counts=True)):

            counts[letter] = num

            total += num

        counts['total'] = total

        return counts