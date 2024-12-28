import numpy as np

class Cone_Cell:

    def __init__(self, type, chromatic_response, **kwargs):
        self.type = type
        self.chromatic_response = chromatic_response
        self.spike_state = False
        self.coord_r = kwargs.get('coord_r', None)
        self.coord_th = kwargs.get('coord_th', None)
        self.coord_x = kwargs.get('coord_x', None)
        self.coord_y = kwargs.get('coord_y', None)

        if (len(kwargs) < 4):
            if (self.coord_r == None):
                if (self.coord_x == None or self.coord_y == None):
                    raise Exception("Not enough coordinates information.")
                self.coord_r = np.power((self.coord_x**2 + self.coord_y**2), 1/2)
            if (self.coord_th == None):
                if (self.coord_x == None or self.coord_y == None):
                    raise Exception("Not enough coordinates information.")
                if (self.coord_x == 0):
                    self.coord_th = np.pi/2 if self.coord_y > 0 else -np.pi/2
                self.coord_th = np.arctan(self.coord_y/self.coord_x) if self.coord_y > 0 else np.pi + np.arctan(self.coord_y/self.coord_x)
            if (self.coord_x == None):
                if (self.coord_r == None or self.coord_th == None):
                    raise Exception("Not enough coordinates information.")
                self.coord_x = np.cos(self.coord_th) * self.coord_r
            if (self.coord_y == None):
                if (self.coord_r == None or self.coord_th == None):
                    raise Exception("Not enough coordinates information.")
                self.coord_y = np.sin(self.coord_th) * self.coord_r

    def spike(self):
        self.spike_state = True

c1 = Cone_Cell(0, False, coord_x = -5, coord_y = -7)

print(c1.coord_th)