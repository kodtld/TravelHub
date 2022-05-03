from hashlib import new
import tkinter as tk
import webbrowser

class FormatAttractions:
    def open_web(self,link):
        webbrowser.open(link,new=new)

    def form_att(self,root,name,dist,tags,wiki_link,i):
        one_box = tk.Label(root,bg="darkblue")
        x_val = i*0.3333
        one_box.place(relwidth=0.3333,relheight=0.6575,relx=x_val,rely=0.34)
        f_size = 14

        if len(name) > 25:
            f_size = 12

        if len(name) > 35:
            f_size = 10

        if len(name) > 45:
            f_size = 8

        name_and_place = tk.Label(one_box,
            text=f"{name}\n{dist} km from city center",
            bg="lightblue",font=("helvetica",f_size))

        name_and_place.place(relwidth=1,relheight=0.4,relx=0,rely=0)

        if len(tags) >0:
            location_tags = tk.Label(one_box,
            text=f"Tags:\n{tags[0][0]}\n{tags[0][1]}\n{tags[0][2]}",
            bg="lightblue",font=("helvetica",13))
            location_tags.place(relwidth=1,relheight=0.3,relx=0,rely=0.325)

        button_box = tk.Label(one_box,bg="lightblue")
        button_box.place(relwidth=1,relheight=0.3,relx=0,rely=0.675)

        button_text = "Location data"
        if wiki_link == "None":
            button_text = "No location data"

        wiki_button = tk.Button(button_box,text=button_text,
            bg="#7EDCFF",command=lambda:self.open_web(wiki_link),font="helvetica")

        wiki_button.place(relheight=1,relwidth=1,relx=0,rely=0)
