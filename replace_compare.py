import sys, os
from PIL import Image

def replace(img, sub, pos):
    raw = Image.open(img)
    add = Image.open(sub)
    raw.paste(add, pos)
    raw.save(img)

def compare(original, unknow):
    size_original = os.path.getsize(original)
    size_unknow = os.path.getsize(unknow)    
    same = True
    i = 0
    file_original = open(original, "rb")
    file_unknow = open(unknow, "rb")
    while same and i <= size_original and i <= size_unknow:
        if file_original.read(1) != file_unknow.read(1):
            same = False
        i = i + 1
    file_original.close()
    file_unknow.close()    

if __name__ == "__main__":
    original = sys.argv[1]
    unknow = sys.argv[2]
    sub = sys.argv[3]
    pos = (int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    replace(original, sub, pos)
    replace(unknow, sub, pos)
    if compare(original, unknow):
        print("Les images sont différentes.")
    else:
        print("Les images sont identiques.")
            

