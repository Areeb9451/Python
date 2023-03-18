f = open("Image.jpg",'rb')

f1 = open('myPic.jpg','wb')

for i in f:
    f1.write(i)

