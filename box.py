import math
import numpy

class Box():
    def __init__(self, d, verticies):
        self.d = d
        self.verticies = verticies

    # Projected point formula:
    # projected x = dx / (d - z) = x / (1 - z/d)

    def projected_point(self, p):
        projected_x = p[0] / (1 - p[2] / self.d)
        projected_y = p[1] / (1 - p[2] / self.d)

        return [projected_x, projected_y]

    def projected_verticies(self):
        return [self.projected_point(v) for v in self.verticies]

    # standard matrices for rotation
    def rotate_over_z(self, theta):
        standard_matrix = numpy.array([[math.cos(theta), -math.sin(theta), 0],
                                        [math.sin(theta), math.cos(theta), 0],
                                        [0, 0, 1]])

        self.verticies = [standard_matrix.dot(v) for v in self.verticies]

    def rotate_over_x(self, theta):
        standard_matrix = numpy.array([[1, 0, 0],
                                        [0, math.cos(theta), math.sin(theta)],
                                        [0, -math.sin(theta), math.cos(theta)]])

        self.verticies = [standard_matrix.dot(v) for v in self.verticies]

    def rotate_over_y(self, theta):
        standard_matrix = numpy.array([[math.cos(theta), 0, math.sin(theta)],
                                        [0, 1, 0],
                                        [-math.sin(theta), 0, math.cos(theta)]])

        self.verticies = [standard_matrix.dot(v) for v in self.verticies]