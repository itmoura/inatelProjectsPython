import os

import numpy as np
import pandas as pd
from numpy import genfromtxt


class DataSets:

    @staticmethod
    def read(folder, filename):
        filename_abs = os.path.join(os.path.dirname(__file__), folder, filename)
        return genfromtxt(filename_abs, delimiter=",", dtype=float)

    @staticmethod
    def add_bias(arr, bias = -1):
        biased_arr = np.ndarray(shape=(arr.shape[0], arr.shape[1]+1), dtype=float)
        for i in range(0, len(arr)):
            biased_arr[i] = np.append(bias, arr[i])

        return biased_arr

class IRIS:
    df = pd.read_csv("./dataset_1.csv")
    df.isna().any()

    input = DataSets.add_bias(np.array((df["sepal_largura"], df["sepal_comprimento"])).reshape(-1, 2))
    outputs = np.array(list(df["tipo"])).reshape(-1, 1)

    output = np.arange(outputs.size, dtype=float).reshape(-1, 1)

    for i in range(outputs.size):
        if outputs[i] == 'setosa':
            output[i] = 0
        else:
            output[i] = 1
