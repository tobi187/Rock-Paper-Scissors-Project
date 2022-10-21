import random

moves = ['ROCK', 'PAPER', 'SCISSORS']

class Player:
    def move(self):
        return 'ROCK'

    def learn(self, my_move, their_move):
        pass

    def beats(one, two):
        return ((one == 'ROCK' and two =='SCISSORS') or
        (one == 'SCISSORS' and two == 'PAPER') or
        (one == 'PAPER' and two == 'ROCK'))

class RealPlayer(Player):
    def __init__(self):
        super(). __init__()
        user.input = 'Real Player'

    def move(self):
        while True:
            move = user_input(
            'PICK A MOVE: (ROCK, PAPER, SCISSORS \n').lower()
            if move in moves:
                return move
            else:
                print('This is an incorrect move. Please input the correct move')
class AIPlayer(Player):
    def move(self):
        return random.choice(self.moves)

class RepetitivePlayer(Player):
    def move(self):
        return 'ROCK'

class RoundPlayer(Player):
    def move(self):
        if self.user_input is None:
            return random.choice(moves)

class MemoryPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.human_player_memory = {}
        for move in moves:
            self.human_player_memory[move] = 0

    def move(self):
        if p1_move =='ROCK':
            return 'PAPER'
        if p1_move =='SCISSORS':
            return 'ROCK'
        if p1_move == 'PAPER':
            return 'rock'

    def learn(self, my_move, their_move):
        self.human_player_memory[their_move] += 1

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player1: {move1} Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("GAME BEGIN")
        for round in range(3):
            print(f"ROUND {round}:")
            self.play_round()
        print("GAME SET AND MATCH")
        self.p1.score = 0
        self.p2.score = 0

    def sequences(self):

        user_input= input('How many sequences would you like to play')
        try:
        rounds = int(user_input)
        except ValueError:
        print('This is not a legitmate number')

    if self.number_sequences.lower() == 'exit':
            exit()

    if __name__ == '__main__':
        game = Game(Player(), Player())
        game.play_game()
