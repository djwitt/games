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

    def check_letter(self, letter_guess):
        """Check letter guessed, return tuple(Boolean, Output Message)"""

        if letter_guess.isalpha() and len(letter_guess) < 2:

            # If the letter has not already been guessed
            if letter_guess not in self.guessed:

                # If the letter is in the word
                if letter_guess in self.picked_word:

                    # Find all indexes of that letter
                    indexed = [
                        index
                        for (index, letter) in enumerate(self.picked_word)
                        if letter == letter_guess
                    ]

                    # Find out how many indexes there are
                    letter_count = indexed.count(letter_guess)

                    # Push letters into index of the invisble word.
                    for index in indexed:
                        self.invisible_word[index] = letter_guess

                    # Return Boolean and Message if True
                    msg_true = f"\n{letter_guess} is apart of the word."
                    return (True, msg_true)

                else:
                    msg_false = f"\n{letter_guess} is not apart of the word."
                    return (False, msg_false)
            else:
                return (False, "\nYou've already guessed that letter!")

        else:
            input_error = f"\n Your guess needs to be a letter or you've typed too many characters"
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

    if play.tries < play.max_tries and play.invisible_word != play.picked_word:

        # Check letter to receive (Boolean, Output Message)
        if check_letter[0]:
            print(check_letter[1])

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
