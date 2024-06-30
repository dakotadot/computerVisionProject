# app_components/image_handler.py

import cv2
from PIL import Image, ImageTk

class ImageHandler:
    @staticmethod
    def load_image(file_path):
        """
        Load an image from a file path and convert it to a format suitable for Tkinter.
        """
        img = cv2.imread(file_path)
        img_display = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_display = Image.fromarray(img_display)
        img_display = ImageTk.PhotoImage(img_display)
        return img, img_display

    @staticmethod
    def process_image(img):
        """
        Convert the given image to grayscale and convert it to a format suitable for Tkinter.
        """
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_display = Image.fromarray(gray_img)
        img_display = ImageTk.PhotoImage(img_display)
        return img_display