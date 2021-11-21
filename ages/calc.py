import numpy as np
from scipy.spatial import Voronoi
from ages import lloyd

SIZE = 100
POINTS = 500

def get_random_voronoi(size=SIZE, num_points=POINTS):
    points = (np.random.rand(num_points, 2) * size).astype('uint64')
    return Voronoi(points)

def lloyd_relaxation(vor, reps=1, size=SIZE):
    points = lloyd.relax(vor.vertices, vor.regions)
    points = lloyd.constrain(points, (size, size))
    vor = Voronoi(points)

    return lloyd_relaxation(vor, reps - 1, size) if reps > 1 else vor