from PIL import Image
import numpy as np

image_string = ""
with open('compressed_mona_lisa', 'r') as file:
    image_string = file.read().replace('\n', '')

a = image_string.split("|")
print(a)
image_dimensions = a[0].split("x")
quantization_value = a[1]

encoded_image = a[2].split(",")

print(encoded_image)

# Solution 3
arr = []
for node in encoded_image:
    data = node.split(";")
    arr += [data[1] for _ in range(int(data[0]))]

print(arr)

reverse_quantization_image = np.array(arr, dtype=int) * 10

print(len(arr))

image_as_2d_array = np.reshape(reverse_quantization_image, (int(image_dimensions[0]), int(image_dimensions[1])))

print(image_as_2d_array)

decoded_image = Image.fromarray(image_as_2d_array)
decoded_image.show()
