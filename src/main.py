from tkinter import *

root = Tk()
root.title("TravelHUB")
S_Height = 800
S_Width =  1100
canvas = Canvas(root, height = S_Height, width = S_Width)
canvas.pack()

# Set Home Screen Background Image
bgimage = PhotoImage(file = "BGimagesmarrel.png")
bg_label = Label(root,image = bgimage)
bg_label.place(x=0,y=0,relwidth=1, relheight=1)

# Home Screen Entry Box
hp = Entry(root,bg="white",font="helvetica",justify=CENTER)
hp.insert(END,"Type in your destination...")
hp.place(relx = 0.3, rely = 0.5, relwidth = 0.4, relheight = 0.1)

# Home Screen Button
take_button = Button(root, bg="#00BAFF", activebackground="#7EDCFF", text= "Take me there!", font="helvetica", fg="white", activeforeground="white")
take_button.place(relx = 0.3, rely = 0.63, relwidth = 0.4, relheight = 0.1)

# Main frame
main_frame = Frame(root)
#main_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

root.mainloop()
