from scipy import io
from scipy.interpolate import interp1d, UnivariateSpline, Rbf
import numpy as np

#MATLAB ARRAY EXPORT & IMPORT
# Original array
arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})
mydata = io.loadmat('arr.mat', squeeze_me=True)
vec = mydata['vec']
print("Imported from .mat file:\n", vec)

#INTERPOLATION SETUP 
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1 

new_xs = np.arange(2.1, 3, 0.1)

#1D LINEAR INTERPOLATION
linear_ys = 2*xs + 1
linear_interp = interp1d(xs, linear_ys)
linear_result = linear_interp(new_xs)
print("\n1D Linear Interpolation:\n", linear_result)

#UNIVARIATE SPLINE INTERPOLATION 
spline_interp = UnivariateSpline(xs, ys)
spline_result = spline_interp(new_xs)
print("\nSpline Interpolation:\n", spline_result)

# RADIAL BASIS FUNCTION 
rbf_interp = Rbf(xs, ys)
rbf_result = rbf_interp(new_xs)
print("\nRBF Interpolation:\n", rbf_result)
