#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.5
 Author:         Gabriel

 Script Function: Zoom via Chrome/Firefox

#ce ----------------------------------------------------------------------------
#include <AutoItConstants.au3>
#include "ZoomConstants.au3"

$muted = False

;ShellExecute("firefox.exe", $LINK)
Opt("MouseCoordMode", 0)
WinWait($MEETING)
WinActivate($MEETING)
SetMute(True)
Send($SHORTCUTS.Quit)
Quit()

Func SetMute($value)
	If $muted <> $value Then
		Send($SHORTCUTS.Mute)
	EndIf
EndFunc