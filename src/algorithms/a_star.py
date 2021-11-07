from src.algorithms.algorithm import *


class AStar(AlgorithmInterface):

    def get_new_instance(self):
        new = AStar()
        new.set_defaults()
        return new

    def mark_visited_cells(self):
        for cell in self.open_nodes:
            if cell is not None:
                cell.set_color((135, 255, 66, 100))
        for cell in self.closed_nodes:
            if cell is not None:
                cell.set_color((255, 73, 0, 100))
        for cell in self.best_path_nodes:
            if cell is not None:
                cell.set_color((0, 25, 255, 100))

    def initialize(self, maze):
        if self.initialized:
            return
        else:
            self.set_initialized(True)

    def next_step(self, current_cell, maze):

        if current_cell is maze.end_cell:
            self.set_result(Result(self.return_nodes_visited(), True, "FOUND PATH!"))
            return self.backtrack(current_cell, maze.start_cell)
        elif current_cell is maze.start_cell and not self.open_nodes.__contains__(current_cell):
            current_cell.g_cost = 0
            current_cell.parent = current_cell
            current_cell.calc_dists(current_cell.parent, maze)
            self.open_nodes.append(current_cell)
            return current_cell
        elif current_cell is None or len(self.open_nodes) == 0:

            self.set_result(Result(self.return_nodes_visited(), False, "NO PATH FOUND"))
            self.set_solved_maze(True)


        else:
            self.open_nodes.remove(current_cell)
            self.closed_nodes.append(current_cell)
            neighbors = self.get_neighbors(current_cell, maze)
            for cell in neighbors:
                cell.calc_dists(current_cell, maze)
            self.append_valid_neighbors_to_open_nodes(neighbors)

            return self.find_min_in_open_nodes()

    def backtrack(self, current_node, target_node):
        if current_node is target_node:
            self.set_solved_maze(True)
            return None
        else:
            self.best_path_nodes.append(current_node)
            return self.backtrack(current_node.parent, target_node)

    def append_valid_neighbors_to_open_nodes(self, neighbors):
        for cell in neighbors:
            if not self.closed_nodes.__contains__(cell) and not self.open_nodes.__contains__(cell):
                self.open_nodes.append(cell)

    def find_min_in_open_nodes(self):
        cells_with_min_g_cost = []
        min_f_cost = 999999999
        min_h_cost = 999999999
        for cell in self.open_nodes:
            if cell.f_cost == min_f_cost:
                cells_with_min_g_cost.append(cell)
            if cell.f_cost < min_f_cost:
                cells_with_min_g_cost.clear()
                cells_with_min_g_cost.append(cell)
                min_f_cost = cell.f_cost
        if len(cells_with_min_g_cost) == 1:
            return cells_with_min_g_cost[0]
        else:
            current_cell = None
            for cell in cells_with_min_g_cost:
                if cell.h_cost <= min_h_cost:
                    min_h_cost = cell.h_cost
                    current_cell = cell
            return current_cell

    def return_nodes_visited(self):
        return len(self.open_nodes) + len(self.closed_nodes)
