import subprocess
import time

from help.adb_helper import adb_click


def on_off_wifi(device_id):
    if device_id == "00179b6a0411":
        adb_command_swipe = f"adb -s {device_id} shell input touchscreen swipe 800 1 800 200"
        subprocess.run(adb_command_swipe)
        adb_command_swipe_2 = f"adb -s {device_id} shell input touchscreen swipe 800 1 800 500"
        subprocess.run(adb_command_swipe_2)
        adb_click(device_id, 905, 705)
        time.sleep(5)
        adb_click(device_id, 905, 705)
        time.sleep(2)
        adb_click(device_id, 535, 2260)
    elif device_id == "14d9cef2" or device_id == "f521da0e":
        subprocess.run(f"adb -s {device_id} shell su -c 'svc wifi disable'")
        time.sleep(5)
        subprocess.call(f"adb -s {device_id} shell su -c 'svc wifi enable'")
        time.sleep(5)


def off_wifi_emulator(device_id):
    subprocess.run(f"adb -s {device_id} shell su -c 'svc wifi disable'")
    time.sleep(2)


def on_wifi_emulator(device_id):
    subprocess.call(f"adb -s {device_id} shell su -c 'svc wifi enable'")
    time.sleep(2)


# off_wifi_emulator("emulator-5554")
# on_wifi_emulator("emulator-5554")
