import pandas as pd
import numpy as np
import Ruche
import Bee


def parse():
    return pd.read_excel('./fleurs.xlsx')

c = parse()
print(c)


