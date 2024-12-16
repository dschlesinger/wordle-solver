from utils.valid_words import ValidWords
from utils.worlde_history import History

# Init wordle valid words set
VW = ValidWords()

H = History()

print(VW.find_possible(H), sep='\n')