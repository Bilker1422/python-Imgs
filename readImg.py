import cv2
from pytesseract import pytesseract
import os
import re


#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_images = r'newImg/'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file_name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = cv2.imread(path_to_images + file_name)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_boxes(thresh, lang='eng',config='--psm 6')
        for b in data.splitlines():
            b = b.split(' ')
            print(b)

