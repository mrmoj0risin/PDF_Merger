import os
import sys
import PyPDF2

inputs = sys.argv[1:]

try:
    while True:
        path = input("ENTER path with PDF's")
        if os.path.exists(path):
            print("=")
            break
        else:
            print('Enter VALID PATH')
except:
    print("234")
try:
    path_converted = input("Enter path where to store merged PDF")
    if not os.path.exists(path_converted):
        os.mkdir(path_converted)
except:
    pass


with os.scandir(path) as entries:
    mergedObject = PyPDF2.PdfFileMerger()
    for file in entries:
        if file.name.lower().endswith('.pdf'):

            with open(file,"rb") as filePDF:
                mergedObject.append(filePDF)
                mergedObject.write(f"{path_converted}/mergedfilesoutput.pdf")
