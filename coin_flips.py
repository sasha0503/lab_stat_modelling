import random
import matplotlib.pyplot as plt


def simulate_coin_flips(num_flips):
    results = []
    for _ in range(num_flips):
        result = random.choice(['Heads', 'Tails'])
        results.append(result)
    return results


# Simulating and storing results
results_list = []
num_flips_list = [10, 100, 1000, 10000]

for num_flips in num_flips_list:
    results = simulate_coin_flips(num_flips)
    results_list.append(results)

# Plotting all charts on one plot
fig, axs = plt.subplots(1, 4, figsize=(15, 8))

for i, ax in enumerate(axs.flat):
    heads_count = results_list[i].count('Heads')
    tails_count = results_list[i].count('Tails')
    ax.bar(['Орел', 'Решка'], [heads_count, tails_count])
    ax.set_title(f'{num_flips_list[i]} Підкидань')

plt.tight_layout()
plt.show()
