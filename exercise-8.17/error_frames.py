import cv2

# Load the video to process each frame.
video = cv2.VideoCapture('../videos/video1.mp4')

prev_frame = None

while video.isOpened():
    success, cur_frame = video.read()

    # Break if the video has ended.
    if not success:
        break

    # Keep the previous frame except on first iteration.
    if prev_frame is None:
        prev_frame = cur_frame.copy()
        continue

    # Show the difference between the current and the previous frame.
    error_frame = cv2.absdiff(cur_frame, prev_frame)
    cv2.imshow('Error Frames', error_frame)
    cv2.waitKey(60)

    # Keep the previous frame.
    prev_frame = cur_frame.copy()

video.release()
cv2.destroyAllWindows()
