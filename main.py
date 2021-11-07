from src.controller import *
from src.maze import Maze
from src.gui import *
from src.maze_generator import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    maze = Maze(36, 36, 20)
    algorithm = AStar()
    window = Window()
    generator = MazeGenerator()
    controller = Controller(maze, window, algorithm, generator)
    current_cell = controller.maze.start_cell
    counter = 0
    while True:
        clock.tick(100)
        counter += 1
        if counter % 5 == 0 and controller.state is controller.state.AUTO_GEN:
            generator.next_step(controller.maze)
        controller.window.screen.fill((100, 100, 100))
        controller.window.draw_ui()
        controller.update()
        current_state = controller.get_state()
        if current_state is current_state.START_NODE:
            current_cell = controller.maze.start_cell
        if current_state is current_state.SOLVING and not controller.algorithm.solved_maze:
            if controller.check_start_end_node():
                frame_rate = 40
                current_cell = controller.algorithm.next_step(current_cell, controller.maze)
                controller.algorithm.mark_visited_cells()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if current_state is current_state.RESET:
            controller.set_state(current_state.DRAWING)
            controller.reset()
        if current_state is current_state.RERUN:
            controller.maze.reset_cells()
            current_cell = controller.maze.start_cell
            controller.set_state(current_state.SOLVING)
            controller.reset_algorithm()
        if controller.algorithm.solved_maze:
            controller.window.result_to_ui(controller.algorithm.result)
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            controller.handle_mouse_down(x, y)
        controller.maze.update_state()
        controller.window.draw_maze(controller.maze)
        pygame.display.update()


if __name__ == '__main__':
    main()
