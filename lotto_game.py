import random


class LottoGame:

    def __init__(self):
        self.userLottoNumbers = []
        self.lottoCombination = []

    def main(self):
        print("===Welcome to 6/49 Lotto===")
        for i in range(6):
            userInput = input(f"number {i + 1}: ")
            if userInput > str(49):
                print("Number cannot be exceed to 49")
                break
            # number must be 1 to 49 only
            self.userLottoNumbers.append(int(userInput))
        
        print("============================")
        print("Your Lotto Numbers: ", self.userLottoNumbers)
        self.checkWinner(self.userLottoNumbers, self.lottoCombination)
        self.displayWinnerCombination()
    
    def displayWinnerCombination(self):
        print("============================")
        print(f"6/49 Lotto Winner Combination Number: {self.lottoCombination}")

    def randomLottoNumbers(self):
        for j in range(6):
            rand = random.randint(1, 49)
            self.lottoCombination.append(rand)

    def checkWinner(self, userNumber, lottoCombi):
        # lottoCombination
        self.randomLottoNumbers()
        # check user numbers if it is equal in lotto combination
        for j in range(6):
            if userNumber[j] == lottoCombi[j]:
                print("============================")
                print("You have won from the 6/49 lotto worth of 5 million pesos!!!")
                break
            else:
                print("============================")
                print("Sorry please try again next life")
                break


