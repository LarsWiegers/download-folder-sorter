import os

downloadsFolder = r'C:\Users\Windows\Downloads'

for file in os.listdir(downloadsFolder):
    parts = file.split('.')
    length = len(parts)

    directoryPath = downloadsFolder + "\\" + parts[length - 1]

    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)

    try:
        os.rename(downloadsFolder + "\\" + file, directoryPath + "\\" + file)
    except PermissionError as error:
        print(str(error))
