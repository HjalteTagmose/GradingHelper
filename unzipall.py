import os
from zipfile import ZipFile

def unzip(zip, to):
    with ZipFile(zip, 'r') as zipObj:
        zipObj.extractall(to)

path = input('Enter folder path: ').replace('\\','/')
if path == "": path = os.getcwd()

folders = [file for file in os.listdir(path) if os.path.isdir(os.path.join(path, file))]

for folder in folders:
    folderPath = os.path.join(path, folder)
    zips = [file for file in os.listdir(folderPath) if file.endswith(('zip'))]
    for zip in zips:
        zipPath = os.path.join(folderPath, zip)
        unzip(zipPath, folderPath)


