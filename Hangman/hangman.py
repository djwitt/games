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

    def check_letter(self, letter_guess):
        """Check letter guessed, return tuple(Boolean, Output Message)"""

        check_alpha = letter_guess.isalpha()
        check_guess_length = len(letter_guess) < 2

        if check_alpha and check_guess_length:
            if letter_guess not in self.guessed:
                if letter_guess in self.picked_word:

                    self.get_indexes(letter_guess, self.picked_word)
                    msg_true = f"\n{letter_guess} is apart of the word."
                    return (True, msg_true)

                msg_false = f"\n{letter_guess} is not apart of the word."
                return (False, msg_false)

            return (False, "\nYou've already guessed that letter!")

        input_error = f"\n Your guess is not a letter or you've \
            typed too many characters"
        return (False, input_error)

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
