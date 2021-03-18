# Hangman


class Hangman:
    def __init__(self):
        self.game_running = True
        self.picked_word = list("KIKI")
        self.invisible_word = []
        self.guessed = []
        self.max_tries = len(self.picked_word) + 2
        self.tries = 0

    def set_invisible(self):
        """Initialize and output Underscores"""
        self.invisible_word = ["_ " for letter in self.picked_word]

    def show_letters(self):
        """Show letters guessed correctly"""
        return "".join(letter for letter in self.invisible_word)

    def update_tries(self):
        self.tries += 1

    def get_indexes(self, letter_input, word):
        """Find all instances of letter in word and grab their indexes.
        Append letters to the invisible word indexes so they can be displayed
        """

        indexed = [
            index for (index, letter) in enumerate(word) if letter == letter_input
        ]

        letter_count = indexed.count(letter_input)

        for index in indexed:
            self.invisible_word[index] = letter_input

    def check_guess_logic(self, letter):
        guess_is_alpha = letter.isalpha()
        guess_length = len(letter) < 2
        letter_not_in_word = None
        letter_in_picked_word = None

        # Default state of variable if all conditions are true
        output_msg = f"\n{letter} is apart of the word."

        # Set all conditions for each variable
        if letter not in self.guessed:
            letter_not_in_word = True
        else:
            letter_not_in_word = False

        if letter in self.picked_word:
            letter_in_picked_word = True
        else:
            letter_in_picked_word = False

        # Check all logic and if condition is not true, set output message
        if not guess_is_alpha:
            output_msg = f"\n Your guess is not a letter"
        elif not guess_length:
            output_msg = f"\n Your guess has too many characters"
        elif not letter_not_in_word:
            output_msg = f"\n You've already guessed that letter!"
        elif not letter_in_picked_word:
            output_msg = f"\n{letter} is not apart of the word."

        return (True, output_msg)

    def check_letter(self, letter_guess):
        """Check letter guessed, return tuple(Boolean, Output Message)"""
        checking_condition = self.check_guess_logic(letter_guess)
        condition_msg = checking_condition[1]

        if checking_condition[0]:
            self.get_indexes(letter_guess, self.picked_word)
            return (True, condition_msg)
        else:
            return (False, condition_msg)

    def full_word(self):
        return "".join(letter for letter in self.picked_word)

    def print_tries(self):
        return f"{self.tries} out of {play.max_tries} tries left"


# Set Game
play = Hangman()
play.set_invisible()

while play.game_running:

    print(f"\nGuess the word: {play.show_letters()}")
    user_input = input("Guess a letter: ").upper()
    check_letter = play.check_letter(user_input)

    check_tries = play.tries < play.max_tries
    check_invis_word = play.invisible_word != play.picked_word

    if check_tries and check_invis_word:

        # Check letter to receive (Boolean, Output Message)
        if check_letter[0]:
            print(check_letter[1])
            play.guessed.append(user_input)

        else:
            play.update_tries()
            play.guessed.append(user_input)
            print(check_letter[1])
            print(play.print_tries())

    elif play.invisible_word == play.picked_word:
        print(f"You won! The final word was {play.full_word()}")
        play.game_running = False

    else:
        print(f"You lost. The final word was {play.full_word()}")
        play.game_running = False
