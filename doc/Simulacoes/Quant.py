import numpy as np 

#path_output = "output/"
#path_dose_squared=
#path_dose_uncertainty=


f="output1e6/c1content-Dose.mhd"

doseMap = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)

dose = doseMap.sum()/len(doseMap)

print(dose)

#def main 
#for arq in rang(len(lista_cilindros)-1):
    
#    f=
#    doseMap = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)
#    dose =doseMap.sum()/len(doseMap)
