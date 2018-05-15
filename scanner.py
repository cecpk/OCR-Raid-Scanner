import cv2
import numpy as np
import argparse
cap = cv2.VideoCapture(0)
from PIL import Image
import pytesseract
import datetime
import time
from skimage.measure import compare_ssim as ssim
import glob, os
import mysql;
import mysql.connector;

# coordinates of the raid pics
Y1 = 650
Y2 = 812

X1 = 1172
X2 = 1282
X3 = 1391




now = datetime.datetime.now()
date1 = str(now.year) + "-0" + str(now.month) + "-" + str(now.day)
today1 = date1 + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
today2 = date1 + " 00:01:00"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
arena1 = "bla"

try:
    connection = mysql.connector.connect(host = "localhost", user = "", passwd = "", db = "")
except:
    print "Keine Verbindung zum Server"
    exit(0)
# load the image
img = cv2.imread(args["image"])

###raid1
raid1 = img[Y1-50:Y1+100, X1-60:X1+60]
cv2.imwrite("raid1.png", raid1)

###raid2
raid2 = img[Y1-50:Y1+100, X2-60:X2+60]
cv2.imwrite("raid2.png", raid2)

###raid3
raid3 = img[Y1-50:Y1+100, X3-60:X3+60]
cv2.imwrite("raid3.png", raid3)

###raid4
raid4 = img[Y2-50:Y2+100, X1-60:X1+60]
cv2.imwrite("raid4.png", raid4)

###raid5
raid5 = img[Y2-50:Y2+100, X2-60:X2+60]
cv2.imwrite("raid5.png", raid5)

###raid3
raid6 = img[Y2-50:Y2+100, X3-60:X3+60]
cv2.imwrite("raid6.png", raid6)

def compare_images(imageA, imageB, title, raidname, guid):
    s = ssim(imageA, imageB)
    m = mse(imageA, imageB)




    if m < 260:

        col = Image.open("raidtimer.png")
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<185 else 255, '1')
        bw.save("cropped_timer_bw.jpg")
    
        timer = pytesseract.image_to_string(Image.open("cropped_timer_bw.jpg"),config='digits')
        out_text =  "\n\n" + "Latias Raid found at Gym: " + title + " Starting at " + timer +"\n"
        print(out_text)
        print str(m) + "\n\n"

        aab = datetime.datetime(100,1,1,int(timer[:2]),int(timer[-2:]),00)
        bba = aab - datetime.timedelta(0,7200) # days, seconds, then other fields.
        raidstart = date1 + " " + str(bba.time()) 

        a = datetime.datetime(100,1,1,int(timer[:2]),int(timer[-2:]),00)
        b = a - datetime.timedelta(0,4500) # days, seconds, then other fields.
        raidend = date1 + " " + str(b.time()) 
        

        cursor = connection.cursor()
		
        query = " UPDATE raid SET level = %s, spawn=%s, start=%s, end=%s, pokemon_id = %s, cp = %s, move_1 = %s, move_2 = %s, last_scanned=%s WHERE gym_id = %s "
 
        data = ("5", today2, raidstart, raidend, "0", "0", "0", "0",  "2018-05-12 00:28:13", guid)
        cursor.execute(query, data)

        connection.commit()
   



def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

i = 1

while i < 7:
    raidfound = 0
    unknownfound = 0
    image1 = cv2.imread("raid" + str(i) +".png")
    raidpic = image1[0:110, 0:120]
    cv2.imwrite("raidpic" + str(i) +".png", raidpic)

    image2 = cv2.imread("raid" + str(i) +".png")
    raidtimer = image2[108:124, 27:97]
    raidtimer = cv2.resize(raidtimer, (0,0), fx=3, fy=3) 
    cv2.imwrite("raidtimer.png", raidtimer)
	

    original = cv2.imread("raidpic" + str(i) +".png")
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    original2 = cv2.imread("raidpic" + str(i) +".png")
#gyms

	
    GYM1 = cv2.imread("raids/GYM1/lvl5.png")
    GYM1 = cv2.cvtColor(GYM1, cv2.COLOR_BGR2GRAY)
    compare_images(original, GYM1, "GYM1", i, "GUID1")
	
    GYM2 = cv2.imread("raids/GYM1Marmortafel/lvl5.png")
    GYM2 = cv2.cvtColor(GYM2, cv2.COLOR_BGR2GRAY)
    compare_images(original, GYM2, "GYM2", i, "GUID2")





    i = i+1

	
	













