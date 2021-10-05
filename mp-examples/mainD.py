import pyvirtualcam
import numpy as np
import cv2
import signal
import sys

cap = cv2.VideoCapture(3)
cam = pyvirtualcam.Camera(width=640, height=480, fps=20, device='/dev/video7')
print(f'Using virtual camera: {cam.device}')

def signal_handler(sig, frame):
    print(cam.close())
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

while True:
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    frame.flags.writeable = False
    cam.send(frame)
    cam.sleep_until_next_frame()
