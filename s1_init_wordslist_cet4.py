"""
单词列表的来源： https://github.com/mahavivo/english-wordlists 

2023-7-1 我的词汇量：通过百词斩app自测，约为 3300-3700（测了两次）。
基于此，短期目标是熟悉 CET4 的词汇列表。

脚本的作用是把单词列表拆分为一个个的单词。每个单词为一个 .md 文件，并添加上 tag 来标记熟悉程度。
这个处理是为了在 obsidian 上方便筛选。

大约 4500 多个单词（文件），在我本地 windows 电脑用 vscode 根本索引不动啊。T.T
"""
import os
import random

this_repo = os.path.dirname(__file__)

path = os.path.join(this_repo, "cet4")
if not os.path.exists(path):
    os.mkdir(path)

target_file = os.path.join(
    os.path.dirname(this_repo), "english-wordlists", "CET4_edited.txt"
)
target_type = "CET4"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(len(lines), "lines")

failed = []
existed = []

for line in lines:
    splited = line.replace("\n", "").split(" ", 1)
    if len(splited) != 2:
        failed.append(line)
        continue
    word, value = splited
    valued = value.replace(" ", "\n\n")
    idata = f"""{word}\n\n{valued}\n\n#type/{target_type}\n\n"""
    ifile = os.path.join(path, f"{word}.md")

    if os.path.exists(ifile):
        print(word, "existed")
        existed.append(line)
        continue

    with open(ifile, "w", encoding="utf-8") as f:
        f.write(idata)

with open("failed.txt", "w", encoding="utf-8") as f:
    f.writelines(failed)

with open("existed.txt", "w", encoding="utf-8") as f:
    f.writelines(existed)

print("done")
