from PIL import Image
import numpy as np

# Open the file that contains rle encoded image as string
image_string = ""
with open('rle_compressed_image', 'r') as file:
    image_string = file.read().replace('\n', '')

# Split string at | to separated the image data
image_data = image_string.split("|")

# Split string at x, on image_data[0] and retrieve the image dimensions
image_dimensions = image_data[0].split("x")

# Retrieve the quantization value
quantization_value = int(image_data[1])

# The actual encoded image string
encoded_image = image_data[2].split(",")

# Create the array of values that represent the image
arr = []
for node in encoded_image:
    data = node.split(";")
    arr += [data[1] for _ in range(int(data[0]))]

# Reverse quantization
reverse_quantization_image = np.array(arr, dtype=int) * quantization_value

# Reshape array from 1d to 2d
image_as_2d_array = np.reshape(reverse_quantization_image, (int(image_dimensions[0]), int(image_dimensions[1])))

# Reconstruct and display image
decoded_image = Image.fromarray((image_as_2d_array).astype(np.uint8))
decoded_image.show()
