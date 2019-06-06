from PIL import Image
import numpy as np

image_string = ""
with open('compressed_mona_lisa', 'r') as file:
    image_string = file.read().replace('\n', '')

image_data = image_string.split("|")

image_dimensions = image_data[0].split("x")
quantization_value = image_data[1]

encoded_image = image_data[2].split(",")

arr = []
for node in encoded_image:
    data = node.split(";")
    arr += [data[1] for _ in range(int(data[0]))]

reverse_quantization_image = np.array(arr, dtype=int) * 10

image_as_2d_array = np.reshape(reverse_quantization_image, (int(image_dimensions[0]), int(image_dimensions[1])))

decoded_image = Image.fromarray(image_as_2d_array)
decoded_image.show()
