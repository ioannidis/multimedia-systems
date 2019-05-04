import cv2

quantization_value = 10

# Load video
video = cv2.VideoCapture('encoded_video.mp4')

# Load the first frame of the video
success, first_frame = video.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# Set video codec
video_codec = cv2.VideoWriter_fourcc(*'XVID')

# Setup the output
output = cv2.VideoWriter('decoded_video.mp4', video_codec, int(video.get(5)), (int(video.get(3)), int(video.get(4))), False)
output.write(first_frame)

frame_num = 0

previous_frame = first_frame
while video.isOpened():
    # Skip the first frame because we load it outside the loop
    if frame_num == 0:
        success, current_frame = video.read()
        frame_num += 1
        continue

    success, current_frame = video.read()
    frame_num += 1

    if not success:
        break

    # Frame to BW
    current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Sum frames
    current_frame = previous_frame +  current_frame

    previous_frame = current_frame
    output.write(current_frame)

video.release()
output.release()
