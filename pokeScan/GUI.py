import tkinter as tk
from tkinter import filedialog, Label
from pokeScan.ImageHandler import ImageHandler

class GUIHandler:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Vision App")

        # Set the initial size of the window
        window_width = 800
        window_height = 600

        # Get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the center position
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        # Create and place the buttons
        self.open_button = tk.Button(self.root, text="Open Image", command=self.open_file)
        self.open_button.pack(pady=10)

        self.process_button = tk.Button(self.root, text="Process Image", command=self.process_image_command)
        self.process_button.pack(pady=10)

        # Create and place the image display label
        self.image_label = Label(self.root)
        self.image_label.pack(pady=10)

        # Initialize variables to store images
        self.img = None
        self.img_display = None

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        if file_path:
            self.img, self.img_display = ImageHandler.load_image(file_path)
            self.image_label.config(image=self.img_display)
            self.image_label.image = self.img_display

    def process_image_command(self):
        if self.img is not None:
            self.img_display = ImageHandler.process_image(self.img)
            self.image_label.config(image=self.img_display)
            self.image_label.image = self.img_display