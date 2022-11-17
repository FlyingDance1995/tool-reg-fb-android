import os
from is_live_account import is_live_account
from saver import save_content


def read_accounts(file):
    accounts = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            fb_id = line.split('|')[0]
            accounts.append({
                'fb_id': fb_id,
                'text': line,
            })
    return accounts


def main(input_file, output=False):
    accounts = read_accounts(input_file)

    output_file = input_file.replace('.txt', '__live.txt')
    i = 0
    for a in accounts:
        is_live = is_live_account(a['fb_id'])
        print(a['fb_id'] + ' - ' + str(is_live))
        i += 1 if is_live else 0
        if is_live and output:
            save_content(output_file, a['text'])

    print(f'Live {i} / {len(accounts)}')


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # input_file = 'D:/MVS Project/python-tool-utils/data/facebook_account/facebook_account_2021_06_25.txt'
    input_file_path = 'E:/fb_android_login/output.txt'


    main(input_file_path, output=True)




