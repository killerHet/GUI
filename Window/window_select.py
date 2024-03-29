import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        master.title('GUI')

        # create the menu bar
        menu_bar = tk.Menu(master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open')
        file_menu.add_command(label='Save')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)
        menu_bar.add_cascade(label='File', menu=file_menu)
        master.config(menu=menu_bar)

        # create the side bar
        side_bar = tk.Frame(master, width=200, height=400, bg='gray')
        side_bar.pack(side='left', fill='y', padx=10, pady=5)

        # create the canvas
        self.canvas = tk.Canvas(master, width=650, height= 400, bg='white')
        self.canvas.pack(side='right', padx=10, pady=5)

        # create tool bar frame
        tool_bar = tk.Frame(side_bar, width=200, height=400)
        tool_bar.grid(row=1, column=0, padx=5, pady=5)

        # create point select
        self.point_select = tk.Button(tool_bar, text='Point Select', command=self.draw_dot)
        self.point_select.grid(row=0, column=1)
        self.canvas.bind('<ButtonPress-1>', self.draw_dot)

        # file opening
        self.file_opening = tk.Button(tool_bar, text="Opening File", command=self.browse_file)
        self.file_opening.grid(row=0, column=2)
        self.canvas.bind('<ButtonPress-2>', self.browse_file)
        #
        # # save file
        self.save = tk.Button(tool_bar, text="Save File", command=self.save_image)
        self.save.grid(row=1, column=1)
        self.canvas.bind('<ButtonPress-3>', self.save_image)

    # file saving
    def save_image(self):
        save_path = filedialog.asksaveasfilename(defaultextension='.jpg')
        if save_path:
            self.image.save(save_path)
    # file opening
    def browse_file(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(title="Select an image file", filetypes=filetypes)
        if filepath:
            self.image = Image.open(filepath)
            photo = ImageTk.PhotoImage(self.image)
            w = 650
            h = 400
            self.canvas.image = photo
            self.canvas.config(width = w, height = h)
            self.canvas.create_image((0,0), image = photo, anchor = tk.NW)

    def quit(self):
        self.master.quit()

    def draw_dot(self, event):
        self.x1 = event.x
        self.y1 = event.y
        self.x2 = event.x
        self.y2 = event.y
        # Draw an oval in the given co-ordinates
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="black", width=2)

if __name__ == '__main__':
    root = tk.Tk()
    root.config(bg="SpringGreen4")
    app = App(root)
    root.mainloop()