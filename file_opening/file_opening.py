import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class FileOpening(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.select_button = tk.Button(self, text="Choose file to upload", command=self.browse_file)
        self.save_button = tk.Button(self, text="Save Image", command=self.save_image)
        self.label_image = tk.Label(self)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.select_button.pack(side="top")
        self.save_button.pack(side="top")
        self.label_image.pack(side="top")

    def browse_file(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(title="Select an image file", filetypes=filetypes)
        if filepath:
            self.image = Image.open(filepath)
            self.photo = ImageTk.PhotoImage(self.image)
            self.label_image.configure(image=self.photo)
            self.label_image.image = self.photo

    def save_image(self):
        if hasattr(self, 'label_image'):
            save_path = filedialog.asksaveasfilename(defaultextension='.jpg')
            if save_path:
                self.image.save(save_path)


root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
win = FileOpening(master=root)
win.mainloop()
