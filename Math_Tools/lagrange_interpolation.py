import numpy as np
import matplotlib.pyplot as plt
def langrange_Barycentric(x_l, y_l):
    k = len(x_l)
    if (k != len(y_l)):
        raise Exception("Arrays are not of the same size")
    
    def w_j(j):
        wj = 1
        for m in range(k):
            if (m != j):
                wj *= 1 / (x_l[j]-x_l[m])
        return wj
    
    def poly_interpolated(x):
        l_cap_num = 0
        l_cap_den = 0
        for j in range(k):
            if (x == x_l[j]):
                return y_l[j]
            l_cap_num += w_j(j) / (x - x_l[j]) * y_l[j]
            l_cap_den += w_j(j) / (x - x_l[j])
        return l_cap_num / l_cap_den
    
    return poly_interpolated
