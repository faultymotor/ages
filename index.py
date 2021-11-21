import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

SIZE = 100
POINTS = 500

def get_random_voronoi(size=SIZE, points=POINTS):
    points = (np.random.rand(points, 2) * size).astype('uint8')
    return Voronoi(points)

def lloyd_relaxation(vor, size=SIZE):
    region_vertices = []

    for region in vor.regions:
        if len(region) > 0:
            vertices = [vor.vertices[c] for c in region]
            region_vertices.append(np.asarray(vertices))
    
    supposed_points = [centeroidnp(vertices) for vertices in region_vertices]
    new_points = []

    for point in supposed_points:
        if 0 <= point[0] and point[0] < size and 0 <= point[1] and point[1] < size:
            new_points.append(point)
            
    return Voronoi(new_points)

def centeroidnp(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return sum_x/length, sum_y/length

vor = get_random_voronoi()
fig = voronoi_plot_2d(vor)
plt.figure(1)

vor = lloyd_relaxation(vor)
fig = voronoi_plot_2d(vor)
plt.figure(2)

plt.show()

