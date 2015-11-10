import TwoDGauss

# Your class should support changing the mean, variance, and weight of any component.
class GMM:
    def __init__(self, n):
        self.n = n
        self.models = [[int, TwoDGauss]]

    def add_model(self, weight, model):
        self.models.append([weight, model])

    def change_weight(self, index, weight):
        old = self.models[index]
        old[0] = weight
        self.models.insert(index, old)
    
    def change_mean(self, index, mean):
		old = self.models[index]
		old[0].set_mean_x(old[0], mean.x)
		old[0].set_mean_y(old[0], mean.y)
		self.models.insert(index, old)
