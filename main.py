import cv2
import mediapipe as mp
import pyvirtualcam
from os import system
from config import (MIN_DETECTION_CONFIDENCE,
                    MIN_TRACKING_CONFIDENCE)
from gestures import Action, action, update_positions
import zoom

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# restart camera
#system("sudo modprobe -r v4l2loopback && sudo modprobe v4l2loopback")
# For webcam input:
cap = cv2.VideoCapture(3)
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_fps = int(cap.get(cv2.CAP_PROP_FPS))
if cap_fps == 0:
    exit("Couldn't get camera")
print("Opening Meeting")
with mp_hands.Hands(min_detection_confidence=MIN_DETECTION_CONFIDENCE,
                    min_tracking_confidence=MIN_TRACKING_CONFIDENCE) as hands, pyvirtualcam.Camera(
        width=cap_width, height=cap_height, fps=cap_fps) as cam:
    zoom.open_meeting()
    print("Meeting entered")
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            # Punkt Positionen (x, y, z), Info
            for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                update_positions(
                    hand_landmarks, hand_info.classification[0].label)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(
                ), mp_drawing_styles.get_default_hand_connections_style())
        # recognize gesture
        to_do = action()
        if to_do == Action.MICRO_ON:
            print("Micro on")
            zoom.set_mute(False)
        elif to_do == Action.MICRO_OFF:
            print("Micro off")
            zoom.set_mute(True)
        elif to_do == Action.EXTRA:
            image = cv2.putText(image, "Guten Morgen, Frau Kanzlerin", (int(cap_width * 0.3), int(cap_height * 0.9)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        # Send image to webcam
        cam.send(cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB))
        # show image
        #cv2.imshow('PipeCam', image)
        #if cv2.waitKey(5) & 0xFF == 27:
        #    break
        # sleep to keep frame rate
        cam.sleep_until_next_frame()

cap.release()
cv2.destroyAllWindows()