import matplotlib.pyplot as plt
from constants import *


def plot_results(logbook, best_individual):
	"""
	Visualize the evolution results and best terrain.
	Args:
		logbook: Evolution statistics
		best_individual: Best terrain found
	"""
	# Plot fitness evolution
	gen = logbook.select("gen")
	avg = logbook.select("avg")
	min_ = logbook.select("min")

	fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

	ax1.plot(gen, avg, label="Average Fitness")
	ax1.plot(gen, min_, label="Best Fitness")
	ax1.set_xlabel("Generation")
	ax1.set_ylabel("Fitness")
	ax1.legend()

	# Visualize best terrain
	x = range(len(best_individual))
	sea = [SEA_LEVEL for _ in range(len(best_individual))]

	ax2.fill_between(x, sea, color="turquoise")
	ax2.fill_between(x, best_individual, color="sandybrown")
	ax2.set_title("Best Terrain Found")
	ax2.axis("off")

	plt.tight_layout()
	plt.show()