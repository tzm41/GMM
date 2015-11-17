from TwoDGauss import TwoDGauss

# http://www.slideshare.net/jprasanth74/advanced-techniques-for-mobile-robotics
# see above link for variable assignments


def em(data, var0, num_iters, verbose):
    var = var0
    for i in range(num_iters):
        ck = e_step(data)  # respective(weight * means)? / total(weight * means)
        var = m_step(data, ck)
        moving_model1.set_mean_x(var[3])
        moving_model1.set_mean_y(var[4])
        moving_model1.set_var_x(var[9])
        moving_model1.set_var_y(var[10])
        moving_model2.set_mean_x(var[5])
        moving_model2.set_mean_y(var[6])
        moving_model2.set_var_x(var[11])
        moving_model2.set_var_y(var[12])
        moving_model3.set_mean_x(var[7])
        moving_model3.set_mean_y(var[8])
        moving_model3.set_var_x(var[13])
        moving_model3.set_var_y(var[14])
        if verbose:
            print("Found")
    return var


def e_step(data):
    c1, c2, c3 = [], [], []
    for i in range(0, 600):
        x_pt, y_pt = data[i]
        denom = (1 / 6) * moving_model1.std_dist(x_pt, y_pt) \
            + (1 / 3) * moving_model2.std_dist(x_pt, y_pt) \
            + (1 / 2) * moving_model3.std_dist(x_pt, y_pt)
        c1.append((1 / 6) * moving_model1.std_dist(x_pt, y_pt) / denom)
    for i in range(0, 600):
        x_pt, y_pt = data[i]
        denom = (1 / 6) * moving_model1.std_dist(x_pt, y_pt) \
            + (1 / 3) * moving_model2.std_dist(x_pt, y_pt) \
            + (1 / 2) * moving_model3.std_dist(x_pt, y_pt)
        c2.append((1 / 6) * moving_model2.std_dist(x_pt, y_pt) / denom)
    for i in range(0, 600):
        x_pt, y_pt = data[i]
        denom = (1 / 6) * moving_model1.std_dist(x_pt, y_pt) \
            + (1 / 3) * moving_model2.std_dist(x_pt, y_pt) \
            + (1 / 2) * moving_model3.std_dist(x_pt, y_pt)
        c3.append((1 / 6) * moving_model3.std_dist(x_pt, y_pt) / denom)
    return c1, c2, c3


def m_step(data, ck):
    c1, c2, c3 = ck
    w1, w2, w3 = 1 / 6, 1 / 3, 1 / 2
    mean_x1 = get_mean(c1, data, 100, 0)
    mean_y1 = get_mean(c1, data, 100, 1)
    mean_x2 = get_mean(c2, data, 200, 0)
    mean_y2 = get_mean(c2, data, 200, 1)
    mean_x3 = get_mean(c3, data, 300, 0)
    mean_y3 = get_mean(c3, data, 300, 1)
    var_x1 = get_var(c1, data, 100, 0, mean_x1)
    var_y1 = get_var(c1, data, 100, 1, mean_y1)
    var_x2 = get_var(c2, data, 200, 0, mean_x2)
    var_y2 = get_var(c2, data, 200, 1, mean_y2)
    var_x3 = get_var(c3, data, 300, 0, mean_x3)
    var_y3 = get_var(c3, data, 300, 1, mean_y3)
    return w1, w2, w3, \
        mean_x1, mean_y1, mean_x2, mean_y2, mean_x3, mean_y3, \
        var_x1, var_y1, var_x2, var_y2, var_x3, var_y3


# get mean of each variable
# cn - coefficient of model n
# nk - number of points in model n
# coordinate - 0 if x, 1 if y
def get_mean(cn, data, nk: int, coordinate: int) -> float:
    multiplicand = 0
    for i in range(0, 600):
        # data[i][x] is the x/y coordinate of the point
        multiplicand += cn[i] * data[i][coordinate]
    mean = (1 / nk) * multiplicand
    return mean


def get_var(cn, data, nk: int, coordinate: int, mean: float) -> float:
    multiplicand = 0
    for i in range(0, 600):
        multiplicand += cn[i] * (data[i][coordinate] - mean) * (data[i][coordinate] - mean)
    var = (1 / nk) * multiplicand
    return var

moving_model1 = TwoDGauss(1, 1, 1, 1)
moving_model2 = TwoDGauss(2, 1, 2, 1)
moving_model3 = TwoDGauss(3, 1, 3, 1)

# initial variables = (w1, w2, w3,
# mean_x1, mean_y1, mean_x2, mean_y2, mean_x3, mean_y3,
# var_x1, var_y1, var_x2, var_y2, var_x3, var_y3)
init_var = (1 / 6, 1 / 3, 1 / 2,
            moving_model1.mean_x, moving_model1.mean_y,
            moving_model2.mean_x, moving_model2.mean_y,
            moving_model3.mean_x, moving_model3.mean_y,
            moving_model1.var_x, moving_model1.var_y,
            moving_model2.var_x, moving_model2.var_y,
            moving_model3.var_x, moving_model3.var_y
            )

# (1,2), (3,3), (5, 2), and variances (1.0, 1.5), (1.0, 0.5), (0.5, 0.5)
gen_model1 = TwoDGauss(1, 1.0, 2, 1.5)
gen_model2 = TwoDGauss(3, 1.0, 3, 0.5)
gen_model3 = TwoDGauss(5, 0.5, 2, 0.5)

test_data = []
for x in range(0, 100):
    test_data.insert(x, gen_model1.generate_point())
for x in range(100, 300):
    test_data.insert(x, gen_model2.generate_point())
for x in range(300, 600):
    test_data.insert(x, gen_model3.generate_point())

# for x in range(0, 600):
#     print(test_data[x])

# print(init_var)
print(moving_model1.mean_x, moving_model1.mean_y, moving_model1.var_x, moving_model1.var_y)
em(test_data, init_var, 10, False)
print(moving_model1.mean_x, moving_model1.mean_y, moving_model1.var_x, moving_model1.var_y)
