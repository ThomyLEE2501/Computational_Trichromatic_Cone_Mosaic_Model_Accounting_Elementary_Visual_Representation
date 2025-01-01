import numpy as np
import cone_cell
class Cone_Clump:
    def __init__(self, size, category, reference_cone):
        self.size = size
        self.category = category
        self.coord_r = reference_cone.coord_r
        self.coord_th = reference_cone.coord_th
        self.coord_x = reference_cone.coord_x
        self.coord_y = reference_cone.coord_y