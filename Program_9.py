import os


def dir_tree(dir):
    file_list = os.listdir(dir)
    for file in file_list:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            dir_tree(path)
        else:
            print(file)


path = input("Enter Path:")
dir_tree(path)
