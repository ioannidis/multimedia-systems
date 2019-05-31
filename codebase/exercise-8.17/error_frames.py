import cv2
import pkg_resources

if __name__ == '__main__':
    file = pkg_resources.resource_filename(__name__, '../videos/video1.mp4')
    video = cv2.VideoCapture(file)

    prev_frame = None

    while video.isOpened():
        success, cur_frame = video.read()

        if not success:
            break

        if prev_frame is None:
            prev_frame = cur_frame.copy()
            continue

        error_frame = cv2.absdiff(cur_frame, prev_frame)
        cv2.imshow('Error Frames', error_frame)

        cv2.waitKey(60)

        prev_frame = cur_frame.copy()

    video.release()
    cv2.destroyAllWindows()
