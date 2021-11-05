class Ruche:
    def __init__(self, reine):
        self.reine = reine
        self.pos = (500, 500)
        self.abeilles = []

    def bannir(self, bee):
        self.abeilles.remove(bee)

