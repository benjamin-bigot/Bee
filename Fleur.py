class Fleur:
    def __init__(self, x, y, id):
        self.__id = id
        self.__position = (x, y)

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id
