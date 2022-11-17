import time

from slack_sdk import WebhookClient


def check():
    while True:
        with open("../output_emulator_5554_backup.txt", "r", encoding="utf8") as f1:
            len_f1 = len(f1.read())
            print("len_f1: ", len_f1)
            f1.close()

        time.sleep(600)

        with open("../output_emulator_5554_backup.txt", "r", encoding="utf8") as f2:
            len_f2 = len(f2.read())
            print("len_f2: ", len_f2)
            f2.close()
            if len_f2 <= len_f1:
                webhook = WebhookClient("https://hooks.slack.com/services/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")
                webhook.send(text="check phone emulator-5556 may be offline")


check()
