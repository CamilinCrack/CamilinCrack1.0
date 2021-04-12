import pandas as pd 
import numpy as np
from io import open 
from datetime import datetime 

Caudal = pd.read_csv("Caudal.txt", header = 0)
Caudal['Fecha'], Caudal['Valor'] = Caudal['Fecha|Valor'].str.split('|', 1).str

#No puedo tomar caudal igual a cero en caso de no existir dato
caudal = Caudal.drop(["Fecha|Valor"], axis =1)

arreglo = np.array(caudal)
arreglo = {"Fecha": arreglo[:,0], "Valor": arreglo[:,1]}
registro = pd.DataFrame(data=arreglo)

registro_copia = registro.copy()

registro["Fecha"] = pd.to_datetime(registro["Fecha"])
registro["Valor"] = registro.Valor.astype(float)

caudal_promedio = registro.groupby(pd.PeriodIndex(registro.Fecha, freq="M")).mean()
caudal_matrix = np.resize(caudal_promedio, (31, 12))
#asasasasas
caudal_matrix = pd.DataFrame(data=caudal_matrix)
#caudal_matrix.iloc[0] = ("N", "N", "N", "N", "N", "N", "N", "N")
#
#caudal_matrixx = caudal_matrix.insert(0, vacios)
#help (np.resize)

#print(caudal_matrix)
print(caudal_matrix)
print(caudal_promedio)
#print(registro)
#print(registro.shape)
