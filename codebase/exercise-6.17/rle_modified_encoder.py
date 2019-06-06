from PIL import Image
import numpy as np
import cv2
import os

FRAMES_PATH = "./video_frames"

if not os.path.exists("video_frames"):
    os.makedirs("video_frames")

# Load video
video = cv2.VideoCapture('../videos/video1.mp4')

# Load the first frame of the video
success, first_frame = video.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite(FRAMES_PATH + "/frame_%d.jpg" % 0, first_frame)

count = 1
while video.isOpened():
    success, current_frame = video.read()

    if success == False:
      break

    current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # save frame as JPEG file
    cv2.imwrite(FRAMES_PATH + "/frame_%d.jpg" % count, current_frame)
    count += 1

# Encode images
quantization_value = 10
output =  ""

for i in range(count):
    # Open image
    bw_image = Image.open(FRAMES_PATH + "/frame_%d.jpg" % i)

    # Image as np array
    image_as_array = np.array(bw_image, dtype=int)
    # print(image_as_array)

    # Quantize image array
    quantized_image_as_2d_array = np.floor_divide(image_as_array, quantization_value)
    # print(quantized_image_as_2d_array)

    # Prepare the output string
    # It contains the dimensions of the image, the quantization value and the encoded image using rle separated by |
    encoded_image = str(quantized_image_as_2d_array.shape[0]) + "x" + str(quantized_image_as_2d_array.shape[1]) + "|" + str(quantization_value) + "|"

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

    output += encoded_image + ",".join(encoded_list) + "#"

# Export string to file
file = open('compressed_mona_lisa', 'w')
file.write(output)
file.close()