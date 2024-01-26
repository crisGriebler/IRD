import numpy as np 

#path_output = "output/"
#path_dose_squared=
#path_dose_uncertainty=
a="macros2/outputnew14.12.23/c1content-Dose.mhd"
b="macros2/outputnew14.12.23/c2content-Dose.mhd"
c="macros2/outputnew14.12.23/c3content-Dose.mhd"
d="macros2/outputnew14.12.23/c4content-Dose.mhd"
## ----------------------------------------------##
f="macros_Adet_jan/outputnew/c1content-Dose.mhd"
g="macros_Adet_jan/outputnew/c2content-Dose.mhd"
h="macros_Adet_jan/outputnew/c3content-Dose.mhd"
i="macros_Adet_jan/outputnew/c4content-Dose.mhd"

doseMap1 = np.fromfile(a.replace('mhd','raw'), dtype=np.float32)
len1 = len(doseMap1)
dose1 = doseMap1.sum()/len1

doseMap2 = np.fromfile(b.replace('mhd','raw'), dtype=np.float32)
len2 =len(doseMap2)
dose2 = doseMap2.sum()/len2

doseMap3 = np.fromfile(c.replace('mhd','raw'), dtype=np.float32)
len3 =len(doseMap3)
dose3 = doseMap3.sum()/len(doseMap3)

doseMap4 = np.fromfile(d.replace('mhd','raw'), dtype=np.float32)
len4 =len(doseMap4)
dose4 = doseMap4.sum()/len(doseMap4)

## --------------------------------------------------------------##

doseMap1_ = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)
len1_ = len(doseMap1_)
dose1_ = doseMap1_.sum()/len1_

doseMap2_ = np.fromfile(g.replace('mhd','raw'), dtype=np.float32)
len2_ =len(doseMap2_)
dose2_ = doseMap2_.sum()/len2_

doseMap3_ = np.fromfile(h.replace('mhd','raw'), dtype=np.float32)
len3_ =len(doseMap3_)
dose3_ = doseMap3_.sum()/len(doseMap3_)

doseMap4_= np.fromfile(i.replace('mhd','raw'), dtype=np.float32)
len4_ =len(doseMap4_)
dose4_ = doseMap4_.sum()/len(doseMap4_)


print('*************************')
print('Resultados da Dose com a Atividade real')
print("cilindro 1 = ", dose1, "Gy")
print("Tamanho do cilindro 1 =", len1)
print("cilindro 2 = ", dose2, "Gy ")
print("Tamanho do cilindro 2 =", len2)
print("cilindro 3 = ", dose3, "Gy ")
print("Tamanho do cilindro 3 =", len3)
print("cilindro 4 = ", dose4, "Gy ")
print("Tamanho do cilindro 4 =", len4)
print('*************************\n')

print('*************************')
print('Resultados da Dose sem Recovery Coefficient')
print("cilindro 1 = ", dose1_, "Gy")
print("Tamanho do cilindro 1 =", len1_)
print("cilindro 2 = ", dose2_, "Gy ")
print("Tamanho do cilindro 2 =", len2_)
print("cilindro 3 = ", dose3_, "Gy ")
print("Tamanho do cilindro 3 =", len3_)
print("cilindro 4 = ", dose4_, "Gy ")
print("Tamanho do cilindro 4 =", len4_)
print('*************************\n')

