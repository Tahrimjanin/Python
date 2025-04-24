from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Uniform Distribution -- para-low=0, high=1
uniform_data = random.uniform(size=1000)
sns.kdeplot(uniform_data, ax=axs[0, 0])
axs[0, 0].set_title("Uniform Distribution")

# Logistic Distribution -- para-low=0, scale=1
logistic_data = random.logistic(size=1000)
sns.kdeplot(logistic_data, ax=axs[0, 1])
axs[0, 1].set_title("Logistic Distribution")

# Difference Between Normal and Logistic Distribution
normal_data = random.normal(scale=2, size=1000)
data = {
    "normal": normal_data,
    "logistic": logistic_data
}
sns.kdeplot(normal_data, ax=axs[1, 0], label="Normal")
sns.kdeplot(logistic_data, ax=axs[1, 0], label="Logistic")
axs[1, 0].set_title("Normal vs Logistic Distribution")
axs[1, 0].legend()

# Multinomial Distribution para--low=0, n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6] 
multinomial_data = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
axs[1, 1].bar(range(len(multinomial_data)), multinomial_data)
axs[1, 1].set_title("Multinomial Distribution (Dice Roll)")

# Exponential Distribution para--low=0, scale=2
exponential_data = random.exponential(scale=2, size=1000)
sns.kdeplot(exponential_data, ax=axs[2, 0])
axs[2, 0].set_title("Exponential Distribution")

# Poisson vs Exponential Distribution
poisson_data = random.poisson(lam=50, size=1000)
data_pe = {
    "Poisson": poisson_data,
    "Exponential": exponential_data
}
sns.kdeplot(poisson_data, ax=axs[2, 1], label="Poisson")
sns.kdeplot(exponential_data, ax=axs[2, 1], label="Exponential")
axs[2, 1].set_title("Poisson vs Exponential Distribution")
axs[2, 1].legend()

plt.tight_layout()
plt.show()
