"""
@author: lcalzado
"""

import pandas as panda

#data4 = panda.read_csv(r"C:\Users\lcalzado\Desktop\numeros.csv", encoding='iso-8859-1')
data4 = panda.read_csv(r"C:\Users\lucia\OneDrive\Escritorio\numeros.csv", encoding='iso-8859-1')

data4.drop(data4[data4["What is your age?"] < 17].index, inplace=True)
data4.drop(data4[data4["What is your age?"] > 75].index, inplace=True)

#data4.to_csv(r'C:\Users\lcalzado\Desktop\datasetUsable.csv', index=False);
data4.to_csv(r'C:\Users\lucia\OneDrive\Escritorio\datasetUsable.csv', index=False);