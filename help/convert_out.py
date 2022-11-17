def convert_output_acc():
    res = ""
    with open("../1Data_22acc_0k_11_54__24_6_2021.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "checkpoint" in line:
                pass
            else:
                res += line
        f.close()

    writing_file = open("../output_new.txt", "w")
    writing_file.write(res)
    writing_file.close()


convert_output_acc()
