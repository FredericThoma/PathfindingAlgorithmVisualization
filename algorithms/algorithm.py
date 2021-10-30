from abc import ABC, abstractmethod



class Result:
    def __init__(self, nodes_visited, found_exit, message):
        self.nodes_visited = nodes_visited
        self.found_exit = found_exit
        self.message = message


class AlgorithmInterface(ABC):

    def __init_subclass__(cls, **kwargs):
        cls.open_nodes = []
        cls.closed_nodes = []
        cls.best_path_nodes = []
        cls.result = None
        cls.initialized = False
        cls.solved_maze = False

    @classmethod
    def set_defaults(cls):
        cls.open_nodes = []
        cls.closed_nodes = []
        cls.best_path_nodes = []
        cls.result = None
        cls.initialized = False
        cls.solved_maze = False

    @classmethod
    def set_result(cls, result):
        cls.result = result

    @classmethod
    def set_solved_maze(cls, has_solved_maze):
        cls.solved_maze = has_solved_maze

    @classmethod
    def set_initialized(cls, is_initialized):
        cls.initialized = is_initialized

    @classmethod
    def get_neighbors(cls, cell, maze):
        neighbors = []

        row = cell.x_coord // maze.cell_size
        col = cell.y_coord // maze.cell_size
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                current_cell = maze.cell_from_indices(i, j)
                if current_cell:
                    if not current_cell == cell and current_cell.traversable:
                        neighbors.append(current_cell)
        return neighbors

    @abstractmethod
    def next_step(self, current_cell, maze):
        pass

    @abstractmethod
    def mark_visited_cells(self):
        pass

    @abstractmethod
    def initialize(self, maze):
        pass

    @abstractmethod
    def find_min_in_open_nodes(self):
        pass

    @abstractmethod
    def backtrack(self, current_node, target_node):
        pass

    @abstractmethod
    def return_nodes_visited(self):
        pass

    @abstractmethod
    def get_new_instance(self):
        pass
