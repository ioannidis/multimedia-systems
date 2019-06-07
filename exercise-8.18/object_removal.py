import cv2

from functions import frame_to_macroblocks, macroblocks_to_frame

# Load the video to process macroblocks.
video = cv2.VideoCapture('../videos/video2.mp4')

has_prev = False
ms_prev_16 = None
ms_prev_8 = None
ms_prev_4 = None

while video.isOpened():
    success, frame = video.read()

    # Break if the video has ended.
    if not success:
        break

    # Extract macroblocks with size 16, 8 and 4.
    ms_16 = frame_to_macroblocks(frame, window=16)
    ms_8 = frame_to_macroblocks(frame, window=8)
    ms_4 = frame_to_macroblocks(frame, window=4)

    # Keep previous macroblocks except from the first iteration.
    if not has_prev:
        has_prev = True
        ms_prev_16 = ms_16
        ms_prev_8 = ms_8
        ms_prev_4 = ms_4
        continue

    # Replace macroblocks to hide motion.
    for i in range(9, 22):
        ms_16[i] = ms_prev_16[i]

    for j in range(19, 45):
        ms_8[j] = ms_prev_8[j]

    for k in range(39, 91):
        ms_4[k] = ms_prev_4[k]

    ms_frame_16 = macroblocks_to_frame(ms_16)
    ms_frame_8 = macroblocks_to_frame(ms_8)
    ms_frame_4 = macroblocks_to_frame(ms_4)

    # Show all four frames and modifications.
    cv2.imshow('Original Video', frame)
    cv2.imshow('Object removal (window=16)', ms_frame_16)
    cv2.imshow('Object removal (window=8)', ms_frame_8)
    cv2.imshow('Object removal (window=4)', ms_frame_4)

    # Keep previous macroblocks.
    ms_prev_16 = ms_16
    ms_prev_8 = ms_8
    ms_prev_4 = ms_4

    cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()
