/*#include "Login.h"
#include "stdafx.h"
//#include "LOGIN_sdk_login_UI.h"
#include <stdarg.h>
#include "auth_service_interface.h"
//#include "mess_info.h"

void CSDKLoginWithEmailUIGroup::InitWindow(CPaintManagerUI& ui_mgr, CSDKLoginUIMgr* main_frame_)
{
	m_loginWithEmailPage = static_cast<CVerticalLayoutUI*>(ui_mgr.FindControl(_T("panel_Login_With_Email")));
	m_editUserAccount = static_cast<CRichEditUI*>(ui_mgr.FindControl(_T("edit_user_email")));
	m_editUserPassword = static_cast<CRichEditUI*>(ui_mgr.FindControl(_T("edit_user_password")));
	m_login_bottom = static_cast<CVerticalLayoutUI*>(ui_mgr.FindControl(_T("panel_Login_Buttom")));
	m_btnLogin = static_cast<CButtonUI*>(ui_mgr.FindControl(_T("btn_login")));
	m_chkRemember = static_cast<CCheckBoxUI*>(ui_mgr.FindControl(_T("chk_remember_me")));
	m_editUserPassword = static_cast<CRichEditUI*>(ui_mgr.FindControl(_T("edit_user_password")));

	m_parentFrame = main_frame_;
}
void CSDKLoginWithEmailUIGroup::UninitWindow()
{
	m_loginEmailWorkFlow.Cleanup();
}
void CSDKLoginWithEmailUIGroup::Show()
{
	if (m_loginWithEmailPage)
	{
		m_loginWithEmailPage->SetVisible(true);
		if (NULL == m_chkRemember || NULL == m_btnLogin)
			return;
		m_chkRemember->SetVisible(true);
		m_btnLogin->SetText(L"login");
		if (m_parentFrame)
		{
			m_parentFrame->SetCurrentPage(m_loginWithEmailPage);
		}
	}

}
void CSDKLoginWithEmailUIGroup::Hide()
{
	if (m_loginWithEmailPage)
	{
		m_loginWithEmailPage->SetVisible(false);
	}

}*/