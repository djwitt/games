# RPS (Rock Paper Scissors)
import random

game_running = True
word_list = ("ROCK", "PAPER", "SCISSORS")
won = 0
lost = 0
tie = 0


def new_hand():
    return random.choice(word_list)


def print_scores():
    return f"Won: {won} - Lost: {lost} - Ties: {tie}"


while game_running:

    computer_hand = new_hand()
    user_input = input("Rock, Paper, or Scissors?: ").upper()

    if user_input == computer_hand:
        print(f"It's a tie!")
        tie += 1
        print_scores()

    elif user_input == "ROCK":
        if computer_hand == "PAPER":
            print(f"\nYou lost! {computer_hand} beats {user_input}")
            lost += 1
            print(print_scores())
        else:
            print(f"\nYou've won! {user_input} beats {computer_hand}")
            won += 1
            print(print_scores())

    elif user_input == "PAPER":
        if computer_hand == "SCISSORS":
            print(f"\nYou lost! {computer_hand} beats {user_input}")
            lost += 1
            print(print_scores())
        else:
            print(f"\nYou've won! {user_input} beats {computer_hand}")
            won += 1
            print(print_scores())

    elif user_input == "SCISSORS":
        if computer_hand == "ROCK":
            print(f"\nYou lost! {computer_hand} beats {user_input}")
            lost += 1
            print(print_scores())
        else:
            print(f"\nYou've won! {user_input} beats {computer_hand}")
            won += 1
            print(print_scores())

    continue_game = input("\nPlay again? (y/n):")
    if continue_game.upper() != "Y":
        print("\n Bye!")
        game_running = False
