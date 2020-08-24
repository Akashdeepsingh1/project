'''
if the number of alive neighbour is 3 or 5 then the current cell will 
be alive in next step even if it is dead now

'''


class GridGame:
    # def __init__(self, game=None, current_alive):
    #     self.current_alive = current_alive
    #     self.game = game

    def checkCurrentAlive(self):
        if not self.game:
            return None
        ml = len(self.game)
        nl = len(self.game[0])
        current_alive = [[0 for _ in range(nl)] for __ in range(ml)]
        for m in range(len(self.game)):
            for n in range(len(self.game[0])):
                count = 0
                for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if m+i >= 0 and m+i < len(self.game) and n+j >= 0 and n+j < (len(self.game[0])) and self.game[i+m][j+n] == 1:
                        count += 1
                current_alive[m][n] = count
        return current_alive

    def gameAfterNewMove(self, currentAlive):
        if not currentAlive:
            return None
        newState = currentAlive
        for i in range(len(currentAlive)):
            for j in range(len(currentAlive[0])):
                if currentAlive[i][j] in (3, 5):
                    newState[i][j] = 1
                else:
                    newState[i][j] = 0
        self.game = newState

    def game(self, game, moves):
        if not game or not moves:
            return 0
        self.game = game[:]

        while moves > 0:
            current_alive = self.checkCurrentAlive()
            self.gameAfterNewMove(current_alive)
            print(self.game)

            moves -= 1
        return self.game


mat = [[0, 1, 1, 0], [1, 1, 0, 0]]
obj = GridGame()
print(obj.game(mat, 2))
