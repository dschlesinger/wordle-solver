from collections import defaultdict

class History:
    # Columns 0,1,2,3,4

    # Example row break down

    """
    hangi

    H,A,N:y, G:g, I:y

    varaibles_postions = {
        3: {"N"}, # At 3 can't be N
        5: {"I"},
    }

    fixed_positions = {
        4: "G",
    }

    invalid_letters = {
        "H", "A",
    }

    """

    def __init__(self, history_file: str = 'input.txt') -> None:
        
        self.variable_positons: defaultdict[str, list[int]] = defaultdict(set)
        self.fixed_positions: dict[str, int] = {}
        self.invalid_letters: set = set()

        with open(history_file, 'r') as hf:

            # iterate over attempts
            for attempt in hf.readlines():

                # Iterate over chars in attempt
                for column, char in enumerate(attempt.split(',')):

                    # account for whitespace
                    char = char.strip()

                    # letter is not valid
                    if ':' not in char:
                        self.invalid_letters.add(char.lower())
                        continue

                    try:

                        letter, tag = char.split(':')

                    except ValueError as VE:

                        raise Exception('Invalid input chars with tag must follow format char:tag')

                    match tag:
                        
                        # There but not at location
                        case 'y':
                            
                            # Safe as defualt dict
                            self.variable_positons[column].add(letter.lower())

                        # Location is correct
                        case 'g':

                            self.fixed_positions[column] = letter.lower()

        self.all_variables = set(sum([list(v) for v in self.variable_positons.values()], []))