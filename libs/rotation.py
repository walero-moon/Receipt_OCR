import cv2
import numpy as np

class Rotate():
    def __init__(self, image):
        self.image = image

    def getSkewAngle(self) -> float:
        """ Gets skew angle from image """
        # Prep image, copy, convert to gray scale, blur, and threshold
        newImage = self.image.copy()
        gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (9, 9), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Apply dilate to merge text into meaningful lines/paragraphs.
        # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
        # But use smaller kernel on Y axis to separate between different blocks of text
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
        dilate = cv2.dilate(thresh, kernel, iterations=2)

        # Find all contours
        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)
        for c in contours:
            rect = cv2.boundingRect(c)
            x,y,w,h = rect
            cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

        # Find largest contour and surround in min area box
        largestContour = contours[0]
        print (len(contours))
        minAreaRect = cv2.minAreaRect(largestContour)
        cv2.imwrite("temp/boxes.jpg", newImage)
        # Determine the angle. Convert it to the value that was originally used to obtain skewed image
        angle = minAreaRect[-1]
        if angle < -45:
            angle = 90 + angle
        return -1.0 * angle
    
    # Rotate the image around its center
    def rotateImage(self, angle: float):
        """  Rotates the image """
        newImage = self.image.copy()
        (h, w) = newImage.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return newImage

    # Deskew image
    def deskew(self):
        """ Deskews the image """
        angle = self.getSkewAngle()
        image = self.rotateImage(-1.0 * angle)
        cv2.imwrite("temp/no_noise_deskewed.jpg", image)
        return(image)

if __name__ == '__main__':
    img_file = "./temp/no_noise_copy_border.jpg"
    img = cv2.imread(img_file)
    rotate = Rotate(img)
    rotate.deskew()
    