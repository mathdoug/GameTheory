import random as rd

class Player:
    """
    Parent Class of all kind of players.
    """
    def __init__(self, money=5):
        self.money = money
        self.alive = True
        self.memory = None
        self.historic_opponent_moves = []
        self.my_historic_moves = []
    
    
    def is_alive(self):
        if self.money == 0:
            self.alive = False
        return self.alive


    def create_memory(self, n_players):
        self.memory = []
        for i in range(n_players):
            self.memory.append([])
        
    
    def update_memory(self, player, move):
        self.memory[player].append(move)
        self.historic_opponent_moves.append(move)
    

    def is_first_move(self, opponent_player):
        if len(self.memory[opponent_player]) > 0:
            return False
        return True
    


class Random(Player):  
    def move(self, opponent_player=None):
        move = rd.choice([0, 1])
        self.my_historic_moves.append(move)
        return move
    

class Cheater(Player):
    def move(self, opponent_player=None):
        move = 0
        self.my_historic_moves.append(move)
        return move


class Cooperator(Player):
    def move(self, opponent_player=None):
        move = 1
        self.my_historic_moves.append(move)
        return move


class Rancorous(Player):
    def move(self, opponent_player):
        move = 1
        if (not self.is_first_move(opponent_player) > 0) and (self.memory[opponent_player][-1] == 0):
            move = 0
        self.my_historic_moves.append(move)
        return move


class Righteous(Player):
    def __init__(self, kind, money=5):
        super().__init__(money)
        self.kind = kind

    
    def move(self, opponent_player):
        if not self.is_first_move(opponent_player):
            move = self.memory[opponent_player][-1]
        # It is the first move
        elif self.kind == 1:
            move = 0
        elif self.kind == 2:
            move = 1
        elif self.kind == 3:
            move = rd.choice([0, 1])
        
        self.my_historic_moves.append(move)
        return move



if __name__ == "__main__":
    p = Random(money=5)
    print("## Random player")
    print(f"   Money : {p.money}")
    print(f"   Alive : {p.alive}")
    print(f"Strategy : {p.move()}")
    print(f"Historic : {p.my_historic_moves}")
    print(f"Strategy : {p.move()}")
    print(f"Historic : {p.my_historic_moves}")
    print(f"Strategy : {p.move()}")
    print(f"Historic : {p.my_historic_moves}")