class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position: ({self.x},{self.y})'

    def move(self):
        pass


class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super(DownAgent, self).__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == "__main__":
    la = LeftAgent(3, 4)
    for i in range(5):
        la.move()
        print(f'Step: {i + 1} {la}')
    print("")
    ra = RightAgent(3, 4)
    for i in range(5):
        ra.move()
        print(f'Step: {i + 1} {ra}')
    print("")
    ua = UpAgent(3, 4)
    for i in range(5):
        ua.move()
        print(f'Step: {i + 1} {ua}')
    print("")
    da = DownAgent(3, 4)
    for i in range(5):
        da.move()
        print(f'Step: {i + 1} {da}')
