import cv2
import numpy as np

''' working with test image, need to ensure carpet is not in image. '''

## get temp image
image = cv2.imread('./testimage3.png')

def detectTable(img):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    mask = cv2.inRange(gray, 240, 255)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ## --> tuple of all contours
    
    sumw = [0, 0]
    sumh = [0, 0]
    # Draw rectangles on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    print(f"{len(contours)} cards detected")
    ## get the "center" of the card, for each card
    for contour in contours:
        outerx, outery, outerw, outerh = cv2.boundingRect(contour)
        innerRect = cv2.minAreaRect(contour)

        box = np.int32(cv2.boxPoints(innerRect))
        dst_pts = np.array([[0, height-1],
                        [0, 0],
                        [width-1, 0],
                        [width-1, height-1]], dtype="float32")

        center = (int((outerx + (outerx+outerw))/2), int((outery + (outery+outerh))/2))

        warped = cv2.warpPerspective(image, box, (180, 266))

        cv2.circle(image, center, 5, (0, 0, 255), 2)
        cv2.rectangle(image, (outerx, outery), (outerx+outerw, outery+outerh), (255, 0, 0), 2)
        cv2.rectangle(image, (box[0, 0], box[0, 1]), (box[2, 0], box[2, 1]), (255, 255, 0), 2)

    # Show the image with detected rectangles
    cv2.imshow('Detected Rectangles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detectTable(image)