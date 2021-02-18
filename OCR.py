import numpy as np
import matplotlib.pyplot as plt 
import cv2
import pytesseract
import csv
import os

def prep(image):
    filtered = cv2.bilateralFilter(image, 30, 60, 15)
    gray = cv2.cvtColor(filtered,cv2.COLOR_BGR2GRAY)

    return gray



def fullocr_single(image):
    text = pytesseract.image_to_string(image,config=r'--oem 3 --psm 6', lang = 'eng')
    return text