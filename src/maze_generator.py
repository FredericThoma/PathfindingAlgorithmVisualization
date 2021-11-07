import random


class MazeGenerator:
    def __init__(self):
        self.initialized_maze = False
        self.maze_bool_representation = []
        self.iteration_counter = 0

    def reset(self):
        self.initialized_maze = False
        self.maze_bool_representation = []
        self.iteration_counter = 0

    def next_step(self, maze):
        self.iteration_counter += 1
        if not self.initialized_maze:
            self.initialized_maze = True
            init_maze(maze)
            self.maze_bool_representation = bool_array_from_maze(maze)
        if self.iteration_counter > 100:
            return
        for row in maze.cell_array:
            for cell in row:
                neighbor_indices = get_indices_of_neighbors(cell, maze)
                alive_neighbor_count = count_alive_neighbors(self.maze_bool_representation, neighbor_indices)
                if should_be_alive(cell, alive_neighbor_count):
                    cell.un_mark()
                else:
                    cell.mark()
        self.maze_bool_representation = bool_array_from_maze(maze)


def bool_array_from_maze(maze):
    bool_array = [[True for i in range(maze.rows)] for j in range(maze.columns)]
    for i in range(maze.rows):
        for j in range(maze.columns):
            bool_array[i][j] = maze.cell_from_indices(i, j).traversable
    return bool_array


def init_maze(maze):
    middle_row = maze.columns // 2
    middle_col = maze.rows // 2
    for i in range(maze.rows):
        for j in range(maze.columns):
            if not (middle_row - 2 <= i <= middle_row + 4 and middle_col - 4 <= j <= middle_col + 2):
                maze.cell_array[i][j].mark()
            else:
                if random.randint(0, 100) < 50:
                    maze.cell_array[i][j].mark()


def get_indices_of_neighbors(cell, maze):
    neighbors = []
    row = cell.x_coord // maze.cell_size
    col = cell.y_coord // maze.cell_size
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            current_cell = maze.cell_from_indices(i, j)
            if current_cell and not current_cell == cell:
                neighbors.append((i, j))
    return neighbors


def should_be_alive(cell, neighbor_count):
    if neighbor_count == 3:
        return True
    if not cell.traversable or not 0 < neighbor_count < 5:
        return False
    return True


def count_alive_neighbors(prev_states, neighbor_indices):
    count = 0
    for n in neighbor_indices:
        i, j = n
        if prev_states[i][j]:
            count += 1
    return count
