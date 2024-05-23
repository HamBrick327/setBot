import cv2
import numpy as np
import os
from time import sleep, time

''' working with test image, need to ensure carpet is not in image. '''

## get temp image
image = cv2.imread('/home/hambrick/setbot/grayimage.jpg')

def detectTable(img):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayimage.jpg", gray)
    # Apply binary thresholding
    mask = cv2.inRange(gray, 230, 255)
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)

    rotates = []

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ## --> tuple of all contours
    
    sumw = [0, 0]
    sumh = [0, 0]
    # Draw rectangles on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    ## get the "center" of the card, for each card
    for i, contour in enumerate(contours): ## I barely understand how half of this stuff works, but dammit I'm gonna make it work
        if cv2.contourArea(contour) < 10_000:
            # np.delete(contours, contour)
            continue

        print(cv2.contourArea(contour))

        x, y, w, h = cv2.boundingRect(contour)
        # print(x, y)
        innerRect = cv2.minAreaRect(contour)
        center = ((x + (w//2)), (y + (h//2)))


        box = np.float32(cv2.boxPoints(innerRect))
        angle = innerRect[2]
        if angle > 45:
            angle = 90 - angle
            angle *= -1
        elif angle <= 45:
            # angle *= -1
            ## very useful
            angle = angle

        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.drawContours(image, [np.int32(box)], 0, (255, 255, 0), 2)
        
        # print(center)
        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

        rotated = rotated[y:y+h, x:x+w]

        cv2.imwrite(os.path.join("cards", f"rotated{i}.jpg"), rotated)

    ## find card color, then bitwise compare to known cards
    for i, im in enumerate(os.listdir("./cards")):
        im = os.path.join(os.getcwd(), "cards", im)
        print(im)
        img = cv2.imread(im)

    # Show the image with detected rectangles
    print(len(os.listdir("cards/")), "cards detected")
    cv2.imwrite('DetectedCards.jpg', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detectTable(image)