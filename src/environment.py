from player import Random, Cheater, Cooperator, Rancorous, Righteous
import random as rd

class MyEnv:
    """
    Class responsible for the environment of the game. It will create the players and 
    divide the players in pairs for each round.
    """
    def __init__(self, n_each_player=5, initial_money=5):
        """
        n_each_player: (int) quantity of each player to be created
        """
        self.n_each_player = n_each_player
        self.players = []
        self.create_players(initial_money)
    

    def create_players(self, initial_money):
        # Five players of each of them
        for i in range(5):
            self.players.append(Random(money=initial_money))
            self.players.append(Cheater(money=initial_money))
            self.players.append(Cooperator(money=initial_money))
            self.players.append(Rancorous(money=initial_money))
            self.players.append(Righteous(1, money=initial_money))
            self.players.append(Righteous(2, money=initial_money))
            self.players.append(Righteous(3, money=initial_money))


    def who_alive(self):
        return [i for i in range(len(self.players)) if self.players[i].is_alive()]
    

    def n_alives(self):
        return len(self.who_alive())
    
    
    def match_pairs(self):
        alive_players = self.who_alive()
        pairs = []
        while len(alive_players) > 1:
            first = rd.choice(alive_players)
            alive_players.remove(first)
            second = rd.choice(alive_players)
            alive_players.remove(second)
            pairs.append((first, second))
        return pairs
    

    def round(self, pairs):
        for first, second in pairs:
            move1 = first.move(second)
            move2 = second.move(first)
