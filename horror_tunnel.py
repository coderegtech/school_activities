import random
import time


class CustomFunctions:
    @staticmethod
    def print_text(text):
        for letter in text:
            print(letter, end='', flush=True)
            time.sleep(0.05)
        print()
    
    @staticmethod
    def random_event(event):
        rand = random.choice(event)
        return rand


class HorrorTunnelGame(CustomFunctions):
    def __init__(self):
        self.game_over = False

    def start_game(self):
        self.intro()

    def intro(self):
        self.print_text("Welcome to the Horror Tunnel!")
        self.print_text("You are trapped in an abandoned underground tunnel.")
        self.print_text("The air is heavy, and you hear distant, unsettling noises.")
        self.print_text("You have no choice but to move forward. Do you dare to continue?\n")
        self.enter_tunnel()

    def enter_tunnel(self):
        print("1. Continue walking down the tunnel.")
        print("2. Sit down and wait for help.")
        choice = input("Choose your action (1 or 2): ")
        if choice == "1":
            self.explore_tunnel()
        elif choice == "2":
            self.wait_for_help()
        else:
            print("Invalid choice. Please choose 1 or 2.\n")
            self.enter_tunnel()

    def explore_tunnel(self):
        self.print_text("\nYou cautiously move forward. The flickering lights cast eerie shadows.")
        self.print_text("As you walk deeper, you come across a rusted metal door.\n")
        self.print_text("1. Open the door.")
        self.print_text("2. Ignore the door and keep walking.")
        choice = input("Choose your action (1 or 2): ")
        if choice == "1":
            self.random_event([self.encounter_ghost(), self.find_exit()])
        elif choice == "2":
            self.random_event([self.encounter_creature(), self.find_exit()])
        else:
            print("Invalid choice. Please choose 1 or 2.\n")
            self.explore_tunnel()

    def encounter_ghost(self):
        time.sleep(0.5)
        self.print_text("\nAs you open the door, a cold gust of wind chills your spine.")
        self.print_text("A shadowy figure appears, its hollow eyes staring into your soul.")
        print("1. Run away.")
        print("2. Confront the ghost.")
        choice = input("Choose your action (1 or 2): ")
        if choice == "1":
            self.run_away()
        elif choice == "2":
            self.confront_ghost()
        else:
            print("Invalid choice. Please choose 1 or 2.\n")
            self.encounter_ghost()

    def encounter_creature(self):
        time.sleep(0.5)
        self.print_text("\nAs you keep walking, you hear scratching sounds behind you.")
        self.print_text("You turn around and see a grotesque creature crawling toward you.\n")
        print("1. Run.")
        print("2. Try to hide.")
        choice = input("Choose your action (1 or 2): ")
        if choice == "1":
            self.run_away()
        elif choice == "2":
            self.hide_from_creature()
        else:
            print("Invalid choice. Please choose 1 or 2.\n")
            self.encounter_creature()

    def confront_ghost(self):
        time.sleep(0.5)
        self.print_text("\nYou bravely step forward and confront the ghost.")
        self.print_text("The ghost lets out a deafening scream, and suddenly, it vanishes.")
        self.print_text("You breathe a sigh of relief but wonder if it will return.\n")
        self.explore_tunnel()

    def hide_from_creature(self):
        time.sleep(0.5)
        self.print_text("\nYou quickly hide behind a pile of debris.")
        self.print_text("The creature sniffs the air, but after a while, it moves away.")
        self.print_text("You barely manage to survive, but the tunnel feels even more dangerous now.\n")
        self.explore_tunnel()

    def run_away(self):
        time.sleep(0.5)
        self.print_text("\nYou sprint back through the tunnel, heart pounding.")
        self.print_text("You manage to escape the immediate danger, but you know the horrors are still out there.")
        self.end_game()

    def find_exit(self):
        time.sleep(0.5)
        self.print_text("\nAfter wandering through the tunnel, you stumble upon an exit door.")
        self.print_text("You push it open and feel the fresh air on your face.")
        self.print_text("Congratulations! You have survived the Horror Tunnel.\n")
        self.end_game()

    def wait_for_help(self):
        time.sleep(0.5)
        self.print_text("\nYou decide to sit and wait for help.")
        self.print_text("Hours pass, but no one comes. The sounds in the tunnel grow louder, closer.")
        self.print_text("Suddenly, a shadow looms over you... It's too late to run.")
        self.end_game()

    def end_game(self):
        time.sleep(0.5)
        print("Game Over. Thanks for playing!")
        self.game_over = True
        

