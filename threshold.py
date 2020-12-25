from PIL import Image

def threshold(img):
    pix = img.load()
    pix = [sum(pix[i,j])/3 for i in range(img.size[0]) for j in range(img.size[1])]
    min, max = 255, 0
    for i in pix:
        if max < i < 128:
            max = i
        if 128 < i < min:
            min = i
    return (max, min)

img=Image.open('F:\课程\数学建模\作业\实验\实验1\其它\pic4.jpg')
bound=threshold(img)
print(bound)

