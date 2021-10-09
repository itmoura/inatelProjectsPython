import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


def plot(x, x_label, y, y_label):
    if len(x) == 1 and len(y) == 1:
        print("Error to plot!")
    else:
        ax = plt.gca()
        ax.plot(x, y, color="blue", linewidth=1.5)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        ax.set_xlim([np.min(x), np.max(x)])
        ax.set_ylim([np.min(y), np.max(y)])

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(f"{x_label} vs {y_label}")

        ax.grid()
        plt.show()

