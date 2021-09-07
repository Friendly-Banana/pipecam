from collections import deque
from config import GESTURE_TRESHOLD, POS_TO_KEEP
from enum import Enum, IntEnum
import mediapipe as mp
HandLandmarks = mp.solutions.hands.HandLandmark


class Hand(str, Enum):
    LEFT = "Left"
    RIGHT = "Right"

class Action(IntEnum):
    NONE = 0
    MICRO_ON = 1
    MICRO_OFF = 2


last_pos_left = deque(maxlen=POS_TO_KEEP)
last_pos_right = deque(maxlen=POS_TO_KEEP)


def update_positions(hand_landmarks, hand: Hand) -> None:
    # avg
    new_pos = sum(
        hand_landmarks.landmark[pos].x for pos in HandLandmarks) / len(HandLandmarks)
    # correct hand
    if hand == Hand.LEFT:
        last_pos_left.append(new_pos)
    else:
        last_pos_right.append(new_pos)


def get_mov(hand: Hand) -> float:
    last_pos = last_pos_left if hand == Hand.LEFT else last_pos_right
    delta_mov = 0
    for i in range(1, len(last_pos)):
        delta_mov += last_pos[i] - last_pos[i-1]
    return delta_mov


def action(value) -> Action:
    if abs(value) > GESTURE_TRESHOLD:
        # moving to the right
        if value > 0:
            return Action.MICRO_OFF
        else:
            return Action.MICRO_ON
    return Action.NONE
