import autoit
from os import system as shell

MEETING = "[CLASS:ZPContentViewWndClass]"

muted = False
autoit.opt("MouseCoordMode", 0)

def detect_mute():
    _, y = autoit.win_get_client_size(MEETING)
    autoit.mouse_move(30, y - 30, 80, y - 80, 6)
    return autoit.pixel_get_color(50, y - 50) == (0,)

def open_meeting() -> bool:
    shell("Start firefox.exe https://us05web.zoom.us/j/6453307470?pwd=c2lld1I1ZVBEZkczek1CS3libzQ5UT09#success")
    autoit.win_wait_active(MEETING)
    return True

def set_mute(value: bool):
    global muted
    if muted != value:
        autoit.win_activate(MEETING)
        autoit.send("!a")
        muted = not muted
