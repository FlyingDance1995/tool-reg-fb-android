import random
import re
import subprocess
import time

from data_name.random_name import random_last_name, random_first_name
from get_birth_day.get_birth_day import do_convert_birth_day
from get_content_text_from_screen.get_content_text import get_content_text_from_screen
from get_otp_from_email.convert_email import convert_email
from get_temp_mail.get_mail import load_web, get_mail, get_code
from help.adb_helper import adb_click, adb_input
from settings import PASS_FB_BOT


def start_app(device_id):
    while True:
        adb_command_start_fb_app = f"adb -s {device_id} shell am start -n com.facebook.katana/.LoginActivity"
        subprocess.call(adb_command_start_fb_app)
        text_image_start_app = get_content_text_from_screen(device_id)
        if text_image_start_app is None:
            time.sleep(5)
            continue
        else:
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
        adb_click(device_id, 350, 1200)
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
        adb_click(device_id, 360, 915)
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


def input_name(device_id, first_name, last_name):
    while True:
        text_check_input_name = get_content_text_from_screen(device_id)
        print("text_check_input_name: ", text_check_input_name)
        if "Ban tén gi" in text_check_input_name or "What's your name?" in text_check_input_name:
            adb_input(device_id, 90, 530, last_name)  # input ho
            time.sleep(2)
            adb_input(device_id, 500, 530, first_name)  # input ten
            time.sleep(2)
            break
        elif "Chon tén cua ban" in text_check_input_name:
            adb_click(device_id, 300, 535)
            time.sleep(1)
            adb_click(device_id, 300, 830)
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
        adb_click(device_id, 215, 475)

    while count2 < month_count:
        count2 += 1
        adb_click(device_id, 360, 475)

    while count3 < year_count:
        count3 += 1
        adb_click(device_id, 489, 470)

    str_day = ""
    str_month = ""
    str_year = ""

    # lấy ngày sinh để back-up
    text_birth_day = get_content_text_from_screen(device_id)
    print("text_birth_day: ", text_birth_day)
    data = text_birth_day.find("?")
    if data == -1:
        try:
            data = text_birth_day.find("birthday?")
            res_day, res_month, res_year = do_convert_birth_day(device_id, text_birth_day, data, 93, 107)
            str_day = res_day.strip()
            str_month = res_month.strip()
            str_year = res_year.strip()
        except Exception as e:
            print(e)
    elif data != -1:
        res_day, res_month, res_year = do_convert_birth_day(device_id, text_birth_day, data, 109, 123)
        str_day = res_day.strip()
        str_month = res_month.strip()
        str_year = res_year.strip()

    return str_day, str_month, str_year


def choice_sex(device_id):
    sex = random.randint(0, 1)
    if sex == 0:
        adb_click(device_id, 269, 473)  # chose sex
    if sex == 1:
        adb_click(device_id, 209, 576)  # chose sex
    time.sleep(2)


def check_status_acc_after_submit_register(device_id):
    n = 0
    while n < 5:
        text_check_loading_register = get_content_text_from_screen(device_id)
        print("text_check_loading_register: ", text_check_loading_register)
        if "Dang tao tai khoan..." in text_check_loading_register or "Dang dang nhap" in text_check_loading_register:
            time.sleep(5)
        elif "Cai dat Wi-Fi" in text_check_loading_register or "Check your Wi-Fi settings" in text_check_loading_register:
            adb_click(device_id, 300, 750)
            time.sleep(5)
            n += 1
            continue
        elif "Chon tén cua ban" in text_check_loading_register:
            adb_click(device_id, 300, 535)
            time.sleep(1)
            adb_click(device_id, 300, 830)
        elif "Da xay ra l6i khi dang nhap" in text_check_loading_register:
            adb_click(device_id, 550, 750)
            continue
        elif "Ban tén gi?" in text_check_loading_register:
            last_name = random_last_name()
            first_name = random_first_name()
            adb_input(device_id, 90, 530, last_name)  # input ho
            time.sleep(2)
            adb_input(device_id, 500, 530, first_name)  # input ten
            time.sleep(2)
            adb_click(device_id, 350, 750)  # continue
        else:
            break


def save_email_and_pass(device_id):
    n = 0
    while n < 5:
        text_verify = get_content_text_from_screen(device_id)
        print("text_verify: ", text_verify)
        if "Ban da dang nhap Facebook" in text_verify or "Dang dang nhap..." in text_verify:
            adb_click(device_id, 500, 820)  # save password
            time.sleep(2)

            adb_click(device_id, 350, 964)  # save email
            time.sleep(2)
        elif "Cai dat Wi-Fi" in text_verify or "Check your Wi-Fi settings" in text_verify:
            adb_click(device_id, 300, 750)
            time.sleep(5)
            n += 1
            continue
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
            # on_off_wifi(device_id)
            # time.sleep(1)
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
        adb_click(device_id, 550, 750)  # toa do cho phep truy cap anh dai dien
        time.sleep(4)
        adb_click(device_id, 350, 275)  # anh
        time.sleep(4)
        adb_click(device_id, 600, 115)
        time.sleep(4)
        text_save_avatar = get_content_text_from_screen(device_id)
        print("text_save_avatar: ", text_save_avatar)
        if "Cat LUU" in text_save_avatar or "Crop SAVE" in text_save_avatar:
            adb_click(device_id, 615, 115)  # nut luu
            while True:
                text_check_upload_avatar_success = get_content_text_from_screen(device_id)
                print("text_check_upload_avatar_success: ", text_check_upload_avatar_success)
                if "Dang tai len" in text_check_upload_avatar_success:
                    time.sleep(5)
                else:
                    break
        else:
            adb_click(device_id, 360, 1200)  # nut luu
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
    else:
        adb_click(device_id, 350, 275)  # anh
        time.sleep(4)
        adb_click(device_id, 600, 115)
        time.sleep(4)
        adb_click(device_id, 600, 115)
        time.sleep(5)
        adb_click(device_id, 360, 1150)
        time.sleep(5)
        # text_save_avatar = get_content_text_from_screen(device_id)
        # print("text_save_avatar: ", text_save_avatar)
        # if "Cat LUU" in text_save_avatar and "Cong khai" in text_save_avatar:
        #     adb_click(device_id, 600, 115)  # nut luu
        #     while True:
        #         text_check_upload_avatar_success = get_content_text_from_screen(device_id)
        #         print("text_check_upload_avatar_success: ", text_check_upload_avatar_success)
        #         if "Dang tai len" in text_check_upload_avatar_success:
        #             time.sleep(5)
        #         else:
        #             break
        # else:
        #     adb_click(device_id, 360, 1150)  # nut luu
        #     while True:
        #         text_check_upload_avatar_success = get_content_text_from_screen(device_id)
        #         print("text_check_upload_avatar_success: ", text_check_upload_avatar_success)
        #         if "Dang tai len" in text_check_upload_avatar_success:
        #             time.sleep(5)
        #         else:
        #             break

    return "success"


def register_bot_fb_by_emulator_5554(device_id, first_name, last_name):

    # start app
    start_app(device_id)

    # click nut dang ky
    adb_click(device_id, 350, 1150)
    time.sleep(5)

    # check loading vietnamese language
    check_language_and_loading_vietnamese_language(device_id)
    adb_click(device_id, 350, 915)
    time.sleep(2)

    # refuse facebook access phone + contacts
    refuse_fb_access_phone_and_contacts(device_id)
    time.sleep(7)
    adb_click(device_id, 300, 750)

    # input name
    input_name(device_id, first_name, last_name)

    adb_click(device_id, 350, 750)  # continue
    time.sleep(2)

    # random birth day
    str_day, str_month, str_year = select_birth_day(device_id)

    # continue button
    adb_click(device_id, 350, 1000)
    time.sleep(2)

    # choose sex
    choice_sex(device_id)

    # continue
    adb_click(device_id, 360, 962)
    time.sleep(2)

    # register by email
    adb_click(device_id, 360, 1200)
    time.sleep(2)

    # get mail đăng ký
    # while True:
    #     load_web(device_id)
    #     email = get_mail(device_id)
    #     if "Loading" in email or "Đang tải." in email:
    #         continue
    #     if "@moxkid.com" not in email:
    #         break

    email = convert_email(str(last_name).strip().lower() + str(first_name).strip().lower().replace(" ", "") \
                          + str(random.randint(1, 31)) + "_" + str(random.randint(1, 12)) + "_" \
                          + str(random.randint(1960, 2010)) + "@gmail.com")
    # input email
    adb_click(device_id, 654, 520)
    time.sleep(2)
    adb_input(device_id, 150, 520, email)
    adb_click(device_id, 200, 735)
    time.sleep(1)

    # input pass
    password = PASS_FB_BOT
    adb_input(device_id, 150, 525, password)  # input pass
    time.sleep(1)

    # continue
    adb_click(device_id, 150, 750)
    time.sleep(5)

    # on_wifi
    # on_wifi_emulator(device_id)

    # register
    adb_click(device_id, 350, 720)
    time.sleep(15)

    check_status_acc_after_submit_register(device_id)
    res_check_after_register = save_email_and_pass(device_id)
    if res_check_after_register == "fail":
        return str_day, str_month, str_year, email, 'fail', "not yet - checkpoint when submit register"

    # get mail verify
    while True:
        load_web(device_id)
        email_verify = get_mail(device_id)
        if "Loading" in email_verify or "Đang tải." in email_verify:
            continue
        if "@moxkid.com" not in email_verify:
            break

    # get otp code
    otp_code = None
    text_verify_otp = get_content_text_from_screen(device_id)
    print("text_verify_otp: ", text_verify_otp)
    if str(email).split("@")[1] in text_verify_otp:
        adb_click(device_id, 300, 850)
        adb_input(device_id, 300, 250, email_verify)
        adb_input("emulator-5554", 300, 300, "wogan56096@herrain.com")
        adb_click("emulator-5554", 300, 400)
        otp_code = get_code(device_id, 0)
    if otp_code is not None:
        adb_input(device_id, 150, 400, otp_code)
        adb_click(device_id, 300, 530)  # toa do nut xac thuc
        time.sleep(20)

    # verify otp code
    res = verify_otp_code(device_id)
    if res == "fail":
        return str_day, str_month, str_year, email_verify, 'fail', "not yet - checkpoint when verify otp"

    # verify email register
    text_verify_confirm_email_register = get_content_text_from_screen(device_id)
    print("text_verify_confirm_email_register: ", text_verify_confirm_email_register)
    if "Xac nhan email cua ban" in text_verify_confirm_email_register:
        adb_input(device_id, 200, 680, email_verify)
        time.sleep(5)
        adb_click(device_id, 500, 575)
        time.sleep(7)

    # chọn ảnh đại diện
    adb_click(device_id, 350, 1085)
    time.sleep(5)

    res_choose_avatar = choose_avatar(device_id)
    if res_choose_avatar == 'success':
        return str_day, str_month, str_year, email_verify, 'success', "Yes"
    else:
        return None


# select_birth_day("emulator-5554")