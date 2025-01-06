import numpy as np
import scipy as sp
import Math_Tools.lagrange_interpolation as l_inter

density_chart_x_inner = [0, 5/60, 10/60, 15/60, 20/60, 25/60, 30/60, 35/60, 40/60, 45/60]
density_chart_y_inner = [180000, 155000, 137000, 120000, 105000, 93000, 83000, 75000, 67500, 60180]
density_chart_x_outer = [0.6, 2, 3, 4, 5, 6]
density_chart_y_outer = [72000, 31000, 24300, 20000, 17700, 16500]

def den_func_inner(r):
    return l_inter.langrange_Barycentric(density_chart_x_inner, density_chart_y_inner)(r)

def den_func_approx_outer(r, a, b, c, d , e, f):
    return a * r + b + c / (d * r**2 + e * r + f)
dens_func_param = sp.optimize.curve_fit(den_func_approx_outer, density_chart_x_outer, density_chart_y_outer)[0]

def density_function_1D(r):
        if (r < 0.75):
            return den_func_inner(r)
        else:
            return den_func_approx_outer(r, dens_func_param[0], dens_func_param[1], dens_func_param[2], dens_func_param[3], dens_func_param[4], dens_func_param[5])
        
def density_function_2D(x, y):
     r_sqr = x**2/1.44 + y**2
     r = r_sqr**(1/2)
     return density_function_1D(r)

def print_density_contour():
     x = np.linspace(0, 6, 100)
     y = np.linspace(0, 6, 100)