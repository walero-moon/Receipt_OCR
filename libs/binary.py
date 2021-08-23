import cv2

class Binarize():
    def __init__(self, image):
        self.image = image

    def greyscale(self):
        """Turns image into greyscale"""
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def binarize(self):
        """Finishes binarizing the image (black and white)"""
        thresh, im_bw = cv2.threshold(self.greyscale(), 130, 200, cv2.THRESH_BINARY)
        cv2.imwrite("temp/bw_image.jpg", im_bw)
        return im_bw

if __name__ == '__main__':
    img_file = "../receipt.jpg"
    img = cv2.imread(img_file)
    binarize = Binarize(img)
    binarize.binarize()