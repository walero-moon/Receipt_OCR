import cv2

class Border():
    def remove_borders(self, image):
        """ Removes borders from an image """
        contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
        cnt = cntsSorted[-1]
        x, y, w, h = cv2.boundingRect(cnt)
        crop = image[y:y+h, x:x+w]
        return (crop)
    
    def add_borders(self, image):
        """ Adds borders to an image """
        color = [255, 255, 255]
        top, bottom, left, right = [150]*4
        image_with_border = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        return image_with_border

if __name__ == '__main__':
    img_file = "./temp/no_noise_copy_border.jpg"
    img = cv2.imread(img_file)
    border = Border()
    new_img = border.remove_borders(img)
    cv2.imwrite("temp/no_noise_copy_border2.jpg", new_img)




