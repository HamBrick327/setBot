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
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)

    rotates = []

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ## --> tuple of all contours
    
    sumw = [0, 0]
    sumh = [0, 0]
    # Draw rectangles on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # for contour in contours:
    #     if cv2.contourArea(contour) < 2000:
    #         contours = list(contours)
    #         contours.remove(contour)


    print(f"{len(contours)} cards detected")
    ## get the "center" of the card, for each card
    for i, contour in enumerate(contours): ## I barely understand how half of this stuff works, but dammit I'm gonna make it work
        x, y, w, h = cv2.boundingRect(contour)
        print(x, y)
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

        cv2.circle(image, center, 2, (0, 0, 255), 3)
        # cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.drawContours(image, [np.int32(box)], 0, (255, 255, 0), 2)
        
        print(center)
        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

        rotated = rotated[y:y+h, x:x+w]

        cv2.imwrite(f"rotated{i}.jpg", rotated)


    # Show the image with detected rectangles
    cv2.imwrite('DetectedCards.jpg', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detectTable(image)