import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class FileOpening(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.button = tk.Button(self, text="Choose file to upload", command=self.browse_file)
        self.label_image = tk.Label(self)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.button.pack(side="top")
        self.label_image.pack(side="top")

    def browse_file(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(title="Select an image file", filetypes=filetypes)
        if filepath:
            image = Image.open(filepath)
            photo = ImageTk.PhotoImage(image)
            self.label_image.configure(image=photo)
            self.label_image.image = photo


root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
win = FileOpening(master=root)
win.mainloop()


