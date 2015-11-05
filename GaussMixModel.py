import TwoDGauss


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