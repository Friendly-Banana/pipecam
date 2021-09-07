from config import GESTURE_TRESHOLD, MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE
from delta_movement import Hand, action, get_mov, update_positions
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=MIN_TRACKING_CONFIDENCE) as hands:
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
        action_right, action_left = action(
            get_mov(Hand.RIGHT)), action(get_mov(Hand.LEFT))
        if action_right == action_left or not action_right or not action_left:
            if action_right:
                print(action_right)
            elif action_left:
                print(action_left)
        # TODO Send to webcam
        cv2.imshow('PipeCam Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cv2.destroyAllWindows()
cap.release()
