import os

def scan_directory(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            print(os.path.join(root, file))
base_path = "Mausive-The_Libary"
scan_directory(base_path)
os.system("pause")