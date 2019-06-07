import cv2
import numpy as np

from functions import frame_to_macroblocks, get_best_match

video = cv2.VideoCapture('../videos/video1.mp4')

_, frame_prev = video.read()
_, frame_next = video.read()

frames = np.concatenate((frame_prev, frame_next), axis=0)
cv2.imshow('First and second frame', frames)

macroblocks_prev = frame_to_macroblocks(frame_prev)
macroblocks_next = frame_to_macroblocks(frame_next)

for row, macroblocks in enumerate(macroblocks_next):
    for col, macroblock in enumerate(macroblocks):
        match = get_best_match(macroblocks_prev, row, col, macroblock)
        diff = cv2.absdiff(macroblock, match)

        padded = cv2.copyMakeBorder(macroblock, 0, 0, 0, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        match_padded = cv2.copyMakeBorder(macroblock, 0, 0, 0, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        image = np.concatenate((padded, match_padded, diff), axis=1)

        cv2.imshow('Macroblock best match', image)
        cv2.waitKey(10)

video.release()
cv2.destroyAllWindows()
