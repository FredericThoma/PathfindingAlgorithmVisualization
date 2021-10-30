class UIElement:
    def __init__(self, image, x_coord, y_coord, related_state, scale: (int, int) = (50, 50)):
        self.image = image
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.size = 75
        self.scale = scale
        self.active = False
        self.related_state = related_state

    def check_intersection(self, x, y):
        return (x > self.x_coord and y > self.y_coord) and (
                x < self.x_coord + self.scale[0] and y < self.y_coord + self.scale[1])

    def update(self, state):
        pass


class AlgorithmUI(UIElement):
    def __init__(self, image, x_coord, y_coord, related_state, related_algorithm, scale):
        super().__init__(image, x_coord, y_coord, related_state, scale)
        self.related_algorithm = related_algorithm


