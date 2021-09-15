#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.5
 Author:         Gabriel

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here
 #include <MsgBoxConstants.au3>


OpenMeeting()
;MsgBox($MB_OK, "", "Meeting open!")

Func OpenMeeting()
	ShellExecute("$env:appdata\Zoom\bin\Zoom.exe")
EndFunc