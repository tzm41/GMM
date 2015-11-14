
data1 = (25, 5, 5, 5)  # Theta = 0.5
data2 = (25, 0, 1, 12)  # Theta = almost 1
data3 = (25, 12, 13, 0)  # Theta = almost 0

# Estimate a new value of u2 given a value for theta
def e_step(data, theta):
    x1, x2, x3, x4 = data
    return (x1 * theta * 0.25) / (0.5 + 0.25 * theta)

# Maximize value of theta given an estimate for u2
def m_step(data, u2):
    x1, x2, x3, x4 = data
    return (u2 + x4) / (u2 + x2 + x3 + x4)

def em(data, theta0, num_iters, verbose):
    theta = theta0
    for i in xrange(num_iters):
        u2 = e_step(data, theta)
        theta = m_step(data, u2)
        if verbose:
            print("%d  u2 = %f    theta = %f" % (i, u2, theta))
    return theta

def run_test(data, theta0):
    print("Test with data = %s, theta0 = %f" % (data, theta0))
    em(data, theta0, 15, True)

#run_test(data1, 0.5)
#run_test(data1, 0.0)
#run_test(data1, 0.999)
print
run_test(data2, 0.5)
#run_test(data2, 0.25)
#run_test(data2, 0.75)
print
#run_test(data3, 0.5)
#run_test(data3, 0.25)
#run_test(data3, 0.75)
