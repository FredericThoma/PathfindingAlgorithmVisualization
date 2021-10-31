from src.cell import Cell


class Maze:
    def __init__(self, rows, columns, cell_size):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.cell_array = self.generate_cell_array(rows, columns)
        self.start_cell = None
        self.end_cell = None

    def reset_cells(self):
        for row in self.cell_array:
            for cell in row:
                cell.reset()

    def generate_cell_array(self, rows, columns):
        _cell_array = [[Cell(i * self.cell_size, j * self.cell_size) for i in range(rows)] for j in range(columns)]
        return _cell_array

    def get_cell_from_pos(self, x, y):
        i = x // self.cell_size
        j = y // self.cell_size
        return self.cell_from_indices(i, j)

    def cell_from_indices(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            return self.cell_array[j][i]
        else:
            return None

    def indices_from_coords(self, x, y):
        return x // self.cell_size, y // self.cell_size

    def set_start_node(self, cell):
        if self.start_cell is None:
            self.start_cell = cell

    def set_end_node(self, cell):
        if self.end_cell is None:
            self.end_cell = cell

    def auto_generate_maze(self):
        pass

    def update_state(self):
        for row in self.cell_array:
            for cell in row:
                if self.start_cell is cell:
                    cell.set_color((255, 0, 0))
                elif self.end_cell is cell:
                    cell.set_color((255, 0, 0))
