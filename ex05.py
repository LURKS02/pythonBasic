
# file ===============================
import os

file_name = "ex05.txt"

f = open(file_name, "wt")
data = "test"
f.write(data)
f.close()

if os.path.exists(file_name):
    f = open(file_name, "rt")
    data = f.read()
    print("data = ", data)
    f.close()
