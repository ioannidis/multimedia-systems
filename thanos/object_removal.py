import cv2
from functions import frame_to_macroblocks, macroblocks_to_frame
import numpy as np

if __name__ == '__main__':
    video = cv2.VideoCapture('video1.mp4')

    _, start_frame = video.read()

    macroblocks_start = frame_to_macroblocks(start_frame)

    while video.isOpened():
        _, frame = video.read()

        if frame is None:
            break

        macroblocks = frame_to_macroblocks(frame)
        macroblocks_edited = macroblocks.copy()

        macroblocks_edited[9] = macroblocks_start[9]
        macroblocks_edited[10] = macroblocks_start[10]
        macroblocks_edited[11] = macroblocks_start[11]
        macroblocks_edited[12] = macroblocks_start[12]
        macroblocks_edited[13] = macroblocks_start[13]
        macroblocks_edited[14] = macroblocks_start[14]
        macroblocks_edited[15] = macroblocks_start[15]
        macroblocks_edited[16] = macroblocks_start[16]
        macroblocks_edited[17] = macroblocks_start[17]
        macroblocks_edited[18] = macroblocks_start[18]
        macroblocks_edited[19] = macroblocks_start[19]
        macroblocks_edited[20] = macroblocks_start[20]
        macroblocks_edited[21] = macroblocks_start[21]

        before = macroblocks_to_frame(macroblocks)
        after = macroblocks_to_frame(macroblocks_edited)

        image = np.concatenate((before, after), axis=1)

        cv2.imshow('Frame', image)

        cv2.waitKey(30)

    video.release()
    cv2.destroyAllWindows()
