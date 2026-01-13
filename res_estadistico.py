#crear un programa que calcule la media, la mediana y la desviación estándar de un conjunto de datos cualquiera
import pandas as pd
import numpy as np
datos = pd.read_csv('datos.csv',header = None) 
resumen = datos.describe().loc[['mean','50%','std']]
resumen.index = ['media','mediana','desviacion_estandar']
resumen.columns = ['valores']
print (resumen)