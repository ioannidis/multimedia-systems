import cv2
import numpy as np
from codebase.functions import frame_to_macroblocks, macroblocks_to_frame

if __name__ == '__main__':
    video = cv2.VideoCapture('../videos/video2.mp4')

    macroblocks_prev = None

    while video.isOpened():
        _, frame = video.read()

        if frame is None:
            break

        macroblocks = frame_to_macroblocks(frame)
        macroblocks_original = macroblocks.copy()

        if macroblocks_prev is None:
            macroblocks_prev = macroblocks
            continue

        macroblocks[9] = macroblocks_prev[9]
        macroblocks[10] = macroblocks_prev[10]
        macroblocks[11] = macroblocks_prev[11]
        macroblocks[12] = macroblocks_prev[12]
        macroblocks[13] = macroblocks_prev[13]
        macroblocks[14] = macroblocks_prev[14]
        macroblocks[15] = macroblocks_prev[15]
        macroblocks[16] = macroblocks_prev[16]
        macroblocks[17] = macroblocks_prev[17]
        macroblocks[18] = macroblocks_prev[18]
        macroblocks[19] = macroblocks_prev[19]
        macroblocks[20] = macroblocks_prev[20]
        macroblocks[21] = macroblocks_prev[21]

        before = macroblocks_to_frame(macroblocks_original)
        after = macroblocks_to_frame(macroblocks)
        image = np.concatenate((before, after), axis=1)

        macroblocks_prev = macroblocks
        cv2.imshow('Before and after frames', image)
        cv2.waitKey(30)

    video.release()
    cv2.destroyAllWindows()
