import shutil
import os

path = input('Enter folder path: ').replace('\\','/')
if path == "": path = os.getcwd()

cargoBat  = os.path.join(path, "RunCargoTester.bat")
hotelBat  = os.path.join(path, "RunHotelTester.bat")
cargoTest = os.path.join(path, "CargoTester.java")
hotelTest = os.path.join(path, "HotelTester.java")

# Find java files
def findSrc(p):
    folders = [file for file in os.listdir(p) if os.path.isdir(os.path.join(p, file))]
    for folder in folders:
        folderPath = os.path.join(p, folder)
        javas = [file for file in os.listdir(folderPath) if file.endswith(('java'))]
        junks = [file for file in os.listdir(folderPath) if file.endswith(('class', 'ctxt', 'bluej'))]
        
        if len(javas) == 0:
            findSrc(folderPath)
        else:
            srctype = ("cargo" if "CargoShip.java" in javas else "hotel")
            print("SRC ("+srctype+"): " + folderPath)

            # delete junk
            for junk in junks:
                junkPath = os.path.join(folderPath, junk)
                os.remove(junkPath)
                
            # paste checkers
            if srctype == "cargo":
                shutil.copy(cargoBat , folderPath)
                shutil.copy(cargoTest, folderPath)
            else:
                shutil.copy(hotelBat , folderPath)
                shutil.copy(hotelTest, folderPath)

findSrc(path)