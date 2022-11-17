from help.utils import convert_birth_day


def do_convert_birth_day(device_id, text_birth_day, data, length_start, length_end):
    if device_id == "14d9cef2" or device_id == "f521da0e":
        birth_day = text_birth_day[data + int(length_start): data + int(length_end)].strip().replace("\n", "")
    elif device_id == "emulator-5554":
        birth_day = text_birth_day[data + int(length_start): data + int(length_end)].strip().replace("\n", "")
    else:
        birth_day = text_birth_day[data + int(length_start): data + int(length_end) + 3].strip().replace("\n", "")

    res_day, res_month, res_year = convert_birth_day(device_id, birth_day)
    day = res_day
    month = res_month
    year = res_year
    if month in ["10", "11", "12"]:
        if device_id == "14d9cef2" or device_id == "f521da0e":
            birth_day = text_birth_day[data + int(length_start): data + int(length_end) + 1].strip().replace("\n", "")
        elif device_id == "emulator-5554":
            birth_day = text_birth_day[data + int(length_start) - 1: data + int(length_end) - 1].strip().replace("\n", "")
        else:
            birth_day = text_birth_day[data + int(length_start): data + int(length_end) + 3].strip().replace("\n", "")
        res_day, res_month, res_year = convert_birth_day(device_id, birth_day)
        year = res_year

    return day, month, year
