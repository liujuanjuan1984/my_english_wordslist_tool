""" 随机获取 num 个不熟悉或陌生的单词，然后检查自己是否熟悉"""

import os
import random
import datetime

this_repo = os.path.dirname(__file__)
wordspath = os.path.join(this_repo, "cet4")

num = 30
words = os.listdir(wordspath)
inum = 0

while True:
    word = random.choice(words)
    ifile = os.path.join(wordspath, word)
    with open(ifile, "r", encoding="utf-8") as f:
        idata = f.read()

    tag_1 = "#progress"
    if tag_1 in idata:
        print(word, "is done.\n")
        continue

    print("+" * 50, "\n", word.replace(".md", ""), "\n0 陌生 1 熟悉?")
    n = input("\n>>")
    if n == "1":
        print(idata, "\n\n0 no 1 yes?")
        checked = input("\n>>")
        if checked == "1":
            tag = "#progress/done"
        else:
            tag = "#progress/doing"
    else:
        tag = "#progress/todo"

    if tag not in idata:
        idata += f"\n\n{datetime.date.today()} {tag}\n\n"
        with open(ifile, "w", encoding="utf-8") as f:
            f.write(idata)

    inum += 1
    if inum >= num:
        break
