#import libraries
import cv2 as cv
import numpy as np

#create image
img = np.zeros((600,900,3),dtype=np.uint8)

#background
cv.rectangle(img,(0,0),(900,500),(255,225,85), -1)
cv.rectangle(img,(0,500),(900,600),(75,180,70), -1)

#sun
cv.circle(img,(200,100),50,(0,255,255), -1)
cv.circle(img,(200,100),65,(220,255,255), 15)

# *** TREE 1 ***

#tree stem
cv.line(img, (710, 500), (710, 420), (30,65,155), 15)

#tree leafs
triangle1 = np.array([[650,420],[770,420],[710,260]])
cv.fillPoly(img,[triangle1],(75,200,70))

# *** TREE 2 ***

#tree stem
cv.line(img, (600, 500), (600, 420), (30,65,155), 25)

#tree leafs
triangle = np.array([[500,440],[700,440], [600,75]], dtype=np.int32)
cv.fillPoly(img, [triangle], (75,200,70))

#text
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img,"Hey There",(100,500),font,1.5,(255,255,255), 2)

# save image
cv.imwrite("Graph.jpg",img)

#show image
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()