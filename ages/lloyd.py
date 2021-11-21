import numpy as np

def find_centroid(ndarray):
    length, _ = ndarray.shape
    return np.array([np.sum(ndarray[:,0]), np.sum(ndarray[:,1])]) / length

def relax(vertices, regions):
    hulls = filter(bool, regions)
    hulls = map(lambda hull: np.take(vertices, hull, 0), hulls)
    hulls = map(find_centroid, hulls)

    return np.array(list(hulls))

def constrain(points, bounds):
    width, height = bounds
    def constrain_point(point):
        x, y = point
        return max(0, min(width, x)), max(0, min(height, y))

    return list(map(constrain_point, points))