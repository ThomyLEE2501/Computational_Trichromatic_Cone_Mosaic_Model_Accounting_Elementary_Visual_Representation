import numpy as np
import scipy as sp
import cone_cell
class Cone_Clump:
    def __init__(self, size, category, reference_cone):
        self.size = size
        self.category = category
        self.coord_r = reference_cone.coord_r
        self.coord_th = reference_cone.coord_th
        self.coord_x = reference_cone.coord_x
        self.coord_y = reference_cone.coord_y
    
    def density_function_1D(r):

        density_chart_x = [0.7, 2, 3, 4, 5, 6]
        density_chart_y = [80000, 31000, 24300, 20000, 17700, 16500]
        def den_func_approx(r, a, b, c, d , e, f):
            return a * r + b + c / (d * r**2 + e * r + f)
        dens_func = sp.optimize.curve_fit(den_func_approx, density_chart_x, density_chart_y)
        param_arr = dens_func[0]
        def deriv(r):
            return sp.misc.derivative(Cone_Clump.density_function_1D, r, dx=1e-6)
        
        return den_func_approx(r, param_arr[0], param_arr[1], param_arr[2], param_arr[3], param_arr[4], param_arr[5])
    
print()
print(Cone_Clump.density_function_1D(0.67))
print(Cone_Clump.density_function_1D(0.7))
print(Cone_Clump.density_function_1D(2))
print(Cone_Clump.density_function_1D(3))
print(Cone_Clump.density_function_1D(4))
print(Cone_Clump.density_function_1D(5))
print(Cone_Clump.density_function_1D(6))