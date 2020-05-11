import os
import sys

def all_files(path):
    for subdir in os.listdir(path):
        sub_path = os.path.join(path, subdir)
        if os.path.isdir(sub_path):
            all_files(sub_path)
        else:
            print(sub_path)

if __name__ == '__main__':
    params = sys.argv[1]
    print(params)
    all_files(params)