from ui.home_ui import HomeUI
import tkinter as tk

class MainFrame():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TravelHUB")
        s_height = 1050
        s_width = 1920
        self.canvas = tk.Canvas(self.root, height=s_height,
                             width=s_width, bg="lightblue")
        
    def load_frame(self):
        self.canvas.pack()
        home_ui = HomeUI(self.root)
        home_ui.place_home_ui()
        self.root.mainloop()

