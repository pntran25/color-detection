import cv2
import numpy as np
import pandas as pd
import argparse
from sklearn.neighbors import KNeighborsClassifier


#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading the image with opencv
img = cv2.imread(img_path)

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# Train a KNN model on RGB values and color names
X = csv[['R', 'G', 'B']]
y = csv['color_name']
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# AI-powered color prediction using KNN
# We convert the RGB input into a DataFrame with column names to match the training format and avoid sklearn warnings
def getColorName(R, G, B):
    input_df = pd.DataFrame([[R, G, B]], columns=['R', 'G', 'B'])
    return knn.predict(input_df)[0]

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):
    display_img = img.copy()
    # Draw rectangle and text if a color has been selected
    if xpos != 0 or ypos != 0:
        cv2.rectangle(display_img,(20,20), (750,60), (b,g,r), -1)
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(display_img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(display_img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        # Draw a larger black circle with a thinner outline at the clicked position
        cv2.circle(display_img, (xpos, ypos), 8, (0, 0, 0), 1)
    cv2.imshow("image", display_img)
    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
