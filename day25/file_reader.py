# ASSIGNMENT
# 2 file_reader.py — a generator that reads a large file line by line

def read_file(file_name):

    with open(file_name , "r") as file:

        for line in file:

            yield line.strip()

for line in read_file("sample.txt"):
    print(line)           