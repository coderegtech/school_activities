import random


class HangGame:

    def hangStage(self, stage):
        if stage == 1:
            print("""
                ________
                |      |
                O      |
                       |
                       |
                       |
            """)
        elif stage == 2:
            print("""
                ________
                |      |
                O      |
                |      |
                       |
                       |
            """)
        elif stage == 3:
            print("""
                ________
                |      |
                O      |
                |      |
               /       |
                       |
            """)
        elif stage == 4:
            print("""
                ________
                |      |
                O      |
                |      |
               / \     |
                       |
            """)
        elif stage == 5:
            print("""
                ________
                |      |
                O      |
               /|      |
               / \     |
                       |
            """)
        elif stage == 6:
            print("""
                ________
                |      |
                O      |
               /|\     |
               / \     |
                       |
            """)

    def randomWords(self):
        guessedWords = ['python','person','love', 'bird', 'cat', 'kitten']
        randomWord = random.choice(guessedWords)
        guessWord = []

        for char in randomWord:
            guessWord.append(char)

        return guessWord

    def main(self):
        guessWord = self.randomWords()

        attempts = 6
        userGuessed = ['_'] * len(guessWord)
        guessedLetters = set()
        playAgain = "n"
        print("="*50)
        print("=========== Welcome to Hang Man Game ===========")
        print("="*50)
        while playAgain == "n":
            
            print("Current word: ", ' '.join(userGuessed))
            print("="*50)
            user = input("Enter a guess letter: ").lower()
            print("="*50)
        
            if user in guessedLetters:
                print("You already guessed that letter.")
                continue
        
            guessedLetters.add(user)
        
            if user in guessWord:
                for i in range(len(guessWord)):
                    if guessWord[i] == user:
                        userGuessed[i] = user
                if '_' not in userGuessed:
                    print("Congratulations! You guessed the word:", ''.join(guessWord))
                    break
            else:
                attempts -= 1
                print("="*50)
                print(f"Wrong guess! You have {attempts} attempts left.")
                self.hangStage(6 - attempts)
        
            if attempts == 0:
                print("Game over! You've been hanged.")
                print("The word was:", ''.join(guessWord))
                print("="*50)
                playAgain = input("Do you want to play again?(y/n)")
