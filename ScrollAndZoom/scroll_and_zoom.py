from tkinter import *
import tkinter as tk
from scrolling_funcitonality import ScrollableImage
from PIL import ImageTk, Image

# create a window
my_window = tk.Tk()  # parent window
my_window.configure(bg='gray')
width, height = 1000, 1000

dim = str(width) + "x" + str(height)
# set the dimension for the window
my_window.geometry(dim)
my_window.title("Zoom In and Out")

# image
image_window = ScrollableImage(
    my_window,
    image=ImageTk.PhotoImage(Image.open(r"C:\Users\DELL\Downloads\screen.jpg").resize((2000, 1000),
                                                                                      Image.LANCZOS)),
    scrollbarwidth=6,
    width=1000,
    height=500
)
image_window.grid(row=1, column=1)
image_width, image_height = 2000, 1000


# Functionality
def Zoom(command):
    zoom = 1.8
    global image_width, image_height
    if command == "in":
        image_width = int(image_width * 1.8)
        image_height = int(image_width * 1.8)
        image_window = ScrollableImage(
            my_window,
            image=ImageTk.PhotoImage(Image.open(r"C:\Users\DELL\Downloads\screen.jpg").resize((image_width, image_height),
                                                                                              Image.LANCZOS)),
            scrollbarwidth=6,
            width=1000,
            height=500
        )
        image_window.grid(row=1, column=1)
    elif command == "out" and image_width > 50 and image_height > 50:
        image_width = int(image_width / 1.8)
        image_height = int(image_height / 1.8)
        image_window = ScrollableImage(
            my_window,
            image=ImageTk.PhotoImage(Image.open(r"C:\Users\DELL\Downloads\screen.jpg").resize((image_width, image_height),
                                                                                              Image.LANCZOS)),
            scrollbarwidth=6,
            width=1000,
            height=500
        )
        image_window.grid(row=1, column=1)

# Zoom In Button
zoom_in_button = tk.Button(my_window, text="Zoom In", command=lambda: Zoom("in"))
zoom_in_button.grid(row=0, column=0, padx=10, pady=10)
# Zoom Out Button
zoom_out_button = tk.Button(my_window, text="Zoom Out", command=lambda: Zoom("out"))
zoom_out_button.grid(row=0, column=1, padx=10, pady=10)


my_window.mainloop()
