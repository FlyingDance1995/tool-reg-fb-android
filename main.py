import json
import re
import time
import subprocess
import threading

import pyautogui

from change_device_info.change_device_info import change_device_info, do_change_device, push_file
from help.adb_helper import turn_on_off_screen, adb_click
from data_name.random_name import random_last_name, random_first_name
from on_off_data_or_wifi.on_off_wifi_of_4g import on_off_wifi, off_wifi_emulator
from proxies.change_ip_proxy import change_ip_proxy_of_phone
from proxies.check_current_public_ip import check_current_public_ip, write_ip
from register_acc_fb.register_acc_fb_by_emulator_5554 import register_bot_fb_by_emulator_5554
from register_acc_fb.register_acc_fb_by_ssa7_phone import register_bot_fb_by_ssa7, choose_avatar
from settings import ADB_COMMAND_TOKEN, PASS_FB_BOT, ADB_CLEAR_SSA7, ADB_CLEAR_REDMI9, ADB_COMMAND_PULL_FILE_SSA7, \
    ADB_COMMAND_PULL_FILE_SSJ5, ADB_COMMAND_VERSION_NAME_SSJ5, ADB_COMMAND_VERSION_NAME_SSA7, \
    ADB_COMMAND_VERSION_CODE_SSA7, ADB_COMMAND_VERSION_CODE_SSJ5, ADB_CLEAR_SSJ5, ADB_COMMAND_TOKEN_EMULATOR_5554, \
    ADB_COMMAND_PULL_FILE_EMULATOR_5554, ADB_COMMAND_VERSION_NAME_EMULATOR_5554, ADB_COMMAND_VERSION_CODE_EMULATOR_5554, \
    ADB_CLEAR_EMULATOR_5554, CURRENT_PROXY
from subprocess import PIPE


class thread_creator_fb_bot(threading.Thread):
    def __init__(self, threadID, name, device_id):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.device_id = device_id

    def run(self):
        print("Starting " + self.device_id)
        process_creator_fb_bot(self.device_id)
        print("Exiting " + self.device_id)


def process_creator_fb_bot(device_id):
    n = 0
    while n < 100:
        n += 1
        time_start = int(time.time())
        if device_id != "emulator-5554":
            turn_on_off_screen(device_id)
        output_ip = change_ip_proxy_of_phone(device_id)
        if device_id != "emulator-5554":
            on_off_wifi(device_id)
        if CURRENT_PROXY == "X_PROXY":
            res_ip = check_current_public_ip()
        else:
            res_ip = output_ip
        res_str = write_ip(res_ip)
        input_last_name = random_last_name()
        input_first_name = random_first_name()
        fb_id, day, month, year, output_email, str_status, have_avatar = register_acc_fb(device_id, input_first_name, input_last_name)

        # fb_id = None
        # day = "10"
        # month = "07"
        # year = "1999"
        # output_email = "wogan56096@herrain.com"
        # str_status = "success"
        # have_avatar = "Yes"

        res_user_agent = ""
        token = None
        cookie = None
        uid = None
        if device_id == "14d9cef2" or device_id == "f521da0e" or device_id == "emulator-5554":
            uid, token, cookie = get_auth_info(device_id)

            # user-agent
            res_user_agent = get_user_agent(device_id)

        # if device_id == "14d9cef2" or device_id == "f521da0e" or device_id == "emulator-5554":
        #     # change device info
        #     res = change_device_info()
        #     do_change_device(res)
        #
        #     # push file to root android
        #     push_file(device_id)

        # Clear katana data
        clear_data(device_id)
        time.sleep(5)
        adb_click("emulator-5554", 450, 115)

        time_end = int(time.time())
        time_process = time_end - time_start
        print("time_process: ", time_process)


        # output
        if device_id == "14d9cef2" or device_id == "f521da0e" or device_id == "emulator-5554":
            write_output(device_id=device_id,
                         res_user_agent=res_user_agent,
                         fb_id=uid,
                         token=token,
                         cookie=cookie,
                         output_email=output_email,
                         day=day,
                         month=month,
                         year=year,
                         str_status=str_status,
                         time=time_process,
                         have_avatar=have_avatar,
                         res_ip=res_ip,
                         res_str=res_str)
        else:
            if fb_id is None:
                fb_id = output_email
            write_output(device_id=device_id,
                         res_user_agent=res_user_agent,
                         fb_id=fb_id,
                         token=token,
                         cookie=cookie,
                         output_email=output_email,
                         day=day,
                         month=month,
                         year=year,
                         str_status=str_status,
                         time=time_process,
                         have_avatar=have_avatar,
                         res_ip=res_ip,
                         res_str=res_str)

        if device_id != "emulator-5554":
            turn_on_off_screen(device_id)
        pyautogui.countdown(10)
        # time.sleep(10)


def register_acc_fb(device_id, first_name, last_name):
    if device_id == "14d9cef2":
        str_day, str_month, str_year, email, status, have_avatar = register_bot_fb_by_ssa7(device_id, first_name, last_name)
        return None, str_day, str_month, str_year, email, status, have_avatar
    elif device_id == "emulator-5554":
        str_day, str_month, str_year, email, status, have_avatar = register_bot_fb_by_emulator_5554(device_id, first_name, last_name)
        return None, str_day, str_month, str_year, email, status, have_avatar
    # elif device_id == "f521da0e":
    #     str_day, str_month, str_year, email, status = register_bot_fb_by_ssj5(device_id, first_name, last_name)
    #     return None, str_day, str_month, str_year, email, status
    # else:
    #     pass


def get_auth_info(device_id):
    user_name = None
    token = None
    cookie = None
    if device_id == "emulator-5554":
        adb_command_token = ADB_COMMAND_TOKEN_EMULATOR_5554
    else:
        adb_command_token = f'adb -s {device_id} shell "' + ADB_COMMAND_TOKEN + '"'
    try:
        result = subprocess.run(adb_command_token, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print('result adb_command_token: ' + str(result.stdout))
    except Exception as e:
        print('Something went wrong when run adb_command_token: ', e)

    if result.returncode == 0:
        auth = result.stdout
        user_name = re.findall(r'uid(.*)session_key', auth)
        user_name = user_name[0] if len(user_name) > 0 else ''
        user_name = re.sub("[^0-9]+", '', user_name)
        print('user_name: ', user_name)
        if device_id == "emulator-5554":
            token = re.findall(r'access_token(.*)username', auth)
        else:
            token = re.findall(r'access_token(.*)analytics_claim', auth)
        token = token[0] if len(token) > 0 else ''
        token = re.sub("[^a-zA-Z0-9]+", '', token)
        print('token: ', token)

        cookie = re.findall(r'\[(.*)\]', auth)
        cookie = cookie[0] if len(cookie) > 0 else None
        if cookie:
            cookie = f'[{cookie}]'
            resp = json.loads(cookie)
            cks = []
            for ck in resp:
                cks.append(f'{ck["name"]}={ck["value"]}')
            cookie = '; '.join(cks)
        print('cookie: ', str(cookie))

    return user_name, token, cookie


def get_user_agent(device_id):
    adb_command_pull_file = ""
    if device_id == "14d9cef2":
        adb_command_pull_file = ADB_COMMAND_PULL_FILE_SSA7
    elif device_id == "f521da0e":
        adb_command_pull_file = ADB_COMMAND_PULL_FILE_SSJ5
    elif device_id == "emulator-5554":
        adb_command_pull_file = ADB_COMMAND_PULL_FILE_EMULATOR_5554
    else:
        pass
    fb_app_ver = ''
    fb_build_ver = ''

    try:
        out = subprocess.run(adb_command_pull_file, stdout=subprocess.PIPE, universal_newlines=True)
        print('out adb_command_pull_file: ' + str(out.stdout))
    except Exception as e:
        print('Something went wrong when run adb_command_pull_file: ', e)

    adb_command_version_name = ""
    if device_id == "14d9cef2":
        adb_command_version_name = ADB_COMMAND_VERSION_NAME_SSA7
    elif device_id == "f521da0e":
        adb_command_version_name = ADB_COMMAND_VERSION_NAME_SSJ5
    elif device_id == "emulator-5554":
        adb_command_version_name = ADB_COMMAND_VERSION_NAME_EMULATOR_5554
    else:
        pass
    try:
        result = subprocess.run(adb_command_version_name, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print('result adb_command_version_name: ' + str(result.stdout))
        if device_id == "f521da0e":
            fb_app_ver = result.stdout.strip().replace('versionName=', '').replace("\n", "").replace("stub", "").strip()
        else:
            fb_app_ver = result.stdout.strip().replace('versionName=', '')
        print('fb_app_ver: ' + fb_app_ver)
    except Exception as e:
        print('Something went wrong when run adb_command_version_name: ', e)

    adb_command_version_code = ""
    if device_id == "14d9cef2":
        adb_command_version_code = ADB_COMMAND_VERSION_CODE_SSA7
    elif device_id == "f521da0e":
        adb_command_version_code = ADB_COMMAND_VERSION_CODE_SSJ5
    elif device_id == "emulator-5554":
        adb_command_version_code = ADB_COMMAND_VERSION_CODE_EMULATOR_5554
    else:
        pass
    try:
        result = subprocess.run(adb_command_version_code, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print('result adb_command_version_code: ' + str(result.stdout))
        fb_build_ver = result.stdout.strip().split(' ')[0].replace('versionCode=', '')
        print('fb_build_ver: ' + fb_build_ver)
    except Exception as e:
        print('Something went wrong when run adb_command_version_code: ', e)

    fb_language_code = ''
    with open('build.prop', "r") as f:
        for prop in f:
            if prop.strip().__contains__('ro.product.locale'):
                fb_language_code = prop.strip().split('=')[1]
                print('fb_language_code: ' + fb_language_code)
            if prop.strip().__contains__('ro.product.manufacturer'):
                fb_manufacture = prop.strip().split('=')[1]
                print('fb_manufacture: ' + fb_manufacture)
            if prop.strip().__contains__('ro.product.brand'):
                fb_brand_device = prop.strip().split('=')[1]
                print('fb_brand_device: ' + fb_brand_device)
            if prop.strip().__contains__('ro.product.model'):
                fb_device_ver = prop.strip().split('=')[1]
                print('fb_device_ver: ' + fb_device_ver)
            if prop.strip().__contains__('ro.build.version.release'):
                fb_os_ver = prop.strip().split('=')[1]
                print('fb_os_ver: ' + fb_os_ver)
        f.close()

    fbdm = 'FBDM/{density=3.0,width=1080,height=1920}'
    user_agent = f'[FBAN/FB4A;FBAV/{fb_app_ver};FBBV/{fb_build_ver};{fbdm};FBLC/{fb_language_code};FBRV/0;FBCR/Viettel Telecom;FBMF/{fb_manufacture};FBBD/{fb_brand_device};FBPN/com.facebook.katana;FBDV/{fb_device_ver};FBSV/{fb_os_ver};FBOP/1;FBCA/x86:armeabi-v7a;]'

    print('user_agent: ' + user_agent)
    return user_agent


def clear_data(device_id):
    if device_id == "00179b6a0411":
        adb_clear = ADB_CLEAR_REDMI9
        subprocess.call(adb_clear)
    elif device_id == "14d9cef2":
        adb_clear = ADB_CLEAR_SSA7
        subprocess.call(adb_clear)
    elif device_id == "f521da0e":
        adb_clear = ADB_CLEAR_SSJ5
        subprocess.call(adb_clear)
    elif device_id == "emulator-5554":
        adb_clear = ADB_CLEAR_EMULATOR_5554
        subprocess.call(adb_clear)
    else:
        pass


def write_output(**kwargs):
    pass_email = ""
    tfa = ""
    date_output = f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}T{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}"
    if kwargs.get("device_id") == "14d9cef2":
        with open("./output_ssa7_backup.txt", "a", encoding="utf-8") as f:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}|{date_output}|ip_used: {kwargs.get("res_ip")}-{kwargs.get("res_str")}\n'
            else:
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}|{date_output}|ip_used: {kwargs.get("res_ip")}-{kwargs.get("res_str")}|checkpoint\n'
            print('output: ' + line)
            f.write(line)
            f.close()
        with open("./output_ssa7.txt", "a", encoding="utf-8") as f2:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}\n'
                print('output: ' + line)
                f2.write(line)
                f2.close()

    elif kwargs.get("device_id") == "00179b6a0411":
        with open("./output_redmi9_backup.txt", "a", encoding="utf-8") as f:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}\n'
            else:
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}|checkpoint\n'
            print('output: ' + line)
            f.write(line)
            f.close()
        with open("./output_redmi9.txt", "a", encoding="utf-8") as f2:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}\n'
            else:
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|checkpoint\n'
            print('output: ' + line)
            f2.write(line)
            f2.close()

    elif kwargs.get("device_id") == "f521da0e":
        with open("./output_ssj5_backup.txt", "a", encoding="utf-8") as f:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}\n'
            else:
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}|checkpoint\n'
            print('output: ' + line)
            f.write(line)
            f.close()
        with open("./output_ssj5.txt", "a") as f2:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}\n'
            else:
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|checkpoint\n'
            print('output: ' + line)
            f2.write(line)
            f2.close()

    elif kwargs.get("device_id") == "emulator-5554":
        with open("./output_emulator_5554_backup.txt", "a", encoding="utf-8") as f:
            if kwargs.get("str_status") == "success":
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}|{date_output}|ip_used: {kwargs.get("res_ip")}-{kwargs.get("res_str")}\n'
            else:
                line = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}|{kwargs.get("day")}-{kwargs.get("month")}-{kwargs.get("year")}|time-process:{kwargs.get("time")}|have-avatar: {kwargs.get("have_avatar")}|{date_output}|ip_used: {kwargs.get("res_ip")}-{kwargs.get("res_str")}|checkpoint\n'
            print('output: ' + line)
            f.write(line)
            f.close()
        with open("./output_emulator_5554.txt", "a", encoding="utf-8") as f2:
            if kwargs.get("str_status") == "success":
                line2 = f'{kwargs.get("fb_id")}|{PASS_FB_BOT}|{kwargs.get("token")}|{kwargs.get("cookie")}|{kwargs.get("output_email")}|{pass_email}|{tfa}|{kwargs.get("res_user_agent")}\n'
                print('output: ' + line2)
                f2.write(line2)
                f2.close()
    else:
        pass


if __name__ == '__main__':
    # thread1 = thread_creator_fb_bot(1, "Thread-1", "00179b6a0411")
    # thread2 = thread_creator_fb_bot(2, "Thread-2", "14d9cef2")
    # thread3 = thread_creator_fb_bot(3, "Thread-3", "f521da0e")
    #
    # # thread1.start()
    # # time.sleep(5)
    # thread2.start()
    # time.sleep(5)
    # thread3.start()

    # get_auth_info("emulator-5554")
    # get_user_agent("emulator-5556")

    # choose_avatar("14d9cef2")

    # process_creator_fb_bot("14d9cef2")
    process_creator_fb_bot("emulator-5554")
