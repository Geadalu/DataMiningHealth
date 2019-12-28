"""
@author: lcalzado
"""

import pandas as panda

#dataFinal = panda.read_csv(r"C:\Users\lcalzado\Desktop\resultado_2ej.csv", encoding='iso-8859-1')
dataFinal = panda.read_csv(r"C:\Users\Lucía Calzado\Desktop\resultado_2ej.csv", encoding='iso-8859-1')
#dataFinal = panda.read_csv(r'C:\Users\lucia\OneDrive\Escritorio\resultado_2ej.csv', encoding='iso-8859-1')

dataFinal.drop(dataFinal[dataFinal["What is your age?"] < 17].index, inplace=True)
dataFinal.drop(dataFinal[dataFinal["What is your age?"] > 75].index, inplace=True)

#dataFinal.to_csv(r'C:\Users\lcalzado\Desktop\datasetUsable_2ej.csv', index=False)
dataFinal.to_csv(r'C:\Users\Lucía Calzado\Desktop\datasetUsable_2ej.csv', index=False)
#dataFinal.to_csv(r'C:\Users\lucia\OneDrive\Escritorio\datasetUsable_2ej.csv', index=False)