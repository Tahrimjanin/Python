from numpy import random
import matplotlib.pyplot as plt #plt is a plotting library and numerical mathematics extension NumPy
import seaborn as sns #library for making statistical graphics in Python
import pandas as pd #pd is pandas_library for data manipulation and analysis
import warnings 
warnings.filterwarnings("ignore")


fig, axs = plt.subplots(3, 2, figsize=(12, 12))  # Create a 3x2 grid of subplots

# Normal Distribution -- para :loc ,scale, size 
normal_data = random.normal(loc=50, scale=5, size=1000)
sns.kdeplot(normal_data, ax=axs[0, 0])  # Plot KDE on first subplot
axs[0, 0].set_title("Normal Distribution") #axs is short for axes

# Binomial Distribution -- para :n, p, size
binomial_data = random.binomial(n=100, p=0.5, size=1000)
sns.kdeplot(binomial_data, ax=axs[0, 1])  # Plot KDE on second subplot
axs[0, 1].set_title("Binomial Distribution")

# Poisson Distribution -- para :lam, size
poisson_data = random.poisson(lam=50, size=1000)
sns.kdeplot(poisson_data, ax=axs[1, 0])  # Plot KDE on third subplot
axs[1, 0].set_title("Poisson Distribution")

# Normal vs Binomial
data_nb = {
    "Normal": normal_data,
    "Binomial": binomial_data
}
sns.kdeplot(normal_data, ax=axs[1, 1], label="Normal")
sns.kdeplot(binomial_data, ax=axs[1, 1], label="Binomial")
axs[1, 1].set_title("Normal vs Binomial Distribution")
axs[1, 1].legend()

# Normal vs Poisson
data_np = {
    "Normal": normal_data,
    "Poisson": poisson_data
}
sns.kdeplot(normal_data, ax=axs[2, 0], label="Normal")
sns.kdeplot(poisson_data, ax=axs[2, 0], label="Poisson")
axs[2, 0].set_title("Normal vs Poisson Distribution")
axs[2, 0].legend()

# Binomial vs Poisson
binomial_lowp = random.binomial(n=1000, p=0.01, size=1000)
poisson_low = random.poisson(lam=10, size=1000)

data_bp = {
    "Binomial (n=1000, p=0.01)": binomial_lowp,
    "Poisson (λ=10)": poisson_low
}
sns.kdeplot(binomial_lowp, ax=axs[2, 1], label="Binomial (n=1000, p=0.01)")
sns.kdeplot(poisson_low, ax=axs[2, 1], label="Poisson (λ=10)")
axs[2, 1].set_title("Binomial vs Poisson Distribution")
axs[2, 1].legend()

plt.tight_layout()
plt.show()
