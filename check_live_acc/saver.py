def save_content(file, txt):
    with open(file, 'a+', encoding='utf-8') as f:
        f.write(txt)
