import cv2
import numpy as np
import os

if __name__ == "__main__":
    i = 0
    path = "/home/lys/UNet/data/test/"
    savepath = "/home/lys/UNet/data/test/"
    filelist = os.listdir(path)
    for file in filelist:
        img = cv2.imread(path+filelist[i])
    #获取图片的宽和高
        width,height = img.shape[:2][::-1]
    #将图片缩小便于显示观看
        # img_resize = cv2.resize(img,
        # (int(width*0.5),int(height*0.5)),interpolation=cv2.INTER_CUBIC)
        # cv2.imshow("img",img_resize)
        # print("img_reisze shape:{}".format(np.shape(img_resize)))

    #将图片转为灰度图
        img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        # cv2.imshow("img_gray",img_gray)


        filename = os.path.splitext(file)[0]
        cv2.imwrite(savepath+filename+'.jpg', img_gray)
        print("img_gray shape:{}".format(np.shape(img_gray)))
        i = i+1
        # cv2.waitKey()
