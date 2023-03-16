import tkinter

class ScrollableImage(tkinter.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super().__init__(master=master, **kw)
        self.cnvs = tkinter.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image((0, 0), anchor='nw', image=self.image)
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        # Vertical and Horizontal scrollbars
        self.v_scroll = tkinter.Scrollbar(self, orient='vertical')
        self.h_scroll = tkinter.Scrollbar(self, orient='horizontal')
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.configure(xscrollcommand=self.h_scroll.set, yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.configure(command=self.cnvs.yview)
        self.h_scroll.configure(command=self.cnvs.xview)
        #Assign the region to be scrolled
        self.cnvs.configure(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_all("<MouseWheel>", self.mouse_scroll)

        self.cnvs.focus_set()
        self.cnvs.bind("<1>", lambda event: self.cnvs.focus_set())
        self.cnvs.bind_all("<Left>", lambda event: self.cnvs.xview_scroll(-1, "units"))
        self.cnvs.bind_all("<Right>", lambda event: self.cnvs.xview_scroll(1, "units"))
        self.cnvs.bind_all("<Up>", lambda event: self.cnvs.yview_scroll(-1, "units"))
        self.cnvs.bind_all("<Down>", lambda event: self.cnvs.yview_scroll(1, "units"))

    def mouse_scroll(self, evt):
        if evt.state == 0:
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units') # For windows