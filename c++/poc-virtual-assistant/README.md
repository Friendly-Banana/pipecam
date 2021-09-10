# poc-virtual-assistant
This project is a proof of concept of how you can programmatically control a zoom client using the C++ SDK with Visual Studio on Windows.

## Usage
1. Follow this guide https://marketplace.zoom.us/docs/sdk/native-sdks/introduction to create an SDK app.
2. Generate a JWT-token. Every time you use the SDK, you need to authenticate your App with such a token. You can find a guide on how to generate the token manually here: https://zoomdevelopersupport.zendesk.com/hc/en-us/articles/360056168291-How-to-create-a-sample-JWT-for-the-Client-SDK.
3. Paste the token in _AuthorizeSDK()_ (line 164).
4. In _joinMeetingForEndUser()_, set the meeting number and password of an existing meeting (lines 288 & 290).
4. Have you set the run options of Visual Studio to "release" and "x86" as required by the introduction guide?
5. Run the application. It will automatically authenticate the SDK. If successful, it will output "AUTH SUCCESSFUL".
6. You can now login (_Datei_ - _Login_). Enter your zoom email and password.
7. Join a meeting (_Datei_ - _Verbinden_). (Should work even without being logged in, in which case you will need to enter the password.)
8. Toggle your mute status (_Datei_ - _Mute/Unmute_).

## Findings
The most important takeaway: **You can't hijack a running zoom meeting and control it.** You need to join a zoom meeting using the SDK methods if you want to control anything like your audio status. From this I would conclude that as a minimum requirement, a lightweight application needs to be developed for every major platform, that asks for a username, password, meeting ID and meeting password. Developing any further custom UI is not needed, as you will see the default zoom UI when joining a meeting via the SDK (you are able to customize it though).

Further Notes:
- Since the zoom client SDK is not the most popular one (and is available for seven platforms), finding solutions is not as easy as in other cases.
- There is no official Linux support yet.
- The official guide for joining or starting meetings with the SDK is incomplete. Setting only the parameters of _StartParam4NormalUser_/_JoinParam4NormalUser_ as shown in the guide will lead to an error. You need to set every parameter (or at least: there is some parameter that needs to be set which is not set in the guide).
- In an actual application, the token needs to be generated in some backend.
- You can't create new meetings with the client SDK.

## DISCLAIMER
I don't know much about C++. If you intend to use any of this code, check for things like memory leaks. Be aware that if you don't call the functions in the right order, you will probably run into uninitialized variables.
