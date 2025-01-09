import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import lagrange_interpolation as l_inter

density_chart_x_inner = [0, 5/60, 10/60, 15/60, 20/60, 25/60, 30/60, 35/60, 40/60, 0.7, 45/60]
density_chart_y_inner = [180000, 155000, 137000, 120000, 105000, 93000, 83000, 75000, 67500, 65000, 62000]
density_chart_x_outer = [0.75, 2, 3, 4, 5, 6, 10, 20]
density_chart_y_outer = [62000, 31000, 24300, 20000, 17700, 16500, 11000, 6000]

density_chart_x_whole = [0, 5/60, 10/60, 15/60, 20/60, 25/60, 30/60, 35/60, 40/60, 45/60, 2, 3, 4, 5, 6, 10, 20, 50]
density_chart_y_whole = [180000, 155000, 137000, 120000, 105000, 93000, 83000, 75000, 67500, 62000, 31000, 24300, 20000, 17700, 16500, 11000, 6000, 6000]

def den_func_inner(r):
    return l_inter.langrange_Barycentric(density_chart_x_inner, density_chart_y_inner)(r)

def den_func_approx_outer(r, a, b, c, d, e):
    return a * r + b / (c * r**2 + d * r + e)
dens_func_param = sp.optimize.curve_fit(den_func_approx_outer, density_chart_x_outer, density_chart_y_outer)[0]

def density_function_1D(r):
        if (r < 0):
             r = -r
        if (r < 0.75):
            return den_func_inner(r)
        f = lambda r: den_func_approx_outer(r, dens_func_param[0], dens_func_param[1], dens_func_param[2], dens_func_param[3], dens_func_param[4])
        if (r > 20):
            return f(20)
        else:
            return f(r)
        
def density_function_2D(x, y):
     r_ = (x**2 + y**2)**(1/2)
     r_sqr = x**2/(1 + 0.2 * r_)**2 + y**2
     r = r_sqr**(1/2)
     return density_function_1D(r)

def plot_density_level_surface():
    X, Y = np.meshgrid(np.linspace(-6, 6, 200), np.linspace(-6, 6, 200))
    Z = np.empty_like(X)

    for i in range(200):
         for j in range(200):
              Z[i][j] = (density_function_2D(X[i][j], Y[i][j]))
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.view_init(elev=15, azim=30)
    surf = ax.plot_surface(X, Y, Z, cmap="viridis")
    fig.colorbar(surf)
    plt.xlabel("Eccentricity / Deg, Nasal-Temporal")
    plt.ylabel("Eccentricity / Deg, Superior-Inferior")
    plt.show()

# plot_density_level_surface()

def plot_density_1D():
    X = np.linspace(0, 10, 500)
    Y = np.empty_like(X)
    for i in range(len(X)):
          Y[i] = density_function_1D(X[i])
    plt.plot(X, Y)
    plt.show()

# plot_density_1D()

def plot_density_2D_level_contour():
    X, Y = np.meshgrid(np.linspace(-6, 6, 200), np.linspace(-6, 6, 200))
    Z = np.empty_like(X)

    for i in range(200):
         for j in range(200):
              Z[i][j] = (density_function_2D(X[i][j], Y[i][j]))

    fig = plt.figure()
    plt.contour(X, Y, Z, 20)
    plt.colorbar()
    plt.xlabel("Eccentricity / Deg, Nasal-Temporal")
    plt.ylabel("Eccentricity / Deg, Superior-Inferior")
    ax=plt.gca()
    plt.show()

plot_density_2D_level_contour()
# print(density_function_1D(0.75))
# print(density_function_1D(2))
# print(density_function_1D(3))
# print(density_function_1D(4))
# print(density_function_1D(5))
# print(density_function_1D(6))