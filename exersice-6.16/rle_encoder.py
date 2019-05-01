from PIL import Image
import numpy as np

quantization_value = 10

# Convert image to black & white
bw_image = Image.open("../images/logo.jpg").convert("L")

# Image as np array
image_as_array = np.array(bw_image, dtype=int)
# print(image_as_array)

# Quantize image array
quantized_image_as_2d_array = np.floor_divide(image_as_array, quantization_value)
# print(quantized_image_as_2d_array)

# Prepare the output string
# It contains the dimensions of the image, the quantization value and the encoded image using rle separated by |
output = str(quantized_image_as_2d_array.shape[0]) + "x" + str(quantized_image_as_2d_array.shape[1]) + "|" + str(quantization_value) + "|"

# Convert 2d array to list
quantized_image_as_list = list(quantized_image_as_2d_array.flat)
# print(quantized_image_as_list)

# Encoding the array
counter = 1
current_node = quantized_image_as_list[0]
encoded_list = []
for node in quantized_image_as_list[1:]:
    if current_node == node:
        counter += 1
    else:
        encoded_list.append(str(counter) + ";" + str(current_node))
        counter = 1
        current_node = node

if counter > 0:
    encoded_list.append(str(counter) + ";" + str(current_node))

output = output + ",".join(encoded_list)

# Export string to file
file = open('compressed_mona_lisa', 'w')
file.write(output)
file.close()