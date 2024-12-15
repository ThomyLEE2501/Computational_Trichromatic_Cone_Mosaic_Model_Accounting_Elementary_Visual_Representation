import numpy as np

class Cone_Cell:

    def __init__(self, tp, coord_r, coord_t, chr_res):
        self.type = tp
        self.coordinate_r = coord_r
        self.coordinate_t = coord_t
        self.chromatic_response = chr_res
        self.spike_state = False

    def spike(self):
        self.spike_state = True

