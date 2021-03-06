from src.cell import *
from src.algorithms.algorithm import *


class Dijkstra(AlgorithmInterface):

    def mark_visited_cells(self):

        for cell in self.closed_nodes:
            if cell is not None:
                cell.set_color((135, 255, 66, 100))
        for cell in self.best_path_nodes:
            if cell is not None:
                cell.set_color((0, 25, 255, 100))

    def initialize(self, maze):
        self.set_initialized(True)
        for row in maze.cell_array:
            for cell in row:
                if cell.traversable:
                    self.open_nodes.append(cell)
        maze.start_cell.g_cost = 0

    def next_step(self, current_cell, maze):
        if current_cell is maze.start_cell and not self.initialized:
            self.initialize(maze)
            return current_cell
        if current_cell is maze.end_cell:
            print("END CELL")
            self.set_result(Result(self.return_nodes_visited(), True, "FOUND PATH!"))
            self.set_solved_maze(True)
            self.backtrack(maze.end_cell, maze.start_cell)
            return
        elif len(self.open_nodes) == 0 or current_cell is None:
            print("NONE OR LEN 0")
            self.set_result(Result(self.return_nodes_visited(), False, "NO PATH FOUND"))
            self.set_solved_maze(True)
        else:
            neighbors = self.get_neighbors(current_cell, maze)
            for n in neighbors:
                if not n.visited:
                    alt = current_cell.g_cost + dist_between_cells(n, current_cell, maze)
                    if alt < n.g_cost:
                        n.g_cost = alt
                        n.parent = current_cell
            current_cell = self.find_min_in_open_nodes()
            if current_cell is None:
                return None
            self.open_nodes.remove(current_cell)
            self.closed_nodes.append(current_cell)
            current_cell.visited = True
            return current_cell

    def backtrack(self, current_node, target_node):
        while current_node is not target_node:
            self.best_path_nodes.append(current_node)
            current_node = current_node.parent
        self.set_solved_maze(True)

    def find_min_in_open_nodes(self):
        min_g = float('inf')
        next_cell = None
        for cell in self.open_nodes:
            if cell.g_cost < min_g:
                min_g = cell.g_cost
                next_cell = cell
        return next_cell

    def return_nodes_visited(self):
        return len(self.closed_nodes)

    def get_new_instance(self):
        new = Dijkstra()
        new.set_defaults()
        return new
