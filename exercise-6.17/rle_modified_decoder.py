from PIL import Image
import numpy as np
import cv2
import os

print("Please wait, process may take a while!")

# Storage path of the decoded video frames
DECODED_FRAMES_PATH = "./decoded_video_frames"

# Create decoded_video_frames directory
if not os.path.exists("decoded_video_frames"):
    os.makedirs("decoded_video_frames")

images_string = ""
with open('rle_compressed_frames', 'r') as file:
    images_string = file.read().replace('\n', '')

encoded_images_list = images_string[:-1].split("#")

video_dimensions = []

count = 0
for image_string in encoded_images_list:

    # Split string at | to separated the image data
    image_data = image_string.split("|")

    # Split string at x, on image_data[0] and retrieve the image dimensions
    image_dimensions = image_data[0].split("x")

    # Get image dimensions
    # They are needed for video reconstruction
    if (count == 0):
        video_dimensions.append(image_dimensions[1])
        video_dimensions.append(image_dimensions[0])

    # Retrieve the quantization value
    quantization_value = image_data[1]

    # The actual encoded image string
    encoded_image = image_data[2].split(",")

    # Create the array of values that represent the image
    arr = []
    for node in encoded_image:
        data = node.split(";")
        arr += [data[1] for _ in range(int(data[0]))]

    # Reverse quantization
    reverse_quantization_image = np.array(arr, dtype=int) * 10

    # Reshape array from 1d to 2d
    image_as_2d_array = np.reshape(reverse_quantization_image, (int(image_dimensions[0]), int(image_dimensions[1])))

    # Reconstruct and display image
    decoded_image = Image.fromarray(image_as_2d_array)
    decoded_image.convert('RGB').save(DECODED_FRAMES_PATH + "/frame_%d.jpg" % count)

    count += 1

# Merge all decoded frames and reconstruct the video
video_codec = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter("rle_modified_decoded_video.avi", video_codec, 30,(int(video_dimensions[0]), int(video_dimensions[1])))

for i in range(count):
    a = cv2.imread(DECODED_FRAMES_PATH + "/frame_" + str(i) + ".jpg")
    video.write(a)

video.release()

print("Video released as 'rle_modified_decoded_video.avi'!")
