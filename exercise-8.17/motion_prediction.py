import cv2
import numpy as np

macroblock_width = 16
macroblock_height = 16


def get_macroblocks(frame):
    pass


def best_match(ref_frame, target_frame):
    pass


video = cv2.VideoCapture('commercial.mp4')
_, ref_frame = video.read()
_, target_frame = video.read()

best_match(ref_frame, target_frame)

video.release()
cv2.destroyAllWindows()
