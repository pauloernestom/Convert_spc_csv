import spc #https://github.com/rohanisaac/spc
import os


def findFiles(path, extension):
    files = []
    for i in os.listdir(path):
        if i.endswith(extension):
            files.append(path + str(i))
    files.sort()
    return files

path = './'

files = findFiles(path, ".spc")

for i in files:
    filename = i.split('/')[-1][:-4]
    f = spc.File(i)
    f.write_file(filename + '.csv')
