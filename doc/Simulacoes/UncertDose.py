
import numpy as np 

#path_output = "output/"
#path_dose_squared=
#path_dose_uncertainty=


f="setintensity/1e8/c1content-Dose-Uncertainty.mhd"
g="setintensity/1e8/c2content-Dose-Uncertainty.mhd"
h="setintensity/1e8/c3content-Dose-Uncertainty.mhd"
i="setintensity/1e8/c4content-Dose-Uncertainty.mhd"


UndoseMap1 = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)
Undose1 = (UndoseMap1.sum()/len(UndoseMap1))*100

UndoseMap2 = np.fromfile(g.replace('mhd','raw'), dtype=np.float32)
Undose2 = (UndoseMap2.sum()/len(UndoseMap2))*100

UndoseMap3 = np.fromfile(h.replace('mhd','raw'), dtype=np.float32)
Undose3 = (UndoseMap3.sum()/len(UndoseMap3))*100

UndoseMap4 = np.fromfile(i.replace('mhd','raw'), dtype=np.float32)
Undose4 = (UndoseMap4.sum()/len(UndoseMap4))*100


print('*************************\n')
print("cilindro 1 = ", Undose1, "% de incerteza relativa")
print("cilindro 2 = ", Undose2, "% de incerteza relativa")
print("cilindro 3 = ", Undose3, "% de incerteza relativa")
print("cilindro 4 = ", Undose4, "% de incerteza relativa ")
