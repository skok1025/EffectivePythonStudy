ALIVE = '*'
EMPTY = '-'

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []

        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.rows])


grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

print(grid)

def count_neighbors(y, x, get):
    n_ = get(y - 1, x + 0)  # 북(N)쪽 이웃
    ne = get(y - 1, x + 1)  # 북동(NE)쪽 이웃
    e_ = get(y + 0, x + 1)  # 동(E)쪽 이웃
    se = get(y + 1, x + 1)  # 남동(SE)쪽 이웃
    s_ = get(y + 1, x + 0)  # 남(S)쪽 이웃
    sw = get(y + 1, x - 1)  # 남서(SW)쪽 이웃
    w_ = get(y + 0, x - 1)  # 서(W)쪽 이웃
    nw = get(y - 1, x - 1)  # 북서(NW)쪽 이웃
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY  # 살아 있는 이웃이 너무 적음: 죽음
        elif neighbors > 3:
            return EMPTY  # 살아 있는 이웃이 너무 많음: 죽음
    else:
        if neighbors == 3:
            return ALIVE  # 다시 생성됨
    return state