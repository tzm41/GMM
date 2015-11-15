from TwoDGauss import TwoDGauss

moving_model1 = TwoDGauss(1, 1, 1, 1)
moving_model2 = TwoDGauss(2, 1, 2, 1)
moving_model3 = TwoDGauss(3, 1, 3, 1)

# (1,2), (3,3), (5, 2), and variances (1.0, 1.5), (1.0, 0.5), (0.5, 0.5)
gen_model1 = TwoDGauss(1, 1.0, 2, 1.5)
gen_model2 = TwoDGauss(3, 1.0, 3, 0.5)
gen_model3 = TwoDGauss(5, 0.5, 2, 0.5)

data = []
for x in range(0, 100):
    data.insert(x, gen_model1.generate_point())
for x in range(100, 300):
    data.insert(x, gen_model2.generate_point())
for x in range(300, 600):
    data.insert(x, gen_model3.generate_point())

for x in range(0, 600):
    print(data[x])
