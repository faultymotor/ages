import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

SIZE = 400
POINTS = 200

def get_random_voronoi(size=SIZE, points=POINTS):
    points = (np.random.rand(points, 2) * size).astype('uint8')
    vor = Voronoi(points)
    return voronoi_plot_2d(vor)

fig = get_random_voronoi()
plt.show()

