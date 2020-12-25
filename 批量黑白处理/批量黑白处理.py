# 2020年12月13日22:37:32
# 效果不佳
import os
from PIL import Image

def strengthen(img):
    pix = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if sum(pix[i, j]) / 3<128:
                pix[i,j]=(0,0,0)
            else:
                pix[i, j] = (255, 255, 255)
    return img

num=1
path=r'G:\软件文件存储\QQ\MobileFile'
outfolder=r'C:\Users\Administrator\Desktop\output'
for folder, subfolders, files in os.walk(path):
    for file in files:
        src = os.path.join(folder, file)
        filename, type = os.path.splitext(file)
        dst = os.path.join(outfolder, f'{num}{type}')
        num += 1
        img = Image.open(src)
        img1 = strengthen(img)
        img1.save(dst)