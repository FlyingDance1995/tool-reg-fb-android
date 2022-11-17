import random
import subprocess
from subprocess import run, PIPE

from settings import ADB_COMMAND_PUSH_SSA7, ADB_COMMAND_ROOT_SSA7, ADB_COMMAND_PUSH_EMULATOR_5554, \
    ADB_COMMAND_ROOT_EMULATOR_5554


def change_device_info():
    # todo maintain tim them setting tuong tu add vao list nay
    reading_file = open("build.prop", "r")
    new_file_content = ""
    data = None
    for line in reading_file:
        if line.strip().__contains__('ro.product.model'):
            line = line.strip().split('=')[0] + '=' + random.choice(['SM-A700H', 'S90-T', 'Y3t', 'D310W', 'S39h'])
            if line.strip().split('=')[1] == 'SM-A700H':
                with open('device_config_fake/input_device_info.txt', "r", encoding='utf-8') as f:
                    for arr in f:
                        if arr.__contains__('a73'):
                            data = arr.strip().replace('|', '').split(',')
                f.close()
            if line.strip().split('=')[1] == 'S90-T':
                with open('device_config_fake/input_device_info.txt', "r", encoding='utf-8') as f:
                    for arr in f:
                        if arr.__contains__('S90'):
                            data = arr.strip().replace('|', '').split(',')
                f.close()
            if line.strip().split('=')[1] == 'Y3t':
                with open('device_config_fake/input_device_info.txt', "r", encoding='utf-8') as f:
                    for arr in f:
                        if arr.__contains__('Y3t'):
                            data = arr.strip().replace('|', '').split(',')
                f.close()
            if line.strip().split('=')[1] == 'D310W':
                with open('device_config_fake/input_device_info.txt', "r", encoding='utf-8') as f:
                    for arr in f:
                        if arr.__contains__('D310W'):
                            data = arr.strip().replace('|', '').split(',')
                f.close()
            if line.strip().split('=')[1] == 'S39h':
                with open('device_config_fake/input_device_info.txt', "r", encoding='utf-8') as f:
                    for arr in f:
                        if arr.__contains__('S39h'):
                            data = arr.strip().replace('|', '').split(',')
                f.close()
        new_file_content += line.strip() + '\n'
    writing_file = open("build.prop", "w")
    writing_file.write(new_file_content)
    reading_file.close()
    return data


def do_change_device(data):
    reading_file = open("build.prop", "r")
    new_file_data = ""
    for line in reading_file:
        if line.strip().__contains__('ro.build.id'):
            line = line.strip().split('=')[0] + '=' + data[0]
        if line.strip().__contains__('ro.build.display.id'):
            line = line.strip().split('=')[0] + '=' + data[1]
        if line.strip().__contains__('ro.build.version.incremental'):
            line = line.strip().split('=')[0] + '=' + data[2]
        if line.strip().__contains__('ro.build.version.sdk'):
            line = line.strip().split('=')[0] + '=' + data[3]
        if line.strip().__contains__('ro.build.version.release'):
            line = line.strip().split('=')[0] + '=' + data[4]
        if line.strip().__contains__('ro.build.host'):
            line = line.strip().split('=')[0] + '=' + data[5]
        if line.strip().__contains__('ro.build.flavor'):
            line = line.strip().split('=')[0] + '=' + data[6]
        if line.strip().__contains__('ro.product.brand'):
            line = line.strip().split('=')[0] + '=' + data[7]
        if line.strip().__contains__('ro.product.name'):
            line = line.strip().split('=')[0] + '=' + data[8]
        if line.strip().__contains__('ro.product.device'):
            line = line.strip().split('=')[0] + '=' + data[9]
        if line.strip().__contains__('ro.product.board'):
            line = line.strip().split('=')[0] + '=' + data[10]
        if line.strip().__contains__('ro.product.manufacturer'):
            line = line.strip().split('=')[0] + '=' + data[11]
        if line.strip().__contains__('ro.product.locale'):
            line = line.strip().split('=')[0] + '=' + data[12]
        if line.strip().__contains__('ro.build.product'):
            line = line.strip().split('=')[0] + '=' + data[13]
        if line.strip().__contains__('ro.build.description'):
            line = line.strip().split('=')[0] + '=' + data[14]
        if line.strip().__contains__('ro.build.fingerprint'):
            line = line.strip().split('=')[0] + '=' + data[15]
        if line.strip().__contains__('ro.build.PDA'):
            line = line.strip().split('=')[0] + '=' + data[16]
        if line.strip().__contains__('ro.build.hidden_ver'):
            line = line.strip().split('=')[0] + '=' + data[17]
        new_file_data += line.strip() + '\n'

    reading_file.close()

    writing_file = open("build.prop", "w")
    writing_file.write(new_file_data)
    writing_file.close()


def push_file(device_id):
    adb_command_push = ""
    if device_id == "14d9cef2":
        adb_command_push = ADB_COMMAND_PUSH_SSA7
    elif device_id == "emulator-5554":
        adb_command_push = ADB_COMMAND_PUSH_EMULATOR_5554
    try:
        result = run(adb_command_push, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print('result adb_command_push: ' + str(result.stdout))
    except Exception as e:
        print('Something went wrong when run adb_command_push: ', e)

    adb_command_root = ""
    if device_id == "14d9cef2":
        adb_command_root = ADB_COMMAND_ROOT_SSA7
    elif device_id == "emulator-5554":
        adb_command_root = ADB_COMMAND_ROOT_EMULATOR_5554
    sub = subprocess.Popen(adb_command_root, stdin=subprocess.PIPE)
    sub.stdin.write('mount -o rw,remount /system\n'.encode('utf-8'))
    sub.stdin.write('cp -r /data/local/tmp/build.prop /system/build.prop\n'.encode('utf-8'))
