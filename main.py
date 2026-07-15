"""
main.py

Entry point for the Blackjack application.

This module displays the main menu, allows the player
to view the game rules, learn about the project,
or start a new Blackjack game.

Author: Johnathan Casanova
Language: Python 3
Version: 1.0.0
"""

from game import Game


MENU_WIDTH = 40
SEPARATOR = "=" * MENU_WIDTH
RETURN_MESSAGE = "\nPress Enter to return to the main menu..."
VALID_CHOICES = {"1", "2", "3", "4"}
VERSION = "1.0.0"


class BlackjackApp:

    def print_header(self, title: str) -> None:
        print(f"\n{SEPARATOR}")
        print(title.center(MENU_WIDTH))
        print(SEPARATOR)

    def start_game(self) -> None:
        game = Game()
        game.play_game()

    def pause(self) -> None:
        input(RETURN_MESSAGE)
        print()

    def display_menu(self) -> None:
        self.print_header("BLACKJACK IN PYTHON")
        print("Welcome to Blackjack in Python!".center(MENU_WIDTH))
        print("Created by Johnathan Casanova".center(MENU_WIDTH))
        print("\nMenu".center(MENU_WIDTH))
        print()
        print("1. Play Game".center(MENU_WIDTH))
        print("2. Game Rules".center(MENU_WIDTH))
        print("3. About".center(MENU_WIDTH))
        print("4. Exit".center(MENU_WIDTH))

    def show_rules(self) -> None:
        self.print_header("BLACKJACK RULES")
        print("""
1. The goal of the game is to get as close to 21 as possible without going over.

2. Number cards are worth their face value.
   Face cards are worth 10.
   Aces can count as 1 or 11.

3. Both the player and dealer start with two cards.
   The player sees both cards.
   Only one dealer card is visible.

4. The player may Hit or Stand.

5. Going over 21 is a Bust.

6. The dealer must hit until reaching 17.

7. Closest to 21 wins.

8. Equal scores result in a Push.
""")
        self.pause()

    def show_about(self) -> None:
        self.print_header("ABOUT PROJECT")
        print(f"{'Project:':12} Blackjack-in-Python")
        print(f"{'Developer:':12} Johnathan Casanova")
        print(f"{'Language:':12} Python 3")
        print(f"{'Version:':12} {VERSION}")
        print("""
Development Tools:

Visual Studio Code (VS Code)
Python 3.11
Git
GitHub
""")
        print("""
Features:             
- Object-Oriented Programming
- Classes and Objects
- Game Control
- Game Menu
- Game Logic
- Dealer AI
- Multiple Rounds
- Score Calculation
- Automatic Ace Value Adjustment
- User Input Validation
- Functions and Methods
- Inheritance
- Encapsulation
- Type Hints
- Random Module
""")
        print("""
Purpose:

The purpose of this project is to showcase my technical skills
and understanding of the Python programming language, as well as
my ability to implement object-oriented programming concepts.

This project demonstrates my proficiency in creating a functional
and interactive game while highlighting my attention to detail
and commitment to delivering a polished final product.
""")
        self.pause()

    def main_menu(self) -> None:

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ").strip()

            if choice not in VALID_CHOICES:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            actions = {
                "1": self.start_game,
                "2": self.show_rules,
                "3": self.show_about,
            }

            if choice == "4":
                print()
                print("Thank you for playing!")
                print("Goodbye!")
                break

            actions[choice]()

if __name__ == "__main__":
    app = BlackjackApp()
    app.main_menu()