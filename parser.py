import numpy as np


def parseASCII(filename: str):
    freq = []
    opticalDensity = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for x in lines:
                if x[0] == '#' or x.isspace():
                    continue
                data = x.split()
                freq.append(data[0])
                opticalDensity.append(data[1])
    except FileNotFoundError:
        return None
    return np.array(freq, dtype=float), np.array(opticalDensity, dtype=float)

