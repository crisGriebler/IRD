import SimpleITK as sitk

def sum_pixel_values(mhd_file_path):
    # Read the image
    image = sitk.ReadImage(mhd_file_path)

    # Get the pixel array
    pixel_array = sitk.GetArrayFromImage(image)

    # Sum the pixel values
    total_sum = pixel_array.sum()

    return total_sum

# Replace 'your_file.mhd' with the path to your MHD file
mhd_file_path = 'BG_cil4_tripla.mhd'

# Calculate the sum of pixel values
total_sum = sum_pixel_values(mhd_file_path)

# Print the result
print(f"Sum of pixel values in {mhd_file_path}: {total_sum}")

#import numpy as np 
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#path_output = "output/"
#path_dose_squared=
#path_dose_uncertainty=

#f="En89_2/89cil2p.mhd"
#f="En89_2/89cil2m.mhd"
#f="En156_2/156cil2.mhd"
#f="En270_2/270cil2.mhd"
#f="tripla2/triplacil2.mhd"
#f="tripla2/triplacil2m.mhd"


#f=f = mpimg.imread('BG_cil4_89.mhd')
#g="En156_1/156cil1.mhd"
#f="En270_1/270cil1.mhd"
#f="tripla1/triplacil1.mhd"
#Quant = np.fromfile(f.replace('mhd','zraw'), dtype=np.uint16)
#print('Tamanho de f: ', f.shape)
#print('Tipo do pixel:', f.dtype)
#print('Número total de pixels:', f.size)
#print('Pixels:\n', f)
#Counts = Quant.sum()

#print(Counts)



#Dose = doseMap.sum()/len(doseMap)
#def main 
#for arq in rang(len(lista_cilindros)-1):
    
#    f=
#    doseMap = np.fromfile(f.replace('mhd','raw'), dtype=np.float32)
#    dose =doseMap.sum()/len(doseMap)
