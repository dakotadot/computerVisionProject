# This is my main method where the application will launch from
# I would like this file to be where the application launches from
# and stuff. Trying to envision it currently. Really want to focus
# on solid principles and building a nice looking application. 

import tkinter as tk
from pokeScan.GUI import GUIHandler
from pokeScan import ImageHandler

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIHandler(root)
    root.mainloop()