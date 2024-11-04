from hang_game import HangGame
from horror_tunnel import HorrorTunnelGame
from lotto_game import LottoGame
from slambook import Slambook
from student_data import StudentEnrollment
from tic_tac_toe import TicTacToe


class Main:

    def __init__(self):
        self.hangman = HangGame()
        self.horror_tunnel = HorrorTunnelGame()
        self.tic_tac_toe = TicTacToe()
        self.lotto_game = LottoGame()
        self.slambook = Slambook()
        self.student = StudentEnrollment()


    def main_page(self):
        print("="*40)
        print("======Welcome to My Coding Projects======")
        projects = ['[1] Hang Man Game', '[2] Horror Tunnel Game', 
                    '[3] Tic-Tac-Toe', '[4] 6/49 Lotto Game', '[5] Slambook', '[6] Enrollment System']
        print(projects)
        print("="*40)
        choose = input("Enter project to show: ")
        
        if choose == '1':
            self.hangman.main()
        elif choose == '2':
            self.horror_tunnel.start_game()
        elif choose == '3':
            self.tic_tac_toe.playGame()
        elif choose == '4':
            self.lotto_game.main()
        elif choose == '5':
            self.slambook.main()
        elif choose == '6':
            self.student.main()

if __name__ == "__main__":
    obj = Main()
    obj.main_page()