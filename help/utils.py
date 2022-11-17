
dict_month_sma7 = {
    "Th1": "01",
    "Th2": "02",
    "Th3": "03",
    "Th4": "04",
    "Th5": "05",
    "ThS": "05",
    "Th6": "06",
    "Th7": "07",
    "Th8": "08",
    "Th9": "09",
    "Th10": "10",
    "Th11": "11",
    "Th12": "12",
}

dict_month_redmi9 = {
    "thg1": "01",
    "thg2": "02",
    "thg3": "03",
    "thg4": "04",
    "thg5": "05",
    "thg6": "06",
    "thg7": "07",
    "thg8": "08",
    "thg9": "09",
    "thg10": "10",
    "thg11": "11",
    "thg12": "12"
}

dict_month_ssj5 = {
    "Th1": "01",
    "Th2": "02",
    "Th3": "03",
    "Th4": "04",
    "Th5": "05",
    "Th6": "06",
    "Th7": "07",
    "Th8": "08",
    "Tho": "09",
    "Th10": "10",
    "Th11": "11",
    "Th12": "12",
}

dict_month_emulator_5554 = {
    "thg1": "01",
    "thg2": "02",
    "thg3": "03",
    "thg4": "04",
    "thg5": "05",
    "thg6": "06",
    "thg7": "07",
    "thg8": "08",
    "thgs": "08",
    "thg9": "09",
    "thg10": "10",
    "thg11": "11",
    "thg12": "12",
}


def convert_birth_day(device_id, input):
    day = ''
    month = ''
    year = ''
    data = input.strip().split(" ")
    if device_id == "14d9cef2":
        dict_month = dict_month_sma7
    elif device_id == "f521da0e":
        dict_month = dict_month_ssj5
    elif device_id == "emulator-5554":
        dict_month = dict_month_emulator_5554
    else:
        dict_month = dict_month_redmi9
    if len(data) == 3:
        day = data[0]
        if str(data[1]) in dict_month:
            month = dict_month[data[1]]
        if len(data[2]) >= 4:
            year = data[2][:4]
    elif len(data) == 4:
        day = data[0]
        if str(data[1]+data[2]) in dict_month:
            month = dict_month[data[1]+data[2]]
        if len(data[3]) >= 4:
            year = data[3][:4]
    else:
        print("some thing went wrong convert_birth_day")
    print(f'day: {day}, month: {month}, year: {year}')
    return day, month, year


# convert_birth_day("emulator-5554", '11 thg 12 1999')