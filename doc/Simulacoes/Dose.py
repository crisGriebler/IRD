import numpy as np 

#path_output = "output/"
#path_dose_squared=
#path_dose_uncertainty=


f="setintensity/1e8/c1content-Dose.mhd"
g="setintensity/1e8/c2content-Dose.mhd"
h="setintensity/1e8/c3content-Dose.mhd"
i="setintensity/1e8/c4content-Dose.mhd"

doseMap1 = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)
dose1 = doseMap1.sum()/len(doseMap1)

doseMap2 = np.fromfile(g.replace('mhd','raw'), dtype=np.float32)
dose2 = doseMap2.sum()/len(doseMap2)

doseMap3 = np.fromfile(h.replace('mhd','raw'), dtype=np.float32)
dose3 = doseMap3.sum()/len(doseMap3)

doseMap4 = np.fromfile(i.replace('mhd','raw'), dtype=np.float32)
dose4 = doseMap4.sum()/len(doseMap4)


print('*************************\n')
print("cilindro 1 = ", dose1, "Gy")
print("cilindro 2 = ", dose2, "Gy ")
print("cilindro 3 = ", dose3, "Gy ")
print("cilindro 4 = ", dose4, "Gy ")
print('*************************\n')


