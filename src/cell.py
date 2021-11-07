class Cell:

    def __init__(self, x, y, traversable: bool = True):
        self.x_coord = x
        self.y_coord = y
        self.traversable = traversable
        self.color = (200, 200, 200)
        self.g_cost = float('inf')  # dist to start node
        self.h_cost = float('inf')  # dist to end node
        self.f_cost = self.g_cost + self.h_cost  # sum of distances to start and end
        self.parent = None
        self.visited = False

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def mark(self):
        self.traversable = False
        self.set_color((50, 50, 50))

    def un_mark(self):
        self.traversable = True
        self.set_color((200, 200, 200))

    def reset(self):
        self.set_color((200, 200, 200) if self.traversable else (50, 50, 50))
        self.g_cost = float('inf')
        self.h_cost = float('inf')
        self.f_cost = self.g_cost + self.h_cost
        self.parent = None
        self.visited = False

    def calc_dists(self, parent_cell, maze):
        new_g_cost = parent_cell.g_cost + dist_between_cells(self, parent_cell, maze)
        if new_g_cost < self.g_cost:
            self.g_cost = new_g_cost
            self.parent = parent_cell
        self.h_cost = dist_between_cells(self, maze.end_cell, maze)
        self.f_cost = self.g_cost + self.h_cost


def dist_between_cells(cell_a, cell_b, maze):
    diff_row = abs((cell_a.x_coord // maze.cell_size) - (cell_b.x_coord // maze.cell_size))
    diff_col = abs((cell_a.y_coord // maze.cell_size) - (cell_b.y_coord // maze.cell_size))
    dist = 0
    while not (diff_row == 0 or diff_col == 0):
        diff_row -= 1
        diff_col -= 1
        dist += 14
    if diff_row == 0:
        return dist + 10 * diff_col
    else:
        return dist + 10 * diff_row
