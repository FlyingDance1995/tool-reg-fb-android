import base64
import subprocess


def adb_click(device_id, x, y):
    adb_command = 'adb -s %s shell input tap %s %s' % (device_id, x, y)
    subprocess.call(adb_command)


def adb_input(device_id, x, y, text):
    adb_command = 'adb -s %s shell input tap %s %s' % (device_id, x, y)
    subprocess.call(adb_command)
    # This only run input for ascii char
    # adb_command_input = 'adb -s %s shell input text %s' % (device_id, str(text))

    # This run for any type of char
    charsb64 = str(base64.b64encode(text.encode('utf-8')))[1:]
    adb_command_input = f"adb -s {device_id} shell am broadcast -a ADB_INPUT_B64 --es msg {charsb64}"
    subprocess.run(adb_command_input)


def turn_on_off_screen(device_id):
    adb_command = f'adb -s {device_id} shell input keyevent 26'
    subprocess.call(adb_command)


# adb_click("emulator-5554", 300, 850)
