import pygame
from src.ui_element import UIElement, AlgorithmUI
from src.algorithms.dijkstra import Dijkstra
from src.algorithms.a_star import AStar
from src.algorithms.breadth_first_search import BFS
from src.controller import State
from src.algorithms.algorithm import Result


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 720))
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.ui_elements = create_ui_elements()
        self.algorithm_ui = create_algorithm_ui()

    def result_to_ui(self, result: Result):
        if result is None:
            return
        pygame.draw.rect(self.screen, (10, 10, 10), pygame.Rect(750, 335, 300, 150))
        pygame.draw.rect(self.screen, (100, 100, 100), pygame.Rect(755, 340, 290, 140))
        message_color = (0, 255, 0) if result.found_exit else (255, 0, 0)
        nodes_visited_text = self.font.render("nodes visited: " + str(result.nodes_visited), False, (255, 255, 255))
        message_text = self.font.render(result.message, False, message_color)
        self.screen.blit(nodes_visited_text, (780, 410))
        self.screen.blit(message_text, (780, 350))

    def draw_ui(self):
        for element in self.ui_elements + self.algorithm_ui:
            if element.active:
                pygame.draw.rect(self.screen, (255, 232, 0),
                                 pygame.Rect(element.x_coord - 4, element.y_coord - 4, element.scale[0] + 8,
                                             element.scale[1] + 8))
            self.screen.blit(pygame.transform.scale(element.image, element.scale), (element.x_coord, element.y_coord))

    def draw_maze(self, maze):
        for row in maze.cell_array:
            for cell in row:
                color = cell.get_color()
                cell_rect = pygame.Rect(cell.x_coord, cell.y_coord, maze.cell_size - 2, maze.cell_size - 2)
                pygame.draw.rect(self.screen, color, cell_rect)

    def get_element_from_pos(self, x, y):
        for element in self.ui_elements:
            if element.check_intersection(x, y):
                return element
        for element in self.algorithm_ui:

            if element.check_intersection(x, y):
                return element
        return None

    def get_active_algorithm(self):
        for alg in self.algorithm_ui:
            if alg.active:
                return alg.related_algorithm

    def set_alg_ui_active(self, algorithm):
        for element in self.algorithm_ui:
            if type(element.related_algorithm) is type(algorithm):
                element.active = True


def create_ui_elements():
    ui_elements = []
    brush = pygame.image.load('images/Brush.png')
    ui_elements.append(UIElement(brush, 750, 25, State.DRAWING))
    eraser = pygame.image.load('images/Eraser.png')
    ui_elements.append(UIElement(eraser, 750, 100, State.ERASING))
    start_node_button = pygame.image.load('images/StartNode.PNG')
    ui_elements.append(UIElement(start_node_button, 750, 175, State.START_NODE))
    end_node_button = pygame.image.load('images/EndNode.PNG')
    ui_elements.append(UIElement(end_node_button, 750, 250, State.END_NODE))
    go = pygame.image.load('images/GO.PNG')
    ui_elements.append(UIElement(go, 850, 25, State.SOLVING, (125, 50)))
    reset = pygame.image.load('images/Reset.PNG')
    ui_elements.append(UIElement(reset, 850, 100, State.RESET, (125, 50)))
    rerun = pygame.image.load('images/Rerun.PNG')
    ui_elements.append(UIElement(rerun, 850, 175, State.RERUN, (125, 50)))
    return ui_elements


def create_algorithm_ui():
    algorithm_elements = []
    a_star = pygame.image.load('images/A-star.PNG')
    algorithm_elements.append(AlgorithmUI(a_star, 825, 625, State.ALGORITHM, AStar(), (125, 50)))
    dijkstra = pygame.image.load('images/Dijkstra.PNG')
    algorithm_elements.append(AlgorithmUI(dijkstra, 925, 550, State.ALGORITHM, Dijkstra(), (125, 50)))
    bfs = pygame.image.load('images/BFS.PNG')
    algorithm_elements.append(AlgorithmUI(bfs, 750, 550, State.ALGORITHM, BFS(), (125, 50)))
    return algorithm_elements
