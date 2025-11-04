class Dummy:
    def __init__(self, x):
        self.x = x
    def calc_x_2(self):
        if not isinstance(self.x, (int, float)):
            raise TypeError
        else:
            return self.x**2