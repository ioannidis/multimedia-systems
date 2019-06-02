import cv2
import pkg_resources

from codebase.functions import frame_to_macroblocks, macroblocks_to_frame

if __name__ == '__main__':
    file = pkg_resources.resource_filename(__name__, '../videos/video2.mp4')
    video = cv2.VideoCapture(file)

    has_prev = False
    ms_prev_16 = None
    ms_prev_8 = None
    ms_prev_4 = None

    while video.isOpened():
        _, frame = video.read()

        if frame is None:
            break

        ms_16 = frame_to_macroblocks(frame, window=16)
        ms_8 = frame_to_macroblocks(frame, window=8)
        ms_4 = frame_to_macroblocks(frame, window=4)

        if not has_prev:
            has_prev = True
            ms_prev_16 = ms_16
            ms_prev_8 = ms_8
            ms_prev_4 = ms_4
            continue

        for i in range(9, 22):
            ms_16[i] = ms_prev_16[i]

        for j in range(19, 45):
            ms_8[j] = ms_prev_8[j]

        for k in range(39, 91):
            ms_4[k] = ms_prev_4[k]

        ms_frame_16 = macroblocks_to_frame(ms_16)
        ms_frame_8 = macroblocks_to_frame(ms_8)
        ms_frame_4 = macroblocks_to_frame(ms_4)

        cv2.imshow('Original Video', frame)
        cv2.imshow('Object removal (window=16)', ms_frame_16)
        cv2.imshow('Object removal (window=8)', ms_frame_8)
        cv2.imshow('Object removal (window=4)', ms_frame_4)

        ms_prev_16 = ms_16
        ms_prev_8 = ms_8
        ms_prev_4 = ms_4

        cv2.waitKey(30)

    video.release()
    cv2.destroyAllWindows()
