import TwoDGauss


# Your class should support changing the mean, variance, and weight of any component.
class GMM:
    def __init__(self, n):
        self.n = n
        self.models = [float, TwoDGauss]    # float is the weight

    def add_model(self, weight, model):
        self.models.append([weight, model])

    def change_weight(self, index, weight):
        if weight < 0 or weight > 1:
            old = self.models[index]
            old[0] = weight
            self.models.insert(index, old)
    
    def change_mean(self, index, mean_x, mean_y):
        old = self.models[index]
        old[1].set_mean_x(mean_x)
        old[1].set_mean_y(mean_y)
        self.models.insert(index, old)
    
    def change_var(self, index, var_x, var_y):
        old = self.models[index]
        old[1].set_var_x(var_x)
        old[1].set_var_y(var_y)
        self.models.insert(index, old)
