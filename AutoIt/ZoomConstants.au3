#include <StringConstants.au3>
#include <Array.au3>
#include-once
; Zoom Window Titles
Const $LOGGED_IN = "Zoom"
Const $NOLOGIN = "Zoom Cloud Meetings"
Const $JOIN_MEETING = "[CLASS:zWaitHostWndClass]"
Const $ENTER_MEETING_PASSWORD = "Enter meeting passcode"
Const $WAITING_HOST = "Waiting for Host"
Const $GDRP = "[REGEXPCLASS:(zGDPRWndClass.*)]"
Const $CONFIRM_LEAVE = "End Meeting or Leave Meeting?"
Const $MEETING = "[CLASS:ZPContentViewWndClass]"

Const $ALL_WINDOW_TITLES = [$LOGGED_IN, $NOLOGIN, $JOIN_MEETING, $ENTER_MEETING_PASSWORD, $WAITING_HOST, $GDRP, $CONFIRM_LEAVE, $MEETING]

Const $JOIN_AUDIO[] = [250, 115]

Const $username = "dev"
Const $meetingId = "6453307470"
Const $password = "c2lld1I1ZVBEZkczek1CS3libzQ5UT09"
Const $LINK = "https://us05web.zoom.us/j/6453307470?pwd=c2lld1I1ZVBEZkczek1CS3libzQ5UT09#success"

; Key shortcuts for Zoom
Global $SHORTCUTS[]
For $name In StringSplit("Mute a|Video v|Share s|Participants u|Chat h|Quit q|Record r", "|", $STR_NOCOUNT)
	$t = StringSplit($name, " ", $STR_NOCOUNT)
	$SHORTCUTS[$t[0]] = "!" & $t[1]
Next

Func print($param)
	if IsArray($param) Then
		ConsoleWrite(_ArrayToString($param, ", ") & @LF)
	Else
		ConsoleWrite($param & @LF)
	EndIf
EndFunc


Func Quit()
    print("Quitting...")
    For $title In $ALL_WINDOW_TITLES
        WinClose($title)
    Next
EndFunc