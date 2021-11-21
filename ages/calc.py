import numpy as np
from scipy.spatial import Voronoi

SIZE = 100
POINTS = 500

def get_random_voronoi(size=SIZE, points=POINTS):
    points = (np.random.rand(points, 2) * size).astype('uint8')
    return Voronoi(points)

def lloyd_relaxation(vor, reps=1, size=SIZE):
    in_bounds = lambda point: 0 <= point[0] and point[0] < size and 0 <= point[1] and point[1] < size

    region_vertices = [np.asarray([vor.vertices[coord] for coord in region]) for region in vor.regions if len(region) > 0]
    region_vertices = [vertices for vertices in region_vertices if len(list(filter(in_bounds, vertices))) > 0]

    new_points = [find_centroid(vertices) for vertices in region_vertices]
    new_points = filter(in_bounds, new_points)
    new_points = list(new_points)
    
    vor = Voronoi(new_points)
    return lloyd_relaxation(vor, reps - 1, size) if reps > 1 else vor

def find_centroid(ndarray):
    length = ndarray.shape[0]
    return np.sum(ndarray[:, 0]) / length, np.sum(ndarray[:, 1]) / length