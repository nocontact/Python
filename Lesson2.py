import os

def RenameFiles():
    flist = os.listdir(r"/Users/alex/Downloads/prank")
    print (flist)
    os.chdir(r"/Users/alex/Downloads/prank")
    for fname in flist:
        os.rename(fname, fname.translate(None,"0123456789"))

RenameFiles()

