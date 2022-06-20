# Во овој проблем ќе ја имплементирате играта Pacman.
# Оваа игра се игра така што имате едно човече кое се движи низ просторот
# и целта е да ги изеде сите точки притоа избегнувајќи чудовишта.
# Видео кое ќе ве запознае со играта: https://www.youtube.com/watch?v=i_OjztdQ8iw.
# Притоа во нашиот пример е поедноставена оваа игра така што секогаш ќе имате правоаголни форми
# и не треба да избегнувате чудовишта. Целта на оваа поедноставена игра е да се изедат сите точки во просторот.
#
# Креирајте класа Player која го означува играчот во играта.
# Во оваа класа треба да ги чувате моменталните позиции на играчот во играта (x и y координати).
# Оваа класа има метода move(position) што означува придвижување на играчот на дадената позиција.
# Потоа креирајте класа Game која ќе ја означува моменталната игра.
# Во оваа класа треба да го чувате просторот на игра (матрица) и притоа може да си чувате и помошни вредности.
# За крај креирајте класа Pacman во која ќе чувате инстанца од класата Player и класата Game .
# Во оваа класа треба да имате една метода play_game() во која треба да ја имплементирате логиката за играта.
# Почетната позиција на играчот е (0,0). Играчот може да се движи горе, долу, лево или десно.
# Притоа ако во некоја можна позиција каде може да се придвижи играчот има точка тогаш таа позиција
# е посакуваната позиција каде треба да се придвижи.
# Ако има повеќе позиции каде има точки, во тој случај играчот избира случајно каде да се придвижи.
# Ако во ниедна можна позиција нема точки, тогаш пак играчот избира случајно на која позиција ќе се придвижи.
# Играта завршува кога нема преостанати точки кои треба да ги изеде играчот.
#
# Влез: На влез прво добивате ширина и висина на просторот за игра.
# Потоа во секој нареден ред добивате состојбата на редот од просторот.
# Притоа секоја позиција се означува со # што означува празно поле и . што означува дека во полето има точка.
#
# Излез: На излез се печати секој чекор кој го направил играчот се додека не ги изел сите точки.
#
# Напомена: За да симулирате случајно придвижување може да го користите модулот random.
# Метода која генерира случаен број во даден ранг е randint(range_from, range_to).
# Може да користите и дополнителни методи од овој модул кои може да ги најдете во документација.
# Бидејќи работиме со случајни придвижувања, НЕ МОРА тест примерите да ви поминуваат,
# туку се само за ваше тестирање.
import random
random.seed(0)
global n, m, matrix


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Position: ({self.x},{self.y})'

    def move(self, direction):
        directions = []
        all_dots = []
        x = self.x
        y = self.y
        if direction == 1: #TOP
            if [x, y + 1] in dot_positions and y + 1 != m - 1:
                self.x = x
                self.y = y + 1
                dot_positions.remove([x, y])
                directions.append(['Gore'])
                all_dots.append([x, y + 1])
            elif y+1 != m-1:
                self.x = x
                self.y = y + 1
                directions.append(['Gore'])
        elif direction == 2: #RIGHT
            if [x + 1, y] in dot_positions and x + 1 != n - 1:
                self.x = x + 1
                self.y = y
                dot_positions.remove([x, y])
                directions.append(['Desno'])
                all_dots.append([x + 1, y])
            elif x+1 != n-1:
                self.x = x + 1
                self.y = y
                directions.append(['Desno'])
        elif direction == 3: #BOTTOM
            if [x, y - 1] in dot_positions and y - 1 != 0:
                self.x = x
                self.y = y - 1
                dot_positions.remove([x, y])
                directions.append(['Dole'])
                all_dots.append([x, y - 1])
            elif y - 1 != 0:
                self.x = x
                self.y = y
                directions.append(['Dole'])
        elif direction == 4: #LEFT
            if [x - 1, y] in dot_positions and x - 1 != 0:
                self.x = x - 1
                self.y = y
                dot_positions.remove([x, y])
                directions.append(['Levo'])
                all_dots.append([x - 1, y])
            elif x-1 != 0:
                self.x = x - 1
                self.y = y
                directions.append(['Levo'])
        return directions


    def goal_test(self):
        if not dot_positions:
            return f'All dots are eaten! \nHere are the directions of the player:'
        else:
            return f'Your program is broken'

    class Game:
        def __init__(self, grid_size):
            self.grid_size = grid_size

        def __str__(self):
            return f'The size of the matrix is {self.grid_size[0]}x{self.grid_size[0]}'


    class Pacman:
        def __init__(self, player, game):
            grid_size = (n, m)
            player = Player()
            game = Game()

        def play_game(self):
            player.move()


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(0, n):
        string_line = str(input())
        temp_matrix = list(string_line)
        matrix.append(temp_matrix)
    print(f'{matrix}')
    dot_positions = []
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == "#":
                matrix[i][j] = 0
            elif matrix[i][j] == ".":
                matrix[i][j] = 1
                dot_positions.append([i, j])
    print(f'{matrix}')
    print(f'{dot_positions}')
    player = Player(0, 0)
    result = []
    for i in range(0, n * m):
        direction = (random.randint(1, 4))
        player.move(direction)
    print(player.goal_test())