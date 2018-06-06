import cv2
import numpy as np
import argparse
cap = cv2.VideoCapture(0)
from PIL import Image
import pytesseract
import datetime
import time
Y1 = 650
Y2 = 812

X1 = 1172
X2 = 1282
X3 = 1391



from skimage.measure import compare_ssim as ssim
import glob, os
import mysql;
import mysql.connector;
now = datetime.datetime.now()
date1 = str(now.year) + "-0" + str(now.month) + "-" + str(now.day)
today1 = date1 + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
today2 = date1 + " 00:01:00"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
arena1 = "bla"

try:
    connection = mysql.connector.connect(host = "", user = "", passwd = "", db = "")
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
    #s = ssim(imageA, imageB)
    m = mse(imageA, imageB)



#    print str(raidname) + " " + title + str(s) + " " + str(m)
    if m < 205:
        raidfound = 1
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
 
        data = ("5", today2, raidstart, raidend, None, "0", "0", "0",  "2018-05-12 00:28:13", guid)
        cursor.execute(query, data)

        connection.commit()
        return 1


def compare_Yellow(imageA, imageB, title, raidname, guid):
   # s = ssim(imageA, imageB)
    m = mse(imageA, imageB)



#    print str(raidname) + " " + title + str(s) + " " + str(m)
    if m < 150:
        raidfound = 1
        col = Image.open("raidtimer.png")
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<185 else 255, '1')
        bw.save("cropped_timer_bw.jpg")
    
        timer = pytesseract.image_to_string(Image.open("cropped_timer_bw.jpg"),config='digits')
        out_text =  "\n\n" + "Yellow Egg found at Gym: " + title + " Starting at " + timer +"\n"
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
 
        data = ("3", today2, raidstart, raidend, "0", "0", "0", "0",  "2018-05-12 00:28:13", guid)
        cursor.execute(query, data)

        connection.commit()
        return 1



def compare_Pink(imageA, imageB, title, raidname, guid):
   # s = ssim(imageA, imageB)
    m = mse(imageA, imageB)



#    print str(raidname) + " " + title + str(s) + " " + str(m)
    if m < 150:
        raidfound = 1
        col = Image.open("raidtimer.png")
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<185 else 255, '1')
        bw.save("cropped_timer_bw.jpg")
    
        timer = pytesseract.image_to_string(Image.open("cropped_timer_bw.jpg"),config='digits')
        out_text =  "\n\n" + "Pink Egg found at Gym: " + title + " Starting at " + timer +"\n"
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
 
        data = ("1", today2, raidstart, raidend, "0", "0", "0", "0",  "2018-05-12 00:28:13", guid)
        cursor.execute(query, data)

        connection.commit()
        return 1        

def compare_images2(imageA, imageB):
    #s = ssim(imageA, imageB)
    m = mse(imageA, imageB)
    #print "compare 2 " + str(m)
    if m < 260:
        return 1
    else:
        return 0

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

    raidlevel = image2[108:124, 27:97]
    raidlevel = cv2.resize(raidtimer, (0,0), fx=3, fy=3) 
    cv2.imwrite("raidlevel.png", raidtimer)
	
# load the images -- the original, the original + contrast,
# and the original + photoshop
    original = cv2.imread("raidpic" + str(i) +".png")
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    original2 = cv2.imread("raidpic" + str(i) +".png")
#gyms


    schloss = cv2.imread("raids/schloss/lvl5.png")
    schloss = cv2.cvtColor(schloss, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, schloss, "schloss", i, "2f00a6c307c04fc0b687df0631ab99b3.12")
    if foundraid == 1:
        raidfound = 1
    
    schlossMarmotafel = cv2.imread("raids/SchlossMarmortafel/lvl5.png")
    schlossMarmotafel = cv2.cvtColor(schlossMarmotafel, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, schlossMarmotafel, "schlossMarmotafel", i, "7be1f2ef992a478396ce93b84a8ba0c5.16")
    
    schlossMarmotafelPink = cv2.imread("raids/SchlossMarmortafel/pink.png")
    schlossMarmotafelPink = cv2.cvtColor(schlossMarmotafelPink, cv2.COLOR_BGR2GRAY)
    foundraid = compare_Pink(original, schlossMarmotafelPink, "schlossMarmotafel", i, "7be1f2ef992a478396ce93b84a8ba0c5.16")
    if foundraid == 1:
        raidfound = 1

    kulturfoyer = cv2.imread("raids/kulturfoyer/lvl5.png")
    kulturfoyer = cv2.cvtColor(kulturfoyer, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, kulturfoyer, "kulturfoyer", i, "273733b3710c4a22bd39a779335275b3.16")
    if foundraid == 1:
        raidfound = 1

    steinfamilie = cv2.imread("raids/steinfamilie/lvl5.png")
    steinfamilie = cv2.cvtColor(steinfamilie, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, steinfamilie, "steinfamilie", i, "1f4b284a64e54cc1b82ff81eeceb4353.16")
    if foundraid == 1:
        raidfound = 1

    Kriegerdenkmal = cv2.imread("raids/Kriegerdenkmal/lvl5.png")
    Kriegerdenkmal = cv2.cvtColor(Kriegerdenkmal, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, Kriegerdenkmal, "Kriegerdenkmal", i, "bad8815a2bdf43ef8fbf1663e896b97a.16")
    if foundraid == 1:
        raidfound = 1

    rosentraegerin = cv2.imread("raids/rosentraegerin/lvl5.png")
    rosentraegerin = cv2.cvtColor(rosentraegerin, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, rosentraegerin, "rosentraegerin", i, "1111111111111111111111")
    if foundraid == 1:
        raidfound = 1

    hausderwirtschaftsf = cv2.imread("raids/hausderwirtschaftsf/lvl5.png")
    hausderwirtschaftsf = cv2.cvtColor(hausderwirtschaftsf, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, hausderwirtschaftsf, "hausderwirtschaftsf", i, "9e43335e983a42a4a08e2f6235191899.16")   
    if foundraid == 1:
        raidfound = 1

    rathaus = cv2.imread("raids/rathaus/lvl5.png")
    rathaus = cv2.cvtColor(rathaus, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, rathaus, "rathaus", i, "f6708c43071d4d5a8da78241a58afc38.12")
    if foundraid == 1:
        raidfound = 1

    schmollerbunker = cv2.imread("raids/schmollerbunker/lvl5.png")
    schmollerbunker = cv2.cvtColor(schmollerbunker, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, schmollerbunker, "schmollerbunker", i, "e06bf065c750404d8ab3901350315d6b.12")
    if foundraid == 1:
        raidfound = 1

    sitzplastik = cv2.imread("raids/sitzplastik/lvl5.png")
    sitzplastik = cv2.cvtColor(sitzplastik, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, sitzplastik, "sitzplastik", i, "396aa27d5c524903b7b90a73b72a92bf.16")
    if foundraid == 1:
        raidfound = 1

    skulpturbahnhof = cv2.imread("raids/skulpturbahnhof/lvl5.png")
    skulpturbahnhof = cv2.cvtColor(skulpturbahnhof, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, skulpturbahnhof, "skulpturbahnhof", i, "aa9566b5eba24554a6bc310304995a0b.16")
    if foundraid == 1:
        raidfound = 1

    ludwigskirche = cv2.imread("raids/ludwigskirche/lvl5.png")
    ludwigskirche = cv2.cvtColor(ludwigskirche, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, ludwigskirche, "ludwigskirche", i, "230c8e74ff84482dac3dafb227400de0.12")
    if foundraid == 1:
        raidfound = 1

    hausboot = cv2.imread("raids/hausboot/lvl5.png")
    hausboot = cv2.cvtColor(hausboot, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, hausboot, "hausboot", i, "688f0ae6818643da945746556e4ae2c0.16")
    if foundraid == 1:
        raidfound = 1

    lva = cv2.imread("raids/lva/lvl5.png")
    lva = cv2.cvtColor(lva, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, lva, "lva", i, "b1705db141484ec5918a8410487ce495.16")
    if foundraid == 1:
        raidfound = 1

    turbienekraftwerk = cv2.imread("raids/turbienekraftwerk/lvl5.png")
    turbienekraftwerk = cv2.cvtColor(turbienekraftwerk, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, turbienekraftwerk, "turbienekraftwerk", i, "5dd0708f475a439d9cf40de9f32969ba.16")
    if foundraid == 1:
        raidfound = 1

    zeichendesgeheimen = cv2.imread("raids/zeichendesgeheimen/lvl5.png")
    zeichendesgeheimen = cv2.cvtColor(zeichendesgeheimen, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, zeichendesgeheimen, "zeichendesgeheimen", i, "3644762019624356b34452548f3b8c07.16")
    if foundraid == 1:
        raidfound = 1

    tth = cv2.imread("raids/tth/lvl5.png")
    tth = cv2.cvtColor(tth, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, tth, "tth", i, "e2427adb9bbf48da8b551ffead255c7d.16")
    if foundraid == 1:
        raidfound = 1

    dragonlord = cv2.imread("raids/dragonlord/lvl5.png")
    dragonlord = cv2.cvtColor(dragonlord, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, dragonlord, "dragonlord", i, "4e55e00350914c60b4ee9c139c4e739e.16")
    if foundraid == 1:
        raidfound = 1

    postbank = cv2.imread("raids/postbank/lvl5.png")
    postbank = cv2.cvtColor(postbank, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, postbank, "postbank", i, "49615ad4194b415bab19214005558d20.16")
    if foundraid == 1:
        raidfound = 1

    horus = cv2.imread("raids/horus/lvl5.png")
    horus = cv2.cvtColor(horus, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, horus, "horus", i, "aeca11a21d97413da63b7fd6aa352348.16")
    if foundraid == 1:
        raidfound = 1

    holzgiraffe = cv2.imread("raids/holzgiraffe/lvl5.png")
    holzgiraffe = cv2.cvtColor(holzgiraffe, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, holzgiraffe, "holzgiraffe", i, "10c2be75638b4586981348a8e186dcb5.16")
    if foundraid == 1:
        raidfound = 1

    OHG = cv2.imread("raids/OHG/lvl5.png")
    OHG = cv2.cvtColor(OHG, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, OHG, "OHG", i, "1bf249483dfe480bb8f37de68810bb3f.16")
    if foundraid == 1:
        raidfound = 1

    grafitti = cv2.imread("raids/grafitti/lvl5.png")
    grafitti = cv2.cvtColor(grafitti, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, grafitti, "grafitti", i, "ebb7362772934f3faf0b1f6a4e2410ab.16")
    if foundraid == 1:
        raidfound = 1

    eisenbahnbruecke = cv2.imread("raids/eisenbahnbruecke/lvl5.png")
    eisenbahnbruecke = cv2.cvtColor(eisenbahnbruecke, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, eisenbahnbruecke, "eisenbahnbruecke", i, "34805ad67f6c42b397ed348d03e80788.11")
    if foundraid == 1:
        raidfound = 1

    kunstwerk = cv2.imread("raids/kunstwerk/lvl5.png")
    kunstwerk = cv2.cvtColor(kunstwerk, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, kunstwerk, "kunstwerk", i, "18f080e9f8274d9082c18e20b5244104.16")
    if foundraid == 1:
        raidfound = 1

    roemerkastell = cv2.imread("raids/roemerkastell/lvl5.png")
    roemerkastell = cv2.cvtColor(roemerkastell, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, roemerkastell, "roemerkastell", i, "d6232b6b129c4447af70e7a938970972.12")
    if foundraid == 1:
        raidfound = 1

    mariastatue = cv2.imread("raids/mariastatue/lvl5.png")
    mariastatue = cv2.cvtColor(mariastatue, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, mariastatue, "mariastatue", i, "726a19bd6f89409487e74f0eeba371a7.16")
    if foundraid == 1:
        raidfound = 1

    zwerg = cv2.imread("raids/zwerg/lvl5.png")
    zwergYellow = cv2.imread("raids/zwerg/yellow.png")
    zwergPink = cv2.imread("raids/zwerg/pink.png")
    zwerg = cv2.cvtColor(zwerg, cv2.COLOR_BGR2GRAY)
    zwergYellow = cv2.cvtColor(zwergYellow, cv2.COLOR_BGR2GRAY)
    zwergPink = cv2.cvtColor(zwergPink, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, zwerg, "zwerg", i, "69327301919246729c013e59b8e341b5.16")
    foundraid = compare_Yellow(original, zwergYellow, "zwerg", i, "69327301919246729c013e59b8e341b5.16")
    foundraid = compare_Pink(original, zwergPink, "zwerg", i, "69327301919246729c013e59b8e341b5.16")
    if foundraid == 1:
        raidfound = 1

    europagallerie = cv2.imread("raids/europagallerie/lvl5.png")
    europagallerie = cv2.cvtColor(europagallerie, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, europagallerie, "europagallerie", i, "ba3f976e23bc4ad5be8e6f15c25ca286.11")
    if foundraid == 1:
        raidfound = 1

    kufa = cv2.imread("raids/kufa/lvl5.png")
    kufa = cv2.cvtColor(kufa, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, kufa, "kufa", i, "a8269bf8e17c4ac29fba5313aece31c8.16")
    if foundraid == 1:
        raidfound = 1

    kulturverein = cv2.imread("raids/kulturverein/lvl5.png")
    kulturverein = cv2.cvtColor(kulturverein, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, kulturverein, "kulturverein", i, "fab98b63669e4ad896cf2c96e7ec5164.16")
    if foundraid == 1:
        raidfound = 1

    rondell = cv2.imread("raids/rondell/lvl5.png")
    rondell = cv2.cvtColor(rondell, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, rondell, "rondell", i, "3a90207ae74d4d0da740f71c73ea2628.16")
    if foundraid == 1:
        raidfound = 1

    erzengel = cv2.imread("raids/erzengel/lvl5.png")
    erzengel = cv2.cvtColor(erzengel, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, erzengel, "erzengel", i, "6105cafd7bf54bdfb84191208695452e.16")
    if foundraid == 1:
        raidfound = 1

    kirchederjugend = cv2.imread("raids/kirchederjugend/lvl5.png")
    kirchederjugend = cv2.cvtColor(kirchederjugend, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, kirchederjugend, "kirchederjugend", i, "12ba20a9649e45cb80f45d208c6b3424.16")
    if foundraid == 1:
        raidfound = 1

    hauptbahnhof = cv2.imread("raids/hauptbahnhof/lvl5.png")
    hauptbahnhof = cv2.cvtColor(hauptbahnhof, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, hauptbahnhof, "hauptbahnhof", i, "ac4714164c594edc9e99f2c5aea829e5.12")
    if foundraid == 1:
        raidfound = 1

    staatsteather = cv2.imread("raids/staatsteather/lvl5.png")
    staatsteather = cv2.cvtColor(staatsteather, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, staatsteather, "staatsteather", i, "f9ce3c4cd22b4eaf991f7b747b7c709e.12")
    if foundraid == 1:
        raidfound = 1

    chinastatue = cv2.imread("raids/chinastatue/lvl5.png")
    chinastatue = cv2.cvtColor(chinastatue, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, chinastatue, "chinastatue", i, "e76e4963e366458eaf962917e37a78ba.16")
    if foundraid == 1:
        raidfound = 1
    silo = cv2.imread("raids/silo/lvl5.png")
    silo = cv2.cvtColor(silo, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, silo, "silo", i, "860a0689e7d34120822a0b6353511173.11")
    if foundraid == 1:
        raidfound = 1

    schlossKirche = cv2.imread("raids/schlossKirche/lvl5.png")
    schlossKirche = cv2.cvtColor(schlossKirche, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, schlossKirche, "schlossKirche", i, "453d8d73717f45d1ab79dec2354c29bd.16")
    if foundraid == 1:
        raidfound = 1

    mario = cv2.imread("raids/mario/lvl5.png")
    mario = cv2.cvtColor(mario, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, mario, "mario", i, "2ca9839496f948389f12ec5a8f4b0964.16")
    if foundraid == 1:
        raidfound = 1

    blauerHirsch = cv2.imread("raids/blauerHirsch/lvl5.png")
    blauerHirsch = cv2.cvtColor(blauerHirsch, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, blauerHirsch, "blauerHirsch", i, "272733b9f9a3463fa1c93ce368bd2f7d.16")
    if foundraid == 1:
        raidfound = 1

    wandkunst = cv2.imread("raids/wandkunst/lvl5.png")
    wandkunst = cv2.cvtColor(wandkunst, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, wandkunst, "wandkunst", i, "271d788444fe416986ff3c88e0d1465f.16")
    if foundraid == 1:
        raidfound = 1

    juzstarnual = cv2.imread("raids/juzstarnual/lvl5.png")
    juzstarnual = cv2.cvtColor(juzstarnual, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, juzstarnual, "juzstarnual", i, "90581960acca41c1b912e10001f71232.16")
    if foundraid == 1:
        raidfound = 1

    unsichtbar = cv2.imread("raids/unsichtbar/lvl5.png")
    unsichtbar = cv2.cvtColor(unsichtbar, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, unsichtbar, "unsichtbar", i, "47f192d6b15a47c78f10d91e42c87462.16")
    if foundraid == 1:
        raidfound = 1

    gefallenendenkmal = cv2.imread("raids/gefallenendenkmal/lvl5.png")
    gefallenendenkmal = cv2.cvtColor(gefallenendenkmal, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, gefallenendenkmal, "gefallenendenkmal", i, "2c9591d04e6d4390ba98045c38e09dc3.16")
    if foundraid == 1:
        raidfound = 1

    evangelisch = cv2.imread("raids/evangelisch/lvl5.png")
    evangelisch = cv2.cvtColor(evangelisch, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, evangelisch, "evangelisch", i, "523090366f9c4fe5ac6ba379664e839b.16")
    if foundraid == 1:
        raidfound = 1


    schlossrueckseite = cv2.imread("raids/schlossrueckseite/lvl5.png")
    schlossrueckseite = cv2.cvtColor(schlossrueckseite, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, schlossrueckseite, "schlossrueckseite", i, "376f3f44807443d5a1d66631b91c7276.12")
    schlossrueckseitePink = cv2.imread("raids/schlossrueckseite/pink.png")
    schlossrueckseitePink = cv2.cvtColor(schlossrueckseitePink, cv2.COLOR_BGR2GRAY)
    foundraid = compare_Pink(original, schlossrueckseitePink, "schlossrueckseite", i, "376f3f44807443d5a1d66631b91c7276.12")
    if foundraid == 1:
        raidfound = 1
 

    brunnenmalstadt = cv2.imread("raids/brunnenmalstadt/lvl5.png")
    brunnenmalstadt = cv2.cvtColor(brunnenmalstadt, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, brunnenmalstadt, "brunnenmalstadt", i, "6f7cd641b07c4e77b82d064d303e09c6.16")
    if foundraid == 1:
        raidfound = 1

    headsonwall = cv2.imread("raids/headsonwall/lvl5.png")
    headsonwall = cv2.cvtColor(headsonwall, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, headsonwall, "headsonwall", i, "2575bfe00c394f5a96f45776c39efec3.16")
    if foundraid == 1:
        raidfound = 1
 
    htw = cv2.imread("raids/htw/lvl5.png")
    htw = cv2.cvtColor(htw, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, htw, "htw", i, "3039802a04604d24a2b82d5b48460f0b.16")
    if foundraid == 1:
        raidfound = 1

    ufo = cv2.imread("raids/ufo/lvl5.png")
    ufo = cv2.cvtColor(ufo, cv2.COLOR_BGR2GRAY)
    foundraid = compare_images(original, ufo, "ufo", i,"ac32bb06fb6944a69cb39de80dcb760e.16")
    if foundraid == 1:
        raidfound = 1
 
##############################################
    if raidfound == 0:
        unknownfound = 0
        for file in glob.glob("unknown/*.png"):
            
            newimage = cv2.imread(str(file))
            newimage = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
            foundunknown = compare_images2(original, newimage)  
            if foundunknown == 1:
                unknownfound = 1
        
        if unknownfound == 0:
            raidpic2 = image1[0:110, 0:120]
            name22 = time.time()
            cv2.imwrite("unknown/unknown" + str(name22) +".png", raidpic2)	




    i = i+1

	
	













