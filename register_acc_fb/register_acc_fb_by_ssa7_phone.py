import random
import re
import subprocess
import time

from data_name.random_name import random_last_name, random_first_name
from get_birth_day.get_birth_day import do_convert_birth_day
from get_content_text_from_screen.get_content_text import get_content_text_from_screen
from get_temp_mail.get_mail import load_web, get_mail, get_code
from help.adb_helper import adb_click, adb_input
from on_off_data_or_wifi.on_off_wifi_of_4g import on_off_wifi
from proxies.change_ip_proxy import change_ip_proxy_of_phone
from settings import PASS_FB_BOT


def start_app(device_id):
    adb_command_start_fb_app = f"adb -s {device_id} shell am start -n com.facebook.katana/.LoginActivity"
    subprocess.call(adb_command_start_fb_app)
    while True:
        text_image_start_app = get_content_text_from_screen(device_id)
        print("text_image_start_app: ", text_image_start_app)
        if "Tao tai khoan Facebook" in text_image_start_app:
            break
        else:
            time.sleep(5)


def check_language_and_loading_vietnamese_language(device_id):
    while True:
        text_check_loading_language = get_content_text_from_screen(device_id)
        print("text_check_loading_language: ", text_check_loading_language)
        if "Tiéng Viet..." in text_check_loading_language:
            time.sleep(5)
        else:
            break

    # continue with english language
    text_load_fail_vn_language = get_content_text_from_screen(device_id)
    print("text_load_fail_vn_language: ", text_load_fail_vn_language)
    if str(text_load_fail_vn_language).__contains__("TIẾP TỤC BẰNG TIẾNG ANH(MỸ)") \
            or str(text_load_fail_vn_language).__contains__("TIEP TUC BANG TIENG ANH (MY)"):
        adb_click(device_id, 500, 1800)
        time.sleep(1)

    # giao dien bam tiep --> tham gia facebook
    while True:
        text_register_fb = get_content_text_from_screen(device_id)
        print("text_register_fb: ", text_register_fb)
        if "Tham gia Facebook" in text_register_fb or "Join Facebook" in text_register_fb:
            break
        else:
            time.sleep(2)


def refuse_fb_access_phone_and_contacts(device_id):
    text_deny_fb_allow_contacts_and_phone = get_content_text_from_screen(device_id)
    print("text_deny_fb_allow_contacts_and_phone: ", text_deny_fb_allow_contacts_and_phone)
    if "Contacts" and "Phone" in text_deny_fb_allow_contacts_and_phone \
            or "Ngudi lién hé" and "Dién thoai" in text_deny_fb_allow_contacts_and_phone:
        adb_click(device_id, 550, 1400)
        time.sleep(1)
    elif "TUCHOI" in text_deny_fb_allow_contacts_and_phone or "DENY" in text_deny_fb_allow_contacts_and_phone:
        adb_click(device_id, 600, 1500)
        time.sleep(1)
    else:
        adb_click(device_id, 550, 1150)
        time.sleep(2)
        adb_click(device_id, 550, 1150)
        time.sleep(2)
    adb_click(device_id, 500, 1150)


def input_name(device_id, first_name, last_name):
    while True:
        text_check_input_name = get_content_text_from_screen(device_id)
        print("text_check_input_name: ", text_check_input_name)
        if "Ban tén gi" in text_check_input_name:
            adb_input(device_id, 150, 800, last_name)  # input ho
            time.sleep(2)
            adb_input(device_id, 700, 800, first_name)  # input ten
            time.sleep(2)
            break
        elif "Chon tén cua ban" in text_check_input_name:
            adb_click(device_id, 430, 780)
            time.sleep(1)
            adb_click(device_id, 550, 1235)
        else:
            time.sleep(2)


def select_birth_day(device_id):
    count1 = 0
    count2 = 0
    count3 = 0

    day_count = random.randint(1, 30)
    month_count = random.randint(1, 11)
    year_count = random.randint(15, 30)
    while count1 < day_count:
        count1 += 1
        adb_click(device_id, 340, 721)

    while count2 < month_count:
        count2 += 1
        adb_click(device_id, 545, 721)

    while count3 < year_count:
        count3 += 1
        adb_click(device_id, 737, 721)

    str_day = ""
    str_month = ""
    str_year = ""

    # lấy ngày sinh để back-up
    text_birth_day = get_content_text_from_screen(device_id)
    print("text_birth_day: ", text_birth_day)
    data = text_birth_day.find("khac.")
    if data == -1:
        try:
            data = text_birth_day.find("birthday?")
            res_day, res_month, res_year = do_convert_birth_day(device_id, text_birth_day, data, 93, 106)
            str_day = res_day.strip()
            str_month = res_month.strip()
            str_year = res_year.strip()
        except Exception as e:
            print(e)
    elif data != -1:
        res_day, res_month, res_year = do_convert_birth_day(device_id, text_birth_day, data, 20, 32)
        str_day = res_day.strip()
        str_month = res_month.strip()
        str_year = res_year.strip()

    return str_day, str_month, str_year


def choice_sex(device_id):
    sex = random.randint(0, 1)
    if sex == 0:
        adb_click(device_id, 500, 724)  # chose sex
    if sex == 1:
        adb_click(device_id, 500, 900)  # chose sex
    time.sleep(2)


def check_status_acc_after_submit_register(device_id):
    while True:
        text_check_loading_register = get_content_text_from_screen(device_id)
        print("text_check_loading_register: ", text_check_loading_register)
        if "Dang tao tai khoan..." in text_check_loading_register or "Dang dang nhap" in text_check_loading_register:
            time.sleep(5)
        elif "Cai dat Wi-Fi" in text_check_loading_register:
            change_ip_proxy_of_phone(device_id)
            on_off_wifi(device_id)
            continue
        elif "Chon tén cua ban" in text_check_loading_register:
            adb_click(device_id, 430, 780)
            time.sleep(1)
            adb_click(device_id, 550, 1235)
        elif "Ban tén gi?" in text_check_loading_register:
            last_name = random_last_name()
            first_name = random_first_name()
            adb_input(device_id, 150, 800, last_name)  # input ho
            time.sleep(2)
            adb_input(device_id, 700, 800, first_name)  # input ten
            time.sleep(2)
        else:
            break


def save_email_and_pass(device_id):
    while True:
        text_verify = get_content_text_from_screen(device_id)
        print("text_verify: ", text_verify)
        if "Ban da dang nhap Facebook" in text_verify or "Dang dang nhap..." in text_verify:
            adb_click(device_id, 770, 1250)  # save password
            time.sleep(2)

            adb_click(device_id, 500, 1450)  # save email
            time.sleep(2)
        elif "Didn't get the email?" in text_verify or "Ban chua nhan duoc email?" in text_verify:
            break
        elif "Ma xac nhan" in text_verify or "Xac nhan Tai khoan" in text_verify:
            break
        else:
            return 'fail'


def verify_otp_code(device_id):
    while True:
        text_try_loading_verify = get_content_text_from_screen(device_id)
        print("text_try_loading_verify: ", text_try_loading_verify)
        if "Dang xac nhan..." in text_try_loading_verify:
            time.sleep(5)
            on_off_wifi(device_id)
            time.sleep(1)
            adb_click(device_id, 450, 800)  # toa do nut xac thuc
            time.sleep(20)
        elif "Tai khoan cua ban da bi" in text_try_loading_verify:
            return 'fail'
        else:
            time.sleep(2)
            break


def choose_avatar(device_id):
    text_choose_avatar = get_content_text_from_screen(device_id)
    print("text_choose_avatar: ", text_choose_avatar)
    if "CHO PHEP" in text_choose_avatar:
        adb_click(device_id, 800, 1150)  # toan do cho phep truy cap anh dai dien
        time.sleep(4)
        adb_click(device_id, 500, 400)  # anh
        time.sleep(4)
        adb_click(device_id, 1000, 150)
        time.sleep(4)
        text_save_avatar = get_content_text_from_screen(device_id)
        print("text_save_avatar: ", text_save_avatar)
        if "Cat LUU" in text_save_avatar and "Cong khai" in text_save_avatar:
            adb_click(device_id, 1000, 150) # nut luu
            while True:
                text_check_upload_avatar_success = get_content_text_from_screen(device_id)
                print("text_check_upload_avatar_success: ", text_check_upload_avatar_success)
                if "Dang tai len" in text_check_upload_avatar_success:
                    time.sleep(5)
                else:
                    break
        else:
            adb_click(device_id, 500, 1800)  # nut luu
            while True:
                text_check_upload_avatar_success = get_content_text_from_screen(device_id)
                print("text_check_upload_avatar_success: ", text_check_upload_avatar_success)
                if "Dang tai len" in text_check_upload_avatar_success:
                    time.sleep(5)
                else:
                    break

    elif "Tim ban be" in text_choose_avatar:
        adb_click(device_id, 1000, 150)
        time.sleep(2)
        adb_click(device_id, 500, 1250)
        time.sleep(2)

    return 'success'


def register_bot_fb_by_ssa7(device_id, first_name, last_name):

    # start app
    start_app(device_id)

    # click nut dang ky
    adb_click(device_id, 500, 1720)
    time.sleep(5)

    # check loading vietnamese language
    check_language_and_loading_vietnamese_language(device_id)
    adb_click(device_id, 500, 1362)
    time.sleep(2)

    # refuse facebook access phone + contacts
    refuse_fb_access_phone_and_contacts(device_id)

    # input name
    input_name(device_id, first_name, last_name)

    adb_click(device_id, 500, 1140)  # continue
    time.sleep(2)

    # random birth day
    str_day, str_month, str_year = select_birth_day(device_id)

    # continue button
    adb_click(device_id, 500, 1500)
    time.sleep(2)

    # choose sex
    choice_sex(device_id)

    # continue
    adb_click(device_id, 500, 1450)
    time.sleep(2)

    # register by email
    adb_click(device_id, 500, 1800)
    time.sleep(2)

    # get mail đăng ký
    while True:
        load_web(device_id)
        email = get_mail(device_id)
        if "Loading" in email or "Đang tải." in email:
            email = get_mail(device_id)
        if "@moxkid.com" not in email:
            break

    # input email
    adb_input(device_id, 150, 700, email)
    time.sleep(1)
    adb_click(device_id, 500, 1100)
    time.sleep(1)

    # input pass
    password = PASS_FB_BOT
    adb_input(device_id, 150, 700, password)
    time.sleep(1)

    # continue
    adb_click(device_id, 500, 1150)
    time.sleep(2)

    # register
    adb_click(device_id, 500, 1110)
    time.sleep(15)

    check_status_acc_after_submit_register(device_id)
    res_check_after_register = save_email_and_pass(device_id)
    if res_check_after_register == "fail":
        return str_day, str_month, str_year, email, 'fail', "not yet - checkpoint when submit register"

    # get otp code
    otp_code = None
    text_verify_otp = get_content_text_from_screen(device_id)
    print("text_verify_otp: ", text_verify_otp)
    if str(email).split("@")[0] in text_verify_otp:
        otp_code = get_code(device_id, 0)
    if otp_code is not None:
        adb_input(device_id, 150, 600, otp_code)
        adb_click(device_id, 450, 800)  # toa do nut xac thuc
        time.sleep(20)

    # verify otp code
    res = verify_otp_code(device_id)
    if res == "fail":
        return str_day, str_month, str_year, email, 'fail', "not yet - checkpoint when verify otp"

    # verify email register
    text_verify_confirm_email_register = get_content_text_from_screen(device_id)
    print("text_verify_confirm_email_register: ", text_verify_confirm_email_register)
    if "Xac nhan email cua ban" in text_verify_confirm_email_register:
        adb_input(device_id, 200, 680, email)
        time.sleep(1)
        adb_click(device_id, 500, 850)
        time.sleep(5)

    # chọn ảnh đại diện
    adb_click(device_id, 500, 1630)  # toan do chon anh dai dien
    time.sleep(3)

    res_choose_avatar = choose_avatar(device_id)
    if res_choose_avatar == 'success':
        return str_day, str_month, str_year, email, 'success', "Yes"
    else:
        return None
