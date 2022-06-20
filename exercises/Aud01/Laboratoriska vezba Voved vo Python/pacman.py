class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position: ({self.x},{self.y})'

    def move(self, position):
        x_position = position[0]
        y_position = position[1]
        new_x = abs(self.x - x_position)
        new_y = abs(self.y - y_position)
        return new_x,new_y


class Game:
    def __init__(self, matrix):
        self.matrix = matrix


class Pacman:
    player = Player
    game = Game([5, 5])

    def __init__(self, player, game):
        self.player = player
        self.game = game



if __name__ == "__main__":
    m = int(input())
    n = int(input())
    i = 0
    matrix = []
    full_matrix = []
    while i < n:
        line = str(input())
        matrix = list(line)
        # splits string into characters and stores it in list
        full_matrix.append(matrix)
        i += 1
