class Ruche:
    def __init__(self):
        self.__pos = (500, 500)
        self.abeilles = []

    def get_pos(self):
        return self.__pos

    def bannir(self, bee):
        self.abeilles.remove(bee)

