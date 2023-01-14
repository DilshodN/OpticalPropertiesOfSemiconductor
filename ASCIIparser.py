import numpy as np
import GraphicsPlotter
import Tok_functions


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


def exportASCII(freqs: np.array, values: np.array, filename: str):
    with open(filename, 'w') as file:
        for i in range(len(freqs)):
            file.write(str(freqs[i]) + " " + str(values[i]) + "\n")
    file.close()
