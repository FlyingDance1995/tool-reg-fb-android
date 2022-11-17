import time

from get_content_text_from_screen.get_content_text import get_content_text_from_screen
from help.adb_helper import adb_click


def refuse_fb_access_phone_and_contacts(device_id):
    text_deny_fb_allow_contacts_and_phone = get_content_text_from_screen(device_id)
    print("text_deny_fb_allow_contacts_and_phone: ", text_deny_fb_allow_contacts_and_phone)
    if "Contacts" and "Phone" in text_deny_fb_allow_contacts_and_phone \
            or "Ngudi lién hé" and "Dién thoai" in text_deny_fb_allow_contacts_and_phone:
        adb_click(device_id, 360, 900)
        time.sleep(1)
    elif "TUCHOI" in text_deny_fb_allow_contacts_and_phone or "DENY" in text_deny_fb_allow_contacts_and_phone:
        adb_click(device_id, 360, 915)
        time.sleep(1)
    elif "hoangvtc1127@gmail.com" in text_deny_fb_allow_contacts_and_phone:
        adb_click(device_id, 350, 800)
        time.sleep(2)
    else:
        adb_click(device_id, 350, 750)
        time.sleep(2)
        adb_click(device_id, 350, 750)
        time.sleep(2)


# refuse_fb_access_phone_and_contacts("emulator-5554")
