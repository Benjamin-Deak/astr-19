import numpy as np
import math
from tabulate import tabulate

x = np.linspace(0, 2 * math.pi, 1000)
sinx = np.sin(x)

table_data = [(a, b) for a, b in zip(x, sinx)]

table_headers = ["x", "sin(x)"]
table = tabulate(table_data, tablefmt="grid", headers=table_headers, floatfmt=".3f")

def main():
    print(table)

main()