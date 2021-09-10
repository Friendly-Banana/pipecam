#include "YourAuthServiceEventListener.h"
class YourAuthServiceEventListener :
    public ZOOM_SDK_NAMESPACE::IAuthServiceEvent
{
    void onAuthenticationReturn(ZOOM_SDK_NAMESPACE::AuthResult ret) {
        
    }
};