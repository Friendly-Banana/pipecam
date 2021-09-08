from collections import deque
from enum import Enum, IntEnum
from typing import NamedTuple
from math import sqrt

import mediapipe as mp

from config import EXTRA_MAX_DISTANCE, GESTURE_TRESHOLD, POS_TO_KEEP

HandLandmark = mp.solutions.hands.HandLandmark


class Hand(str, Enum):
    LEFT = "Left"
    RIGHT = "Right"


class Action(IntEnum):
    NONE = 0
    MICRO_ON = 1
    MICRO_OFF = 2
    EXTRA = 3


class Vec2D(NamedTuple):
    x: float
    y: float

    @staticmethod
    def zero():
        return Vec2D(0, 0)

    def __bool__(self) -> bool:
        return bool(self.x) or bool(self.y)

    def sqr_distance(self, other) -> float:
        return abs((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance(self, other) -> float:
        return sqrt(self.sqr_distance(other))


EXTRA_POINTS = HandLandmark.INDEX_FINGER_DIP, HandLandmark.INDEX_FINGER_MCP, HandLandmark.INDEX_FINGER_PIP, HandLandmark.INDEX_FINGER_TIP, HandLandmark.THUMB_CMC, HandLandmark.THUMB_IP, HandLandmark.THUMB_MCP, HandLandmark.THUMB_TIP

last_pos_left = deque(maxlen=POS_TO_KEEP)
last_pos_right = deque(maxlen=POS_TO_KEEP)
extra_hands = {hand: (Vec2D.zero(), Vec2D.zero()) for hand in Hand}


def update_positions(hand_landmarks, hand: Hand) -> None:
    # avg
    new_pos = sum(
        hand_landmarks.landmark[pos].x for pos in HandLandmark) / len(HandLandmark)
    # correct hand
    if hand == Hand.LEFT:
        last_pos_left.append(new_pos)
    else:
        last_pos_right.append(new_pos)
    # extra
    extra_hands[hand] = [Vec2D(hand_landmarks.landmark[lm].x, hand_landmarks.landmark[lm].y)
                         for lm in (HandLandmark.INDEX_FINGER_TIP, HandLandmark.THUMB_TIP)]


def get_mov(hand: Hand) -> float:
    last_pos = last_pos_left if hand == Hand.LEFT else last_pos_right
    delta_mov = 0
    for i in range(1, len(last_pos)):
        delta_mov += last_pos[i] - last_pos[i-1]
    return delta_mov


def change_micro(value):
    if abs(value) > GESTURE_TRESHOLD:
        # moving to the right
        if value > 0:
            return Action.MICRO_OFF
        else:
            return Action.MICRO_ON


def extra():
    r_index, r_thumb = extra_hands[Hand.RIGHT]
    l_index, l_thumb = extra_hands[Hand.LEFT]
    if r_index and l_index and r_index.distance(l_index) < EXTRA_MAX_DISTANCE and r_thumb.distance(l_thumb) < EXTRA_MAX_DISTANCE and r_thumb.y < r_index.y:
        return Action.EXTRA


def action() -> Action:
    actions = change_micro(
        get_mov(Hand.RIGHT)), change_micro(get_mov(Hand.LEFT)), extra()
    for action in actions:
        if action:
            return action
    return Action.NONE
