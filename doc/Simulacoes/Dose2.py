##
## Esse código é para cálculo de Dose da pasta macros2 com a atividade correta de cada cilindro.
##

import numpy as np 

f="macros2/outputnew/c1content-Dose.mhd"
g="macros2/outputnew/c2content-Dose.mhd"
h="macros2/outputnew/c3content-Dose.mhd"
i="macros2/outputnew/c4content-Dose.mhd"

doseMap1 = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)
len1 = len(doseMap1)
dose1 = doseMap1.sum()/len1

doseMap2 = np.fromfile(g.replace('mhd','raw'), dtype=np.float32)
len2 = len(doseMap2)
dose2 = doseMap2.sum()/len2

doseMap3 = np.fromfile(h.replace('mhd','raw'), dtype=np.float32)
len3 = len(doseMap3)
dose3 = doseMap3.sum()/len(doseMap3)

doseMap4 = np.fromfile(i.replace('mhd','raw'), dtype=np.float32)
len4 = len(doseMap4)
dose4 = doseMap4.sum()/len(doseMap4)


print('*************************\n')
print("cilindro 1 = ", dose1, "Gy")
print("Tamanho do cilindro 1 =", len1)
print("cilindro 2 = ", dose2, "Gy ")
print("Tamanho do cilindro 2 =", len2)
print("cilindro 3 = ", dose3, "Gy ")
print("Tamanho do cilindro 3 =", len3)
print("cilindro 4 = ", dose4, "Gy ")
print("Tamanho do cilindro 4 =", len4)
print('*************************\n')