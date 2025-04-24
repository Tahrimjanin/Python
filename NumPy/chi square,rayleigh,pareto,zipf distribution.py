from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Chi Square Distribution para:-low=0, df=2
chi_square_data = random.chisquare(df=2, size=1000)
sns.kdeplot(chi_square_data, ax=axs[0, 0])
axs[0, 0].set_title("Chi Square Distribution")

# Rayleigh Distribution para:-low=0, scale=2
rayleigh_data = random.rayleigh(scale=2, size=1000)
sns.kdeplot(rayleigh_data, ax=axs[0, 1])
axs[0, 1].set_title("Rayleigh Distribution")

# Similarity Between Rayleigh and Chi Square 
data_rc = {
    "Rayleigh": rayleigh_data,
    "Chi Square": chi_square_data
}
sns.kdeplot(rayleigh_data, ax=axs[1, 0], label="Rayleigh")
sns.kdeplot(chi_square_data, ax=axs[1, 0], label="Chi Square")
axs[1, 0].set_title("Rayleigh vs Chi Square Distribution")
axs[1, 0].legend()

# Pareto Distribution :para--low=0, a=2
pareto_data = random.pareto(a=2, size=1000)
sns.kdeplot(pareto_data, ax=axs[1, 1])
axs[1, 1].set_title("Pareto Distribution")

# Zipf Distribution para--low=0, a=2
zipf_data = random.zipf(a=2, size=1000)
sns.kdeplot(zipf_data[zipf_data < 10], ax=axs[2, 0])
axs[2, 0].set_title("Zipf Distribution")

plt.tight_layout()
plt.show()
