#COLOR IDENTIFICATION IN IMAGES
#AUTHOR:SELIZ SURESH KOSHY

import cv2
import numpy as np
import pandas as pd
import argparse

#STEP 1:Reading the image with opencv
img = cv2.imread(r'C:\Users\User1\Downloads\Color Identification\butterfly.jpg')

#STEP 2:declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

#STEP 3:Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]#CSV FILE contents title
csv = pd.read_csv('colors.csv', names=index, header=None)
# a csv file containing the RGB values along with its name has been created and is available online including their hex values.we import this file
#to get the required color and identify it.

#STEP 4:function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):#here the location where the mouse was double clicked is calculated and if the calculated value of all the RGB values is
        #less than minimum then the color in csv file is displayed.
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]#PRINTS THE COLOR NAME AS GIVEN IN CSV FILE
    return cname

#STEP 5:function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param): #TO CHECK IF MOUSE HAS BEEN DOUBKE CLICKED
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
#A window named image pops up displaying the given image       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

#STEP 6:FINALLY DISPLAYS THE COLOR NAME FETCHED FROM CSV FILE AFTER CALCULATING THE LOCATION MOUSE WAS CLICKED IT IS DISPLAYED via A RECTANGLE AT
#THE TOP LEFT CORNER
while(1):

    cv2.imshow("image",img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) 
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
