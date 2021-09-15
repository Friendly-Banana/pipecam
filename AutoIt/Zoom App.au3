#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.5
 Author:         Gabriel

 Script Function: Zoom
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

#include <MsgBoxConstants.au3>
#include "ZoomConstants.au3"

;MsgBox($MB_OK, "Debug", $LOGGED_IN)
OpenMeeting()
Sleep(5000)
Quit()

Func OpenMeeting()
    If Not Run(EnvGet("AppData") & "\Zoom\bin\Zoom.exe") Then
		print("Please install Zoom")
		Exit
	EndIf
	print("Waiting for zoom to launch")
	Sleep(3000)
	if WinExists($NOLOGIN) <> 0 Then
		Sleep(50)
        print("No login")
		WinActivate($NOLOGIN)
        Send("{TAB}")
        Send("{ENTER}") ; press join meeting button
		WinWaitActive($JOIN_MEETING)
        Send($meetingId)
        Send("{TAB}")
        Send($username)
        Send("{SPACE}") ; toggle remember name
        For $i = 0 To 5 Step +1
            Send("{TAB}")
        Next
        Send("{ENTER}") ; press join
		WinWaitActive($ENTER_MEETING_PASSWORD)
        Send($password)
		Send("{TAB}")
        Send("{ENTER}")
		local $wait_tries = 2
        Do
            print("Waiting for Meeting to start")
			$wait_tries -= 1
            Sleep(3000)
        Until WinWaitActive($GDRP) <> 0 Or $wait_tries = 0
		Send("{TAB}")
		Send("{TAB}")
        Send("{ENTER}")
		print("Entered Meeting")
    ElseIf WinExists($LOGGED_IN) <> 0 Then
        print("Zoom Account")
        For $i = 0 To 6 Step +1
			Sleep(30) ; prevent key being recognized as being held
            Send("{TAB}")
        Next
        Send("{ENTER}")
    EndIf
EndFunc
