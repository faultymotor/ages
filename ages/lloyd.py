import numpy as np

def find_centroid(ndarray):
    length, _ = ndarray.shape
    return np.array([np.sum(ndarray[:,0]), np.sum(ndarray[:,1])]) / length

def relax(vertices, regions):
    region_vertices = [np.asarray([vertices[coord] for coord in region]) for region in regions if len(region) > 0]

    return [find_centroid(vertices) for vertices in region_vertices]

def constrain(points, bounds):
    width, height = bounds
    def constrain_point(point):
        x, y = point
        return max(0, min(width, x)), max(0, min(height, y))

    return list(map(constrain_point, points))