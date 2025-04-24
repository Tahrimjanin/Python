import numpy as np

# LCM 
num1 = 4
num2 = 6
print("LCM of 4 and 6:", np.lcm(num1, num2))

arr_lcm = np.array([3, 6, 9])
print("LCM of array [3, 6, 9]:", np.lcm.reduce(arr_lcm))

# GCD 
num3 = 6
num4 = 9
print("GCD of 6 and 9:", np.gcd(num3, num4))

arr_gcd = np.array([20, 8, 32, 36, 16])
print("GCD of array [20, 8, 32, 36, 16]:", np.gcd.reduce(arr_gcd))

# Trigonometric Functions
angle_rad = np.pi / 2
print("sin(pi/2):", np.sin(angle_rad))

arr_angles = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("sin values:", np.sin(arr_angles))
print("cos values:", np.cos(arr_angles))
print("tan values:", np.tan(arr_angles))

# Degree to Radian
deg_arr = np.array([90, 180, 270, 360])
print("Degrees to Radians:", np.deg2rad(deg_arr))

# Radian to Degree
rad_arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
print("Radians to Degrees:", np.rad2deg(rad_arr))

# Inverse Trigonometric Functions
x_val = 1.0
print("arcsin(1.0):", np.arcsin(x_val))

sine_vals = np.array([1, -1, 0.1])
print("arcsin of array:", np.arcsin(sine_vals))

# Hypotenuse (Pythagorean Theorem)
base = 3
perp = 4
print("Hypotenuse of base 3 and perp 4:", np.hypot(base, perp))

# Hyperbolic Functions
print("sinh(pi/2):", np.sinh(np.pi/2))
print("cosh values:", np.cosh(arr_angles))
print("tanh values:", np.tanh(arr_angles))

# Inverse Hyperbolic Functions
print("arcsinh(1.0):", np.arcsinh(1.0))

tanh_arr = np.array([0.1, 0.2, 0.5])
print("arctanh values:", np.arctanh(tanh_arr))
