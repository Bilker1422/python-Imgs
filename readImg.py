import cv2
import pytesseract
import csv
import os


path_to_images = r'newImg/'

def addsomething(word):
    StartTime = ""
    for i in range(0, 4):
        if i < 2:
            StartTime += word[i]
        elif i == 2:
            StartTime += ":" + word[i]
        else:
            StartTime += word[i]
    return StartTime


for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file_name in the folder
    Header = ["Subject", "Start date", "Start time", "End Date", "End Time"]
    fullList = []
    for file_name in file_names:
        #Open image with PIL
        img = cv2.imread(path_to_images + file_name)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
        x = data.split("\n")

        Days = ["SUNDAY", "MONDAY","TUESDAY","WEDNESDAY","THURSDAY"]
        Remove = ["-","_",".",",",]
        for i in x:
            x = i
            for char in Remove:
                x= x.replace(char," ")
            while x.find("  ") != -1:
                x= x.replace("  "," ")
            for d in Days:
                if x.find(d) != -1:
                    list = x.split(" ")
                    editlist = []
                    editlist.append(file_name)
                    editlist.append(list[0])
                    editlist.append(addsomething(list[1]))
                    editlist.append(list[0])
                    editlist.append(addsomething(list[2]))
                    fullList.append(editlist)
    with open('time.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(Header)
        # Use writerows() not writerow()
        writer.writerows(fullList)
