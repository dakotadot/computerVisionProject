import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import cv2

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if file_path:
        load_image(file_path)

# Function to load and display the image
def load_image(file_path):
    global img, img_display
    img = cv2.imread(file_path)
    img_display = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_display = Image.fromarray(img_display)
    img_display = ImageTk.PhotoImage(img_display)
    
    image_label.config(image=img_display)
    image_label.image = img_display

def process_image():
    global img, img_display
    if img is not None:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_display = Image.fromarray(gray_img)
        img_display = ImageTk.PhotoImage(img_display)
        
        image_label.config(image=img_display)
        image_label.image = img_display