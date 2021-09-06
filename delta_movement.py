from enum import Enum
import mediapipe as mp
finger_point = mp.solutions.hands.HandLandmark

class Hand(Enum):
    LEFT = "Left"
    RIGHT = "Right"

FINGERS = {"thumb": (finger_point.THUMB_MCP, finger_point.THUMB_IP, finger_point.THUMB_TIP),
          "index": (finger_point.INDEX_FINGER_PIP, finger_point.INDEX_FINGER_DIP, finger_point.INDEX_FINGER_TIP),
          "middle": (finger_point.MIDDLE_FINGER_PIP, finger_point.MIDDLE_FINGER_DIP, finger_point.MIDDLE_FINGER_TIP),
          "ring": (finger_point.RING_FINGER_PIP, finger_point.RING_FINGER_DIP, finger_point.RING_FINGER_TIP),
          "pinky": (finger_point.PINKY_PIP, finger_point.PINKY_DIP, finger_point.PINKY_TIP)
          }

positions = {key: (0,0) for key in FINGERS}


def update_positions(hand_landmarks, hand : Hand):
    liste = []
    for points in FINGERS:
        # avg
        new_pos = sum(hand_landmarks.landmark[pos].x for pos in points) / 3
        delta_mov = FINGERS[points]- new_pos
        FINGERS[points] = new_pos