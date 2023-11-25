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
mhd_file_path = 'Counts\cil1\cil1_89.mhd'

# Calculate the sum of pixel values
total_sum = sum_pixel_values(mhd_file_path)

# Print the result
print(f"Sum of pixel this  values in {mhd_file_path}: {total_sum}")