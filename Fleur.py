class Fleur:
    def __init__(self, x, y):
        self.position = (x, y)
        self.visited = False

    def set_visited(self):
        self.visited = True

    def get_position(self):
        return self.position
