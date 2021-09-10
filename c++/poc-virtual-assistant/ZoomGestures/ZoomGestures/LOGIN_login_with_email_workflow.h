/*#pragma once

#include "UIlib.h"
#include "resource.h"

#include "zoom_sdk_def.h"
#include "zoom_sdk.h"
#include "auth_service_interface.h"
using namespace ZOOM_SDK_NAMESPACE;
/////////////////////////

class CSDKLoginWithEmailFlow
{
public:
	CSDKLoginWithEmailFlow();
	virtual ~CSDKLoginWithEmailFlow();

	ZOOM_SDK_NAMESPACE::SDKError Login(ZOOM_SDK_NAMESPACE::LoginParam& param);
	ZOOM_SDK_NAMESPACE::SDKError LogOut();
	void setAuthService(ZOOM_SDK_NAMESPACE::IAuthService* authservice) {};
	void Cleanup(){}
protected:
	ZOOM_SDK_NAMESPACE::IAuthService* m_pAuthService;
};
*/