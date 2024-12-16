from utils.valid_words import ValidWords
from utils.worlde_history import History

# Init wordle valid words set
VW = ValidWords()

H = History()

print('Explore', *VW.find_explore_words(H)[:5], sep='\n')

print('Possible', *[v[0] for v in VW.score_possible(H)[0:20]], sep='\n')