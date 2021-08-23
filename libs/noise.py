import numpy as np
import cv2

class Noise():
    def __init__(self, image):
        self.image = image

    def noise_removal(self):
        """Removes noise from the image"""
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(self.image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 3)
        cv2.imwrite("temp/no_noise.jpg", image)
        return image

if __name__ == '__main__':
    img_file = "./temp/bw_image.jpg"
    img = cv2.imread(img_file)
    noise = Noise(img)
    noise.noise_removal()