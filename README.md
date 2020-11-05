# GameTheory

This is a simulation of a game theory in order to analyse different strategies and see their evolution in the time.

## Environment

- There is P players and each of them begins with M money. 
- At each step, the players are randomly divided into N/2 pairs. If N is odd, it remains one player and we consider that he doesn't participate on the step.
- For each pair of players, the rules are :
    - Each player must pay 1 money;
    - If both cooperates, each of them earns 2 money.
    - If one cooperates and the other cheats, the one who has cheated earns 3 money;
    - If both cheats, nothing happens.
- If the player has 0 money, he dies.

## Strategies

We are going to consider the following strategies for the players.
- **Random:** he randomly cooperates.
- **Cheater:** he always cheats.
- **Cooperator:** he always cooperates.
- **Rancorous:** he always cooperates. The first time someone cheats him, he will always cheat this player.
- **Righteous:** If the other player cooperated in the last step they played together, he cooperates. Otherwise, he cheats. We have to take into account the first move :
    1. He cheats
    2. He cooperates
    3. He randomly choose