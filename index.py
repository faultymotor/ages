from scipy.spatial import voronoi_plot_2d
import matplotlib.pyplot as plt
from ages import calc

SIZE = 100
POINTS = 500

vor = calc.get_random_voronoi(size=SIZE, points=POINTS)
fig = voronoi_plot_2d(vor)
plt.figure(1)

vor = calc.lloyd_relaxation(vor=vor, reps=1, size=SIZE)
fig = voronoi_plot_2d(vor)
plt.figure(2)

plt.show()

