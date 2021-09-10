/*#pragma once
//#include "sdk_util.h"
#include "UIlib.h"
#include "resource.h"
#include "LOGIN_login_with_email_workflow.h"

class CSDKLoginWithEmailUIGroup
{
public:
	CSDKLoginWithEmailUIGroup();
	virtual ~CSDKLoginWithEmailUIGroup();
	void InitWindow(CPaintManagerUI& ui_mgr, CSDKLoginUIMgr* main_frame_);
	void UninitWindow();
	void Show();
	void Hide();
	bool LogOut();
	void Notify(TNotifyUI& msg);

	void DoLoginWithEmailBtnClick();

protected:
	CVerticalLayoutUI* m_loginWithEmailPage;
	CRichEditUI* m_editUserAccount;
	CRichEditUI* m_editUserPassword;
	CButtonUI* m_btnLogin;
	CCheckBoxUI* m_chkRemember;
	CSDKLoginUIMgr* m_parentFrame;
	CSDKLoginWithEmailFlow   m_loginEmailWorkFlow;
public:
	CVerticalLayoutUI* m_login_bottom;
};


class CSDKLoginUIMgr :
	public CWindowWnd,
	public INotifyUI
{
public:
	CSDKLoginUIMgr();
	virtual ~CSDKLoginUIMgr();

	//void SetEvent(CSDKDemoAppEvent* pAppEvent);
public:
	virtual LPCTSTR		GetWindowClassName() const { return _T("zSDKDemoUI"); }
	UINT GetClassStyle() const { return UI_CLASSSTYLE_FRAME | CS_DBLCLKS; };
	//virtual UINT		GetSkinRes() { return IDXML_LOGINFRAME_UI; };
	//UILIB_RESOURCETYPE GetResourceType() const { return UILIB_RESOURCE; }

	virtual void		InitWindow();
	virtual void		OnFinalMessage(HWND) {}

	virtual void		Notify(TNotifyUI& msg);
	virtual LRESULT		HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam);

	*/
	//LRESULT OnClose(UINT /*uMsg*/, WPARAM /*wParam*/, LPARAM /*lParam*/, BOOL& /*bHandled*/);
	//LRESULT OnDestroy(UINT /*uMsg*/, WPARAM /*wParam*/, LPARAM /*lParam*/, BOOL& /*bHandled*/);
/*
	void SwitchToWaitingPage(const wchar_t* waiting_message, bool show);
	void ShowErrorMessage(const wchar_t* error_message);
	//void SwitchToPage(loginTabPage nPage);

	//CSDKDemoAppEvent* GetAppEvent();
	void SetCurrentPage(CVerticalLayoutUI* current_) { m_currentPage = current_; }

	bool LogOut();
	void ChangeUIforLoginFailed();
	void ChangeUIforJoinFailed();

	void NotifyAuthDone();
	//void EnableEmailLoginUI(bool, SwitchToLoginUIType);

protected:
	CPaintManagerUI m_PaintManager;
	CSDKLoginWithEmailUIGroup m_LoginWithEmailUIGroup;
	//CSDKLoginWithSSOUIGroup m_LoginWithSSOUIGroup;
	//CSDKWithoutLoginStartJoinMeetingUIGroup m_WithoutLoginStartJoinMeetingUIGroup;
	//CSDKRestAPIUserUIGroup m_RestAPIUserUIGroup;
	//CSDKLoginCBHandler     m_LoginCBHandler;
	//CSDKDemoAppEvent* m_pAppEvent;
	CVerticalLayoutUI* m_waitingPage;
	CLabelUI* m_waitingLabelUI;
	CGifAnimUI* m_gifWaiting;
	CVerticalLayoutUI* m_currentPage;

	COptionUI* m_btnLoginWithEmail;
	COptionUI* m_btnRestAPI;
	COptionUI* m_btnLoginWithSSO;
	COptionUI* m_btnJoinMeetingOnly;
	CVerticalLayoutUI* m_panel_login_content;

	CVerticalLayoutUI* m_email_login_page;
	CVerticalLayoutUI* m_sso_login_page;
	CVerticalLayoutUI* m_restApi_login_page;
	CVerticalLayoutUI* m_only_join_page;
};*/

