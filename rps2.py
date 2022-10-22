import random
from telnetlib import GA

moves = ['ROCK', 'PAPER', 'SCISSORS']


class PlayerBase:
    def move(self):
        return 'ROCK'

    def remember(self, their_move):
        pass


class RealPlayer(PlayerBase):
    def move(self):
        while True:
            move = input(
                'PICK A MOVE: (ROCK, PAPER, SCISSORS)\n').upper()
            if move in ["QUIT", *moves]:
                return move
            else:
                print('This is an incorrect move. Please input the correct move')


class AIPlayer(PlayerBase):
    def move(self):
        return random.choice(moves)


class RepetitivePlayer(PlayerBase):
    def __init__(self) -> None:
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move


class RoundPlayer(PlayerBase):
    def __init__(self):
        self.move_index = 0

    def move(self):
        move = moves[self.move_index]
        if self.move_index == 2:
            self.move_index = 0
        else:
            self.move_index += 1
        return move


class MemoryPlayer(PlayerBase):
    def __init__(self):
        self.enemy_moves = []

    def remember(self, their_move):
        self.enemy_moves.append(their_move)

    def move(self):
        if len(self.enemy_moves) < 1:
            return random.choice(moves)
        return self.enemy_moves[-1]


class Game:
    def __init__(self, p1, p2):
        self.p1: PlayerBase = p1
        self.p2: PlayerBase = p2
        self.score = {"p1": 0, "p2": 0, "draw": 0}
        self.play = True

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player1: {move1} Player 2: {move2}")
        self.analyze_moves(move1, move2)
        self.p1.remember(move2)
        self.p2.remember(move1)
        return [move1, move2]

    def play_game(self):
        print("GAME BEGIN")
        round = 1

        while round < 1000:
            print(f"ROUND {round}:")
            if "QUIT" in self.play_round():
                break
            self.print_score()
            round += 1

        print("GAME SET AND MATCH")
        print("Final Score:")
        self.print_score()

    def p1_won(self, m1, m2):
        return (m1 == "ROCK" and m2 == "SCISSORS") \
            or (m1 == "SCISSORS" and m2 == "PAPER") \
            or (m1 == "PAPER" and m2 == "ROCK")

    def analyze_moves(self, m1, m2):
        if "QUIT" in [m1, m2]:
            return
        if m1 == m2:
            print("Draw")
            self.score["draw"] += 1
        elif (self.p1_won(m1, m2)):
            print("You won")
            self.score["p1"] += 1
        else:
            print("You lost")
            self.score["p2"] += 1

    def print_score(self):
        print(f"Player1: {self.score['p1']}")
        print(f"Player2: {self.score['p2']}")
        print(f"Draws: {self.score['draw']}")


if __name__ == '__main__':
    print("Choose which bot to play against")
    print("1: Random Bot")
    print("2: Copy Bot")
    print("3: Cycle Bot")
    print("4: Repetitive Bot")

    while True:
        user_input = input("Type 1, 2, 3, 4 or quit: ")
        if user_input == "quit" or user_input == "q":
            exit()
        if user_input == "1":
            game = Game(RealPlayer(), AIPlayer())
            break
        if user_input == "2":
            game = Game(RealPlayer(), MemoryPlayer())
            break
        if user_input == "3":
            game = Game(RealPlayer(), RoundPlayer())
            break
        if user_input == "4":
            game = Game(RealPlayer(), RepetitivePlayer())
            break

    game.play_game()
