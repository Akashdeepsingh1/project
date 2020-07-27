'''
348. Design Tic-Tac-Toe
Medium

646

46

Add to List

Share
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

'''

from collections import defaultdict


class Classy:

    def __init__ (self):
        self.board = [["" for i in range (3)] for j in range (3)]
        self.player_move = defaultdict (list)
        self.player_symbol = {1: 'X', 2: 'O'}

    def find_victory_move (self, player):
        for i in range (3):
            for j in range (3):
                if self.board[i][j] == self.player_symbol [player]:
                    # one if to check for colmns
                    if self.board[i][0] == self.board[i][1] and self.board[i][2] == "":
                        self.player_move[player].append ([i, 2])
                    elif self.board[i][0] == self.board[i][2] and self.board[i][1] == "":
                        self.player_move[player].append ([i, 1])
                    elif self.board[i][1] == self.board[i][2] and self.board[i][0] == "":
                        self.player_move[player].append ([i, 0])
                    # one if to check for row

                    if self.board[0][j] == self.board[1][j] and self.board[2][j] == "":
                        self.player_move[player].append ([2, j])
                    elif self.board[0][j] == self.board[2][j] and self.board[1][j] == "":
                        self.player_move[player].append ([1, j])
                    elif self.board[1][j] == self.board[2][j] and self.board[0][j] == "":
                        self.player_move[player].append ([0, j])
                    # one if to check the left diagaonal
                    if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.player_symbol[player] and \
                            self.board[2][2] == "":
                        self.player_move[player].append ([2, 2])
                    elif self.board[0][0] == self.board[2][2] and self.board[0][0] == self.player_symbol[player] and \
                            self.board[1][1] == "":
                        self.player_move[player].append ([1, 1])
                    elif self.board[2][2] == self.board[1][1] and self.board[1][1] == self.player_symbol[player] and \
                            self.board[0][0] == "":
                        self.player_move[player].append ([0, 0])

                    # one if to check the right diagonal
                    if self.board[2][0] == self.board[1][1] and self.board[2][0] == self.player_symbol[player] and \
                            self.board[0][2] == "":
                        self.player_move[player].append ([0, 2])
                    elif self.board[2][0] == self.board[0][2] and self.board[2][0] == self.player_symbol[player] and \
                            self.board[1][1] == "":
                        self.player_move[player].append ([1, 1])
                    elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.player_symbol[player] and \
                            self.board[2][0] == "":
                        self.player_move[player].append ([2, 0])

    def move (self, x, y, player):
        '''
        @param x: x coordinate of the move
        @param y: y coordinate of the move
        @param player: which player is playing this move either 0 or 1
        @return player: it's 0 if no win, 1 if player 1 wins the game and 2 if player 2 wins the game
        @throws IllegalArgument - if the move is not valid

        '''
        symbol = "X"
        if player == 2:
            symbol = "0"

        victory_move = self.player_move[player]

        if [x, y] in victory_move:
            self.board[x][y] = symbol
            return player
        else:
            self.board[x][y] = symbol
            self.find_victory_move (player)
            return 0



obj = Classy()
obj.move(1,1,1)
obj.move(2,2,1)
print (obj.move (0, 0, 1))