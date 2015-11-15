from TwoDGauss import TwoDGauss
# http://www.slideshare.net/jprasanth74/advanced-techniques-for-mobile-robotics 
# see above link for variable assignments

def em(data, var0, num_iters, verbose):
    var = var0
    for i in range(num_iters):
        u2 = e_step(data, var)  # respective(weight * means)? / total(weight * means)
        var = m_step(data, u2)
        if verbose:
            print("%d  u2 = %f    theta = %f" % (i, u2, theta))
    return var

moving_model1 = TwoDGauss(1, 1, 1, 1)
moving_model2 = TwoDGauss(2, 1, 2, 1)
moving_model3 = TwoDGauss(3, 1, 3, 1)

# initial variables = (w1, w2, w3,
# mean_x1, mean_y1, mean_x2, mean_y2, mean_x3, mean_y3,
# var_x1, var_y1 , var_x2, var_y2, var_x3, var_y3)
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

for x in range(0, 600):
    print(test_data[x])
