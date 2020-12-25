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

img=Image.open('F:\课程\数学建模\作业\实验\实验1\其它\pic3.jpg')
img1=strengthen(img)
img1.save('F:\课程\数学建模\作业\实验\实验1\其它\pic4.jpg')