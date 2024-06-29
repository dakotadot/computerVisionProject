import ImageHandler
import tkinter as Tk

class GUI():

    root = Tk()
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