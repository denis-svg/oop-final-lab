import matplotlib.pyplot as plt
from statistics import mean

class Plotter:
    @staticmethod
    def plot(arr, label):
        plt.plot([i + 5 for i in range(len(arr))], arr, label=label + str(mean(arr)))
        plt.legend()
        plt.show()