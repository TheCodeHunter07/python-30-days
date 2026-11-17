# ASSIGNMENT
# 2 safe_file_reader.py — ask for a filename and handle a missing file gracefully



file_name = input("Enter the file name: ")

try:
    

    with open(file_name ,"r") as file:

        content = file.read()

        print(content)

except FileNotFoundError:

     print("File does not Exist")

else:
    print("File read successfully!")

finally:
    print("File reading operation completed.")

