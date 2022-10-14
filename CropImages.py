import cv2
import glob
import numpy as np
def cropImg(path):
    count = 0
    afterPath = "afterPath/"
    for img in glob.glob(path+"/*.png"):
        print(img)
        image = cv2.imread(img)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
        xMin = 999999
        yMin = 999999
        xMax = 0
        yMax = 0
        for i in range(0,8):
            for x in contours[1][i]:
                xMin = min(xMin,x[0])
                yMin = min(yMin,x[1])
                xMax = max(xMax,x[0])
                yMax = max(yMax,x[1])
        out = image[yMin:yMax+1,xMin:xMax+1]
        cv2.imwrite(afterPath+str(count)+".png", out)
        count = count+1

def partImg(path):
    count = 0
    afterPath = "newImg/"
    for img in glob.glob(path+"/*.png"):
        print(img)
        image = cv2.imread(img)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
        idx = {3,6}
        images = []
        for q in idx:
            yMin = 9999999999
            xMin = 9999999999
            xMax  = 0
            for x in contours[len(contours)-q]:
                for i in x:
                    xMin = min(xMin,i[0])
                    yMin = min(yMin,i[1])
                    xMax = max(xMax,i[0])
            out = image[yMin:,xMin:xMax]
            images.append(out)
        plot_image = np.concatenate(images, axis=1)
        cv2.imwrite(afterPath + str(count) + ".png", plot_image)
        count = count + 1







path = "editImg"
cropImg(path)
path = "afterPath"
partImg(path)





