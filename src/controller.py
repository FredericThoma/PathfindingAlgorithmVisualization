from enum import Enum
from src.maze import Maze


class State(Enum):
    SOLVING = 1
    DRAWING = 2
    ERASING = 3
    START_NODE = 4
    END_NODE = 5
    ALGORITHM = 6
    RESET = 7
    RERUN = 8
    DONE = 9
    PASSING = 10
    AUTO_GEN = 11


class Controller:

    def __init__(self, maze, window, algorithm, generator):
        self.state = State.DRAWING
        self.maze = maze
        self.window = window
        self.algorithm = algorithm
        self.generator = generator

    def update(self):
        if self.state.DRAWING:
            self.window.set_alg_ui_active(self.algorithm)

    def handle_mouse_down(self, x, y):
        cell = self.maze.get_cell_from_pos(x, y)
        if cell:
            self.request_cell_update(cell)
        else:
            ui_element = self.window.get_element_from_pos(x, y)
            if ui_element:
                self.request_element_update(ui_element)

    def request_element_update(self, ui_element):
        if self.algorithm.solved_maze:
            self.set_state(self.state.DONE)
        if ui_element.related_state is State.ALGORITHM:
            self.set_state(self.state.PASSING)
            self.set_active_algorithm(ui_element.related_algorithm)
        else:
            self.set_state(ui_element.related_state)
            self.update_ui_elements()

    def set_active_algorithm(self, related_algorithm):
        self.algorithm = related_algorithm
        for element in self.window.algorithm_ui:
            if element.related_algorithm is related_algorithm:
                element.active = True
            else:
                element.active = False

    def request_cell_update(self, cell):
        if self.state is State.DRAWING:
            cell.mark()
            cell.set_color((50, 50, 50))
        elif self.state is State.ERASING:
            cell.un_mark()
            cell.set_color((200, 200, 200))
        elif self.state is State.START_NODE:
            self.maze.set_start_node(cell)
        elif self.state is State.END_NODE:
            self.maze.set_end_node(cell)

    def check_start_end_node(self):
        if self.maze.start_cell is None:
            self.set_state(self.state.START_NODE)
            self.update_ui_elements()
            return False
        elif self.maze.end_cell is None:
            self.set_state(self.state.END_NODE)
            self.update_ui_elements()
            return False
        return True

    def reset(self):
        for element in self.window.algorithm_ui:
            element.related_algorithm = element.related_algorithm.get_new_instance()
        self.algorithm.set_defaults()
        self.set_state(self.state.DRAWING)
        self.update_ui_elements()
        self.maze = Maze(self.maze.rows, self.maze.columns, self.maze.cell_size)
        new = self.window.get_active_algorithm().get_new_instance()
        new.set_defaults()
        self.algorithm = new
        self.generator.reset()

    def set_state(self, new_state: State):
        self.state = new_state

    def update_ui_elements(self):
        for element in self.window.ui_elements:
            element.active = True if self.state is element.related_state else False

    def reset_algorithm(self):
        self.update_ui_elements()
        new = self.window.get_active_algorithm().get_new_instance()
        new.set_defaults()
        self.maze.reset_cells()
        new.mark_visited_cells()
        self.algorithm = new

    def get_state(self):
        return self.state
