import random
import matplotlib.pyplot as plt


def simulate_dice_flips(num_flips):
    results = []
    for _ in range(num_flips):
        result = random.randint(1, 6)
        results.append(result)
    return results


# Simulating and storing results
results_list = []
num_flips_list = [6, 600, 6000, 600000]

for num_flips in num_flips_list:
    results = simulate_dice_flips(num_flips)
    results_list.append(results)

# Plotting all charts on one plot
fig, axs = plt.subplots(1, 4, figsize=(15, 8))

for i, ax in enumerate(axs.flat):
    ax.hist(results_list[i], bins=range(1, 8), edgecolor='black', align='left')

plt.tight_layout()
plt.show()
