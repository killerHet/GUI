import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class FileOpening_and_Paint():
    def __init__(self, root = None):
        self.root = root
        #title of GUI window
        self.root.title("BRUSH AND ERASE TOOL")
        #size of GUI window
        self.root.geometry("800x600")
        #initial size of brush
        self.brush_size = 10
        #initial color of brush
        self.brush_color = "black"
        #initial size of eraser tool
        self.eraser_size = 10
        #initialize image variable
        self.image = 0
        #initialize a list which stores all events
        self.event_list = []
        self.last_x = None
        self.last_y = None
        #settung up canvas and bindings
        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        #creates a canvas widget with white background
        self.canvas = tk.Canvas(self.root, bg="white")
        #packs canvas widget into main window
        self.canvas.pack(fill=tk.BOTH, expand=True)
        #creates a button for the user to be able to choose a file to upload
        self.button = tk.Button(self.root, text="Choose file to upload", command=self.browse_file)
        self.button.pack(side="top")
        #creates brush button widget
        self.brush_button = tk.Button(self.root, text="Brush", command=self.set_brush_tool)
        #packs button widget into main window
        self.brush_button.pack(side="top")
        #creates undo button
        self.eraser_button = tk.Button(self.root, text="Undo", command=self.set_eraser_tool)
        #packs undo button into main window
        self.eraser_button.pack(side="top")
        #creates an erase all button and packs it into the canvas
        self.erase_all_button = tk.Button(self.root, text="Erase All", command=self.set_erase_all)
        self.erase_all_button.pack(side="top")
        #bar to set brush size
        brush_size_label = tk.Label(self.root, text="Brush Size:")
        #label appears on the left side
        brush_size_label.pack(side="top")
        #creates horizontal scale widget with values ranging from 1 to 50
        self.brush_size_scale = tk.Scale(self.root, from_=1, to=50, orient=tk.HORIZONTAL, command=self.set_brush_size)
        #sets brush size to whatever the value in the scale is
        self.brush_size_scale.set(self.brush_size)
        self.brush_size_scale.pack(side="top")
        

    def browse_file(self):
        #allowed file paths
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(title="Select an image file", filetypes=filetypes)
        if filepath:
            image = Image.open(filepath)
            image = image.convert("RGBA")
            self.image = ImageTk.PhotoImage(image)
            #opens image into the canvas
            self.canvas.create_image(0, 0, anchor="nw", image=self.image)
            self.event_list = []

    #sets up the event bindings for the canvas widget to enable drawing on the canvas with the brush tool    
    def setup_bindings(self):
        #binds the left mouse button motion event to the draw_brush method when the mouse is moved while the left mouse button is held down
        self.canvas.bind("<B1-Motion>", self.draw_brush)
        #binds the left mouse button release event to the reset method when the left mouse button is released
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    #sets the current tool to the brush tool    
    def set_brush_tool(self):
        #sets the instance variable current_tool to the string "brush", indicating that the brush tool is currently selected
        self.current_tool = "brush"
        #changes the cursor for the canvas widget to a pencil icon
        self.canvas.config(cursor="pencil")

    #sets the current tool to the eraser tool     
    def set_eraser_tool(self):
        #sets the instance variable current_tool to the string "eraser", indicating that the eraser tool is currently selected
        self.current_tool = "brush"
        if self.event_list:
            #undo the last brush stroke
            self.remove_latest_event()
        
    def set_erase_all(self):
        #erases everything on the campus and if there was an image, puts that back into the canvas
        if self.image != 0:
            self.canvas.create_image(0, 0, anchor="nw", image=self.image)
        else:
            self.canvas.delete("all")
        self.event_list = []
        self.current_tool = "brush"

    #updates brush size with whatever the value in the scale is
    def set_brush_size(self, size):
        self.brush_size = int(size)

    def remove_latest_event(self):
        #undoes last brush stroke
        if (len(self.event_list) > 5):
            self.event_list.pop()
            self.event_list.pop()
            self.event_list.pop()
            self.event_list.pop()
            self.event_list.pop()
        else:
            self.event_list.pop()
        self.canvas.delete("all")
        if self.image != 0:
            self.canvas.create_image(0, 0, anchor="nw", image=self.image)
        for i in self.event_list:
            self.canvas.create_oval(i[0], i[1], i[2], i[3], fill=i[4], outline=i[4])

    #implements the drawing functionality for the brush and eraser tools, depending on the current tool selected by the user  
    def draw_brush(self, event):
        #checks if the current tool selected is the brush tool
        if self.current_tool == "brush":
    #gets the x and y coordinates of the mouse pointer from the event object
            x, y = event.x, event.y
            x1, y1 = (x - self.brush_size), (y - self.brush_size)
            #calculates the bottom-right corner of the oval to be drawn based on the current mouse position and the size of the brush
            x2, y2 = (x + self.brush_size), (y + self.brush_size)
            #calculates the distance between the previous position and the current position
            if (self.last_x != None) and (self.last_y != None):
                distance = ((x - self.last_x) ** 2 + (y - self.last_y) ** 2) ** 0.5
                #calculates the step size and direction between the previous position and the current position
                step_x = (x - self.last_x) / distance if distance > 0 else 0
                step_y = (y - self.last_y) / distance if distance > 0 else 0
                #draw a sequence of small ovals between the previous position and the current position
                for i in range(int(distance)):
                    oval_x = int(self.last_x + i * step_x)
                    oval_y = int(self.last_y + i * step_y)
                    oval_x1, oval_y1 = (oval_x - self.brush_size), (oval_y - self.brush_size)
                    oval_x2, oval_y2 = (oval_x + self.brush_size), (oval_y + self.brush_size)
                    self.canvas.create_oval(oval_x1, oval_y1, oval_x2, oval_y2, fill=self.brush_color, outline=self.brush_color)
                    self.event_list.append((oval_x1, oval_y1, oval_x2, oval_y2, self.brush_color))
            else:
                self.canvas.create_oval(x1, y1,  x2, y2, fill=self.brush_color, outline=self.brush_color)
                self.event_list.append((x1, y1, x2, y2, self.brush_color))
            #update the previous position with the current position
            self.last_x, self.last_y = x, y
        #checks if the current tool selected is the eraser tool
        elif self.current_tool == "eraser":
            self.set_eraser_tool()
                       
    #called when the user releases the left mouse button after drawing on the canvas
    def reset(self, event):
        #ensures that there is a new brush stroke from the current mouse position
        self.last_x = None
        self.last_y = None


#represents the main window frame of a Tkinter GUI application     
root = tk.Tk()
#defines the behavior of the GUI application
paint = FileOpening_and_Paint(root)
# waits for user input and responds to it by calling the appropriate event handler functions
root.mainloop()