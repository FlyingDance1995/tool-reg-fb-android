import os

DEVICE_ID_SSA7 = '14d9cef2'  # sm A700h
DEVICE_ID_REDMI9 = '00179b6a0411'  # redmi 9
DEVICE_ID_SSJ5 = "f521da0e"
IP = '192.168.200.3:10000'
PROXY_SSA7 = '192.168.200.3:4002'
PROXY_EMULATOR_5554 = '192.168.200.3:4002'
PROXY_SSJ5 = '192.168.200.3:4005'
PASS_FB_BOT = "!Hqwe123@#@#"
CURRENT_PROXY = os.environ.get("CURRENT_PROXY", 'TIN_SOFT_PROXY')
PUSH_PROXY_IP_SSA7 = 'adb -s 14d9cef2 shell settings put global http_proxy'
PUSH_PROXY_IP_SSJ5 = 'adb -s f521da0e shell settings put global http_proxy'
ADB_COMMAND_TOKEN = 'su -c cat /data/data/com.facebook.katana/app_light_prefs/com.facebook.katana/authentication'
ADB_COMMAND_TOKEN_EMULATOR_5554 = 'adb -s emulator-5554 shell "cat /data/data/com.facebook.katana/app_light_prefs/com.facebook.katana/authentication"'
ADB_COMMAND_PULL_FILE_SSA7 = f'adb -s {DEVICE_ID_SSA7} pull system/build.prop'
ADB_COMMAND_PULL_FILE_SSJ5 = f'adb -s {DEVICE_ID_SSJ5} pull system/build.prop'
ADB_COMMAND_PULL_FILE_EMULATOR_5554 = f'adb -s emulator-5554 pull system/build.prop'
ADB_COMMAND_VERSION_NAME_SSA7 = f'adb -s {DEVICE_ID_SSA7} shell "dumpsys package com.facebook.katana | grep versionName"'
ADB_COMMAND_VERSION_NAME_SSJ5 = f'adb -s {DEVICE_ID_SSJ5} shell "dumpsys package com.facebook.katana | grep versionName"'
ADB_COMMAND_VERSION_NAME_EMULATOR_5554 = f'adb -s emulator-5554 shell "dumpsys package com.facebook.katana | grep versionName"'
ADB_COMMAND_VERSION_CODE_SSA7 = f'adb -s {DEVICE_ID_SSA7} shell "dumpsys package com.facebook.katana | grep versionCode"'
ADB_COMMAND_VERSION_CODE_SSJ5 = f'adb -s {DEVICE_ID_SSJ5} shell "dumpsys package com.facebook.katana | grep versionCode"'
ADB_COMMAND_VERSION_CODE_EMULATOR_5554 = f'adb -s emulator-5554 shell "dumpsys package com.facebook.katana | grep versionCode"'
ADB_COMMAND_PUSH_SSA7 = f'adb -s {DEVICE_ID_SSA7} push ./build.prop /data/local/tmp/'
ADB_COMMAND_PUSH_SSJ5 = f'adb -s {DEVICE_ID_SSJ5} push ./build.prop /data/local/tmp/'
ADB_COMMAND_PUSH_EMULATOR_5554 = f'adb -s emulator-5554 push ./build.prop /data/local/tmp/'
ADB_COMMAND_ROOT_SSA7 = f'adb -s {DEVICE_ID_SSA7} shell su'
ADB_COMMAND_ROOT_SSJ5 = f'adb -s {DEVICE_ID_SSJ5} shell su'
ADB_COMMAND_ROOT_EMULATOR_5554 = f'adb -s emulator-5554 shell su'
ADB_COMMAND_AUTHENTICATION_SYSTEM = 'mount -o rw,remount /system'
ADB_COPY = 'cp -r /data/local/tmp/build.prop /system/build.prop'
ADB_CLEAR_REDMI9 = f'adb -s {DEVICE_ID_REDMI9} shell pm clear com.facebook.katana'
ADB_CLEAR_SSA7 = f'adb -s 14d9cef2 shell pm clear com.facebook.katana'
ADB_CLEAR_SSJ5 = f'adb -s {DEVICE_ID_SSJ5} shell pm clear com.facebook.katana'
ADB_CLEAR_EMULATOR_5554 = f'adb -s emulator-5554 shell pm clear com.facebook.katana'

TM_PROXY = {
    'SERVER': os.environ.get("TM_PROXY_SERVER", "https://tmproxy.com/api/proxy"),
    "API_KEYS": [x for x in os.environ.get("TM_PROXY_API_KEYS", "ed6551958ffce04cccf1bbbfc71cd194").split(",")],
}

TIN_SOFT_PROXY = {
    'SERVER': os.environ.get("TM_PROXY_SERVER", "https://tinsoftproxy.com/"),
    "API_KEYS": [x for x in os.environ.get("TIN_SOFT_PROXY_API_KEYS", "TLorBvJYL0SN6L4SrAxzjtQTaESb09YZbeuRH6").split(",")],
}

# coordinates
COORDINATES_APP_X = '135'
COORDINATES_APP_Y = '225'  # toa do cua app tren man hinh dien thoai

COORDINATES_REGISTER_BUTTON_X = '500'
COORDINATES_REGISTER_BUTTON_Y = '1700'  # toa do cua nut tao tai khoan

COORDINATES_CONTINUE_BUTTON_X = '500'
COORDINATES_CONTINUE_BUTTON_Y = '1350'  # toa do cua nut tiep tuc

COORDINATES_REFUSE_BUTTON_X = '500'
COORDINATES_REFUSE_BUTTON_Y = '1150'  # toa do cua nut tu choi cho phep Facebook thuc hien va quan ly cuoc goi den,\
# truy cap danh ba

COORDINATES_NONE_OF_THE_ABOVE_BUTTON_X = '350'
COORDINATES_NONE_OF_THE_ABOVE_BUTTON_Y = '1150'  # toa do cua nut None of the above


ADB_TURN_OFF_WIFI = "adb shell su -c 'svc wifi disable'"
ADB_TURN_ON_WIFI = "adb shell su -c 'svc wifi enable'"

ADB_TURN_OFF_DATA = "adb shell su -c 'svc data disable'"
ADB_TURN_ON_DATA = "adb shell su -c 'svc data enable'"


FB_BOT_SERVICE = {
    "HOST": os.environ.get("FB_BOT_SERVICE_HOST", "10.158.14.29"),
    "PORT": int(os.environ.get("FB_BOT_SERVICE_PORT", 9443)),
    "ACCOUNT_PER_PAGE": int(os.environ.get("FB_BOT_SERVICE_ACCOUNT_PER_PAGE", 200)),
    "BORN_AT_GTE": int(os.environ.get("CRAWLER_BORN_AT_GTE", 0)),
    "BORN_AT_LTE": int(os.environ.get("CRAWLER_BORN_AT_LTE", 0)),
    "MESSAGE_THRESHOLD": int(os.environ.get("CRAWLER_MESSAGE_THRESHOLD", 0))
}

