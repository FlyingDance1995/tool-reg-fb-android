import subprocess
import re
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def get_content_text_from_screen(device_id):
    if device_id == "14d9cef2":
        adb_screen_cap = f"adb -s 14d9cef2 shell screencap -p /sdcard/screen.png"
        try:
            subprocess.call(adb_screen_cap)
        except Exception as e:
            print("some thing went wrong run adb adb_screen_cap: ", e)


        adb_pull_screen_cap = f"adb -s 14d9cef2 pull /sdcard/screen.png screen_14d9cef2.png"
        try:
            subprocess.call(adb_pull_screen_cap)
        except Exception as e:
            print("some thing went wrong run adb adb_pull_screen_cap: ", e)

        adb_rm_screen = f"adb -s {device_id} shell rm /sdcard/screen.png"
        try:
            subprocess.call(adb_rm_screen)
        except Exception as e:
            print("some thing went wrong run adb adb_pull_screen_cap: ", e)

        img = cv2.imread("./screen_14d9cef2.png")
        text = pytesseract.image_to_string(img)
        # print(text)
        return text
    elif device_id == "emulator-5554":
        while True:
            adb_screen_cap = f"adb -s {device_id} shell screencap -p /sdcard/screen.png"
            try:
                subprocess.call(adb_screen_cap)
            except Exception as e:
                print("some thing went wrong run adb adb_screen_cap: ", e)

            adb_pull_screen_cap = f"adb -s {device_id} pull /sdcard/screen.png screen_emulator-5554.png"
            try:
                subprocess.call(adb_pull_screen_cap)
            except Exception as e:
                print("some thing went wrong run adb adb_pull_screen_cap: ", e)

            adb_rm_screen = f"adb -s {device_id} shell rm /sdcard/screen.png"
            try:
                subprocess.call(adb_rm_screen)
            except Exception as e:
                print("some thing went wrong run adb adb_pull_screen_cap: ", e)

            img = cv2.imread("./screen_emulator-5554.png")
            if img is None:
                continue
            else:
                text = pytesseract.image_to_string(img)
                return text
    elif device_id == "f521da0e":
        adb_screen_cap = f"adb -s {device_id} shell screencap -p /sdcard/screen.png"
        try:
            subprocess.call(adb_screen_cap)
        except Exception as e:
            print("some thing went wrong run adb adb_screen_cap: ", e)


        adb_pull_screen_cap = f"adb -s {device_id} pull /sdcard/screen.png screen_f521da0e.png"
        try:
            subprocess.call(adb_pull_screen_cap)
        except Exception as e:
            print("some thing went wrong run adb adb_pull_screen_cap: ", e)

        adb_rm_screen = f"adb -s {device_id} shell rm /sdcard/screen.png"
        try:
            subprocess.call(adb_rm_screen)
        except Exception as e:
            print("some thing went wrong run adb adb_pull_screen_cap: ", e)

        img = cv2.imread("./screen_f521da0e.png")
        text = pytesseract.image_to_string(img)
        # print(text)
        return text
    else:
        pass


# get_content_text_from_screen("14d9cef2")
