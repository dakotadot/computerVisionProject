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


root = tk.Tk()
root.title("Computer Vision App")

window_width = 320
window_height = 240

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center position
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Create and place the buttons
open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack(pady=10)

process_button = tk.Button(root, text="Process Image", command=process_image)
process_button.pack(pady=10)

# Create and place the image display label
image_label = Label(root)
image_label.pack(pady=10)

# Run the application
root.mainloop()