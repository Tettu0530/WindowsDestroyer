import os, subprocess
import sys

command = "/c rm /s /q ¥:C¥Windows¥System"

yes_no = input("本当にコマンドを実行しますか？(これ以降の取り消しはできません)[Y/N]")

if yes_no == "Y" or yes_no == "y":
    os.system(command)
else:
    sys.exit()