import math
import numpy
import scipy.stats


class TwoDGauss:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    #     self.mean_x = numpy.mean(self.x)
    #     self.var_x = numpy.var(self.x)

    def __init__(self, var_x, var_y, mean_x, mean_y):
        self.var_x = var_x
        self.var_y = var_y
        self.mean_x = mean_x
        self.mean_y = mean_y

    def mean_x(self):
        return self.mean_x

    def set_mean_x(self, mean_x):
        self.mean_x = mean_x

    def mean_y(self):
        return self.mean_y

    def var_x(self):
        return self.var_x

    def var_y(self):
        return self.var_y

    # bivariate pdf
    def std_dist(self, x_pt, y_pt):
        sigma_x = math.sqrt(self.var_x)
        sigma_y = math.sqrt(self.var_y)
        k = (1 / (2 * math.pi * self.var_x() * sigma_x * sigma_y))
        exp = (-1 / 2) * ((math.pow(x_pt - self.mean_x(), 2) / self.var_x()) +
                          (math.pow(y_pt - self.mean_y(), 2) / self.var_y()))
        return k * math.pow(math.e, exp)

