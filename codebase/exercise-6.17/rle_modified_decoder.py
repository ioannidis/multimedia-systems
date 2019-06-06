from PIL import Image
import numpy as np
import cv2

DECODED_FRAMES_PATH = "./decoded_video_frames"

images_string = ""
with open('compressed_mona_lisa', 'r') as file:
    images_string = file.read().replace('\n', '')

encoded_images_list = images_string[:-1].split("#")

video_dimensions = []

count = 0
for image_string in encoded_images_list:

    image_data = image_string.split("|")
    image_dimensions = image_data[0].split("x")
    if (count == 0):
        video_dimensions.append(image_dimensions[1])
        video_dimensions.append(image_dimensions[0])

    quantization_value = image_data[1]

    encoded_image = image_data[2].split(",")

    arr = []
    for node in encoded_image:
        data = node.split(";")
        arr += [data[1] for _ in range(int(data[0]))]

    reverse_quantization_image = np.array(arr, dtype=int) * 10

    image_as_2d_array = np.reshape(reverse_quantization_image, (int(image_dimensions[0]), int(image_dimensions[1])))

    decoded_image = Image.fromarray(image_as_2d_array)
    decoded_image.convert('RGB').save(DECODED_FRAMES_PATH + "/frame_%d.jpg" % count)

    count += 1

video_codec = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter("video.avi", video_codec, 30,(int(video_dimensions[0]), int(video_dimensions[1])))

for i in range(count):
    a = cv2.imread(DECODED_FRAMES_PATH + "/frame_" + str(i) + ".jpg")
    video.write(a)

video.release()
