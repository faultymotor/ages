import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

SIZE = 100
POINTS = 500

def get_random_voronoi(size=SIZE, points=POINTS):
    points = (np.random.rand(points, 2) * size).astype('uint8')
    return Voronoi(points)

def lloyd_relaxation(vor, reps=1, size=SIZE):
    region_vertices = []

    region_vertices = [np.asarray([vor.vertices[coord] for coord in region]) for region in vor.regions if len(region) > 0]
    
    in_bounds = lambda point: 0 <= point[0] and point[0] < size and 0 <= point[1] and point[1] < size

    new_points = filter(in_bounds, [centeroidnp(vertices) for vertices in region_vertices])
    
    vor = Voronoi(list(new_points))
    return lloyd_relaxation(vor, reps - 1, size) if reps > 1 else vor

def centeroidnp(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return sum_x / length, sum_y / length

vor = get_random_voronoi()
fig = voronoi_plot_2d(vor)
plt.figure(1)

vor = lloyd_relaxation(vor)
fig = voronoi_plot_2d(vor)
plt.figure(2)

plt.show()

