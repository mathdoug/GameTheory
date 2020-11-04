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
    


class Random(Player):
    def __init__(self, money=5):
        super().__init__(money)

    
    def strategy(self):
        move = rd.choice([0, 1])
        self.my_historic_moves.append(move)
        return move
    

