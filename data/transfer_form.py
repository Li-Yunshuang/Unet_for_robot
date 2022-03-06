import PIL.Image
import os
i=0
path = "/home/lys/UNet/data/test/"
savepath = "/home/lys/UNet/data/test/"
filelist = os.listdir(path)
print(filelist)
for file in filelist:
    im = PIL.Image.open(path+filelist[i])
    filename = os.path.splitext(file)[0]
    im.save(savepath+filename+'.jpg') # or 'test.tif'
    i=i+1
