import cv2
import numpy as np
from math import ceil

window = 16


def get_macroblocks(frame):
    old_width = frame.shape[0]
    width = fit_size(old_width)
    old_height = frame.shape[1]
    height = fit_size(old_height)

    print(width, height)
    padded_frame = np.pad(frame, ((0, width - old_width), (0, height - old_height), (0, 0)), mode='constant')

    macroblocks = []

    for h in range(0, height, window):
        for w in range(0, width, window):
            print(h,h+window,w,w+window)
            macroblock = padded_frame[h:h + window, w:w + window]
            macroblocks.append(macroblock)

    return padded_frame, macroblocks


def best_match(ref_frame, target_frame):
    pass


def fit_size(x):
    return window * ceil(x / window)


video = cv2.VideoCapture('commercial.mp4')
_, ref_frame = video.read()
_, target_frame = video.read()

padded_frame, macroblocks = get_macroblocks(ref_frame)

while True:
    cv2.imshow('test', ref_frame)

    if cv2.waitKey(0):
        break


video.release()
cv2.destroyAllWindows()
