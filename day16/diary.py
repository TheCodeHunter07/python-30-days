# ASSIGNMENT
# 1 diary.py — append dated entries to a text file and read them back

import datetime

today = datetime.date.today()

entry = input("Write your diary entry: ")

with open("diary.txt" , "a") as file:

    file.write(f"{today}: {entry}\n")

with open("diary.txt" , "r") as file:

   content = file.read()

   print(content)