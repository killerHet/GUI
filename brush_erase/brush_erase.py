#GUI Package for Python
import tkinter as tk

class Paint:
    def __init__(self, root):
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
        
        self.create_widgets()
        self.setup_bindings()

    #creates and places widgets for the GUI   
    def create_widgets(self):
        #creates a canvas widget with white background
        self.canvas = tk.Canvas(self.root, bg="white")
        #packs canvas widget into main window
        self.canvas.pack(fill=tk.BOTH, expand=True)
        #creates button widget
        self.brush_button = tk.Button(self.root, text="Brush", command=self.set_brush_tool)
        #packs button widget into main window
        self.brush_button.pack(side=tk.RIGHT)
        #creates eraser button
        self.eraser_button = tk.Button(self.root, text="Eraser", command=self.set_eraser_tool)
        #packs eraser button into main window
        self.eraser_button.pack(side=tk.RIGHT)
        #creates a Label widget with appropriate text and packs it into main window
        brush_size_label = tk.Label(self.root, text="Brush Size:")
        #label appears on the left side
        brush_size_label.pack(side=tk.LEFT)
        #creates horizontal scale widget with values ranging from 1 to 50
        self.brush_size_scale = tk.Scale(self.root, from_=1, to=50, orient=tk.HORIZONTAL, command=self.set_brush_size)
        #sets brush size to whatever the value in the scale is
        self.brush_size_scale.set(self.brush_size)
        self.brush_size_scale.pack(side=tk.LEFT)

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
        self.current_tool = "eraser"
        #changes the cursor for the canvas widget to a tcross icon
        self.canvas.config(cursor="tcross")

    #updates brush size with whatever the value in the scale is
    def set_brush_size(self, size):
        self.brush_size = int(size)

    #implements the drawing functionality for the brush and eraser tools, depending on the current tool selected by the user  
    def draw_brush(self, event):
        #checks if the current tool selected is the brush tool
        if self.current_tool == "brush":
            #gets the x and y coordinates of the mouse pointer from the event object
            x, y = event.x, event.y
            #calculates the top-left corner of the oval to be drawn based on the current mouse position and the size of the brush
            x1, y1 = (x - self.brush_size), (y - self.brush_size)
            #calculates the bottom-right corner of the oval to be drawn based on the current mouse position and the size of the brush
            x2, y2 = (x + self.brush_size), (y + self.brush_size)
            #creates an oval shape on the canvas with the calculated coordinates, fill color and outline color specified
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)
        #checks if the current tool selected is the eraser tool
        elif self.current_tool == "eraser":
            #gets the x and y coordinates of the mouse pointer from the event object
            x, y = event.x, event.y
            #calculates the top-left corner of the rectangle to be drawn based on the current mouse position and the size of the eraser
            x1, y1 = (x - self.eraser_size), (y - self.eraser_size)
            #calculates the bottom-right corner of the rectangle to be drawn based on the current mouse position and the size of the eraser
            x2, y2 = (x + self.eraser_size), (y + self.eraser_size)
            #creates a white rectangle shape on the canvas with the calculated coordinates, hence erasing anything drawn
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
            
    #called when the user releases the left mouse button after drawing on the canvas
    def reset(self, event):
        #ensures that there is a new brush stroke from the current mouse position
        self.previous_point = None

#represents the main window frame of a Tkinter GUI application     
root = tk.Tk()
#defines the behavior of the GUI application
paint = Paint(root)
# waits for user input and responds to it by calling the appropriate event handler functions
root.mainloop()