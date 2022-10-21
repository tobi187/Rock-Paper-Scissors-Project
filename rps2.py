import random

moves = ['ROCK', 'PAPER', 'SCISSORS']


class PlayerBase:
    def move(self):
        return 'ROCK'

    def remember(self, their_move):
        pass

    def beats(one, two):
        return ((one == 'ROCK' and two == 'SCISSORS') or
                (one == 'SCISSORS' and two == 'PAPER') or
                (one == 'PAPER' and two == 'ROCK'))


class RealPlayer(PlayerBase):
    def move(self):
        while True:
            move = input(
                'PICK A MOVE: (ROCK, PAPER, SCISSORS \n').upper()
            if move in moves:
                return move
            else:
                print('This is an incorrect move. Please input the correct move')


class AIPlayer(PlayerBase):
    def move(self):
        return random.choice(self.moves)


class RepetitivePlayer(PlayerBase):
    def move(self):
        return 'ROCK'


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

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player1: {move1} Player 2: {move2}")
        self.p1.remember(move2)
        self.p2.remember(move1)

    def play_game(self):
        print("GAME BEGIN")
        for round in range(3):
            print(f"ROUND {round + 1}:")
            self.play_round()
        print("GAME SET AND MATCH")
        self.p1.score = 0
        self.p2.score = 0

    def sequences(self):

        user_input = input('How many sequences would you like to play')
        try:
            rounds = int(user_input)
        except ValueError:
            print('This is not a legitmate number')

        if self.number_sequences.lower() == 'exit':
            exit()


if __name__ == '__main__':
    game = Game(RealPlayer(), MemoryPlayer())
    game.play_game()
