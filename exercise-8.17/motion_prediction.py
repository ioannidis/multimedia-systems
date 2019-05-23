import cv2
import numpy as np
from math import ceil

window = 16


def get_macroblocks(frame):
    old_width = frame.shape[0]
    width = fit_size(old_width)
    old_height = frame.shape[1]
    height = fit_size(old_height)

    width_pad = (0, width - old_width)
    height_pad = (0, height - old_height)
    depth_pad = (0, 0)
    padding = (width_pad, height_pad, depth_pad)

    padded_frame = np.pad(frame, padding, mode='constant')

    macroblocks = []

    for r in range(0, width - window, window):
        for c in range(0, height - window, window):
            macroblock = padded_frame[r:r + window, c:c + window]
            macroblocks.append(macroblock)

    return macroblocks


def get_sad(macroblock_prev, macroblock_next):
    colors_sad = []

    for i in range(window):
        for j in range(window):
            pixel_prev = macroblock_prev[i, j]
            pixel_next = macroblock_next[i, j]

            for k in range(3):
                color_prev = pixel_prev[k]
                color_next = pixel_next[k]
                sad = abs(color_next - color_prev)
                colors_sad.append(sad)

    sums = sum(colors_sad)
    count = len(colors_sad)
    sad = sums / count

    return sad


def fit_size(x):
    return window * ceil(x / window)


video = cv2.VideoCapture('commercial2.mp4')
_, ref_frame = video.read()
_, target_frame = video.read()

macroblocks_prev = get_macroblocks(ref_frame)
macroblocks_next = get_macroblocks(target_frame)

macroblock_count = len(macroblocks_prev)

for i in range(macroblock_count):
    print(get_sad(macroblocks_prev[i], macroblocks_next[i]))

# for macroblock in macroblocks:
#     cv2.imshow('Macroblocks', macroblock)
#
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

video.release()
cv2.destroyAllWindows()
