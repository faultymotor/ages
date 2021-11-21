import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

SIZE = 400
POINTS = 200

points = (np.random.rand(POINTS, 2) * SIZE).astype('uint8')

vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.show()