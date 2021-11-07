from src.algorithms.algorithm import *
from collections import deque


class BFS(AlgorithmInterface):

    def next_step(self, current_cell, maze):
        if len(self.open_nodes) == 0:
            self.set_result(Result(self.return_nodes_visited(), False, "NO PATH!"))
            self.set_solved_maze(True)
            return None
        current_cell = self.open_nodes.popleft()
        if current_cell is maze.end_cell:
            self.set_result(Result(self.return_nodes_visited(), True, "FOUND PATH!"))
            self.set_solved_maze(True)
            self.backtrack(current_cell, maze.start_cell)
            return current_cell
        neighbors = self.get_neighbors(current_cell, maze)
        for n in neighbors:
            if n.traversable and not self.closed_nodes.__contains__(n):
                n.parent = current_cell
                self.closed_nodes.append(n)
                self.open_nodes.append(n)
        return current_cell

    def mark_visited_cells(self):
        for cell in self.closed_nodes:
            cell.set_color((255, 73, 0, 100))
        for cell in self.open_nodes:
            cell.set_color((135, 255, 66, 100))
        for cell in self.best_path_nodes:
            if cell is not None:
                cell.set_color((0, 25, 255, 100))

    def initialize(self, maze):
        if self.initialized:
            return
        else:
            self.set_initialized(True)
            self.open_nodes = deque()
            self.closed_nodes.append(maze.start_cell)
            self.open_nodes.append(maze.start_cell)

    def find_min_in_open_nodes(self):
        pass

    def backtrack(self, current_node, target_node):
        if current_node.parent is None or current_node is target_node:
            return
        else:
            self.best_path_nodes.append(current_node)
            return self.backtrack(current_node.parent, target_node)

    def return_nodes_visited(self):
        return len(self.open_nodes) + len(self.closed_nodes)

    def get_new_instance(self):
        new = BFS()
        new.set_defaults()
        new.open_nodes = deque()
        return new
