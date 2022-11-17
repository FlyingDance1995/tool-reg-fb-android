import email
import imaplib
import time
import re

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "dev.socialbox" + ORG_EMAIL
FROM_PWD = "dev.socialboxcc21"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

time = time.strftime("%d-%b-%Y", time.gmtime())


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


def search(key, value, con):
    result, data = con.search(None, f'SINCE "{time}" {key} {value}')
    return data


def get_emails(result_bytes, con):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)

    return msgs


def read_email_from_gmail(input_email):
    con = imaplib.IMAP4_SSL(SMTP_SERVER)

    con.login(FROM_EMAIL, FROM_PWD)

    con.select('Inbox')

    # example read verify code from github.com
    msgs = get_emails(search('FROM', 'registration@facebookmail.com', con), con)
    otp_code = ""
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple:

                # encoding set as utf-8
                content = str(sent[1], 'utf-8')
                msg = email.message_from_string(content)
                str_date = msg["date"]
                str_from = msg["from"]
                mail_return = msg["Return-Path"]
                mail_return = str(mail_return).strip().replace("<", "").replace(">", "")
                data = str(content)
                str_find_pattern_1 = "?code=3D"
                str_find_pattern_2 = ";c=3D"
                try:
                    if str_find_pattern_1 in data:
                        index_end = data.find(str_find_pattern_1)
                        if index_end > -1:
                            if str(mail_return) == str(input_email):
                                print(data[index_end + len(str_find_pattern_1): index_end + len(str_find_pattern_1) + 5])
                                may_be_otp = data[index_end + len(str_find_pattern_1): index_end + len(str_find_pattern_1) + 5]
                                otp_code = may_be_otp.strip()
                                print(f"OTP: {may_be_otp.strip()}")
                                print(f"From: {str_from}")
                                print(f"Date: {str_date}")
                                return otp_code
                    elif str_find_pattern_2 in data:
                        index_end = data.find(str_find_pattern_2)
                        if index_end > -1:
                            if str(mail_return) == str(input_email):
                                print(data[index_end + len(str_find_pattern_2): index_end + len(str_find_pattern_2) + 5])
                                may_be_otp = data[index_end + len(str_find_pattern_2): index_end + len(str_find_pattern_2) + 5]
                                otp_code = may_be_otp.strip()
                                print(f"OTP: {may_be_otp.strip()}")
                                print(f"From: {str_from}")
                                print(f"Date: {str_date}")
                                return otp_code

                except UnicodeEncodeError as e:
                    pass


# read_email_from_gmail('danthaiha065@1tower.vn')
