from .base import *

ALLOWED_HOSTS = ["recruit.ihopeit.com","127.0.0.1"]

LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "admin_passwd_4_ldap"
LDAP_AUTH_URL = "ldap://localhost:389"
SECRET_KEY = 'xmetn6@x_ib0lgy7bs&@bd9g_1#+jkg878txg9d$9nb)$=i^0)'
DEBUG = True
## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=xxxxx"
INSTALLED_APPS += (
    # other apps for production site
)