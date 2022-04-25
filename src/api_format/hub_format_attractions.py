from hashlib import new
import tkinter as tk
import webbrowser
class FormatAttractions:
    def __init__(self,root):
        self.root = root
        self.one_box = tk.Label(root,bg="darkblue")
        self.two_box = tk.Label(root,bg="darkblue")
        self.three_box = tk.Label(root,bg="darkblue")

    def open_web(self,link):
        webbrowser.open(link,new=new)

    def format_one(self,got_attractions):
        self.one_box.place(relwidth=0.33333,relheight=0.6575,relx=0,rely=0.34)
        name = got_attractions[0]['name']
        dist = got_attractions[0]['dist']
        dist = dist*0.001
        dist = "{:.1f}".format(dist)
        tags = [got_attractions[0]['kinds'].split(",")]
        try:
            wikidata = got_attractions[0]['wikidata']
        except:
            wikidata = "None"


        if len(name) > 25:
            name_and_place = tk.Label(self.one_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",12))
        
        elif len(name) > 35:
            name_and_place = tk.Label(self.one_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",10))
        
        else:
            name_and_place = tk.Label(self.one_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",14))
        
        name_and_place.place(relwidth=1,relheight=0.4,relx=0,rely=0)
        location_tags = tk.Label(self.one_box,text=f"Tags:\n{tags[0][0]}\n{tags[0][1]}\n{tags[0][2]}",bg="lightblue",font=("helvetica",13))
        location_tags.place(relwidth=1,relheight=0.3,relx=0,rely=0.325)
        button_box = tk.Label(self.one_box,bg="lightblue")
        button_box.place(relwidth=1,relheight=0.3,relx=0,rely=0.675)

        if wikidata != "None":
            wiki_link = f"https://www.wikidata.org/wiki/{wikidata}"
            wiki_button = tk.Button(button_box,text="Location Wiki",bg="#7EDCFF",command=lambda:self.open_web(wiki_link),font="helvetica")
        
        else:
            wiki_button = tk.Button(button_box,text="Couldn't find Wiki",bg="#7EDCFF",font="Helvetica")
            
        wiki_button.place(relheight=1,relwidth=1,relx=0,rely=0)

    def format_two(self,got_attractions):
        self.two_box.place(relwidth=0.33333,relheight=0.6575,relx=0.33333,rely=0.34)
        name = got_attractions[1]['name']
        dist = got_attractions[1]['dist']
        dist = dist*0.001
        dist = "{:.1f}".format(dist)
        tags = [got_attractions[1]['kinds'].split(",")]
        try:
            wikidata = got_attractions[1]['wikidata']
        except:
            wikidata = "None"
     
        if len(name) > 25:
            name_and_place = tk.Label(self.two_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",12))
        
        elif len(name) > 35:
            name_and_place = tk.Label(self.two_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",10))
        
        else:
            name_and_place = tk.Label(self.two_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",14))
        
        name_and_place.place(relwidth=1,relheight=0.4,relx=0,rely=0)
        location_tags = tk.Label(self.two_box,text=f"Tags:\n{tags[0][0]}\n{tags[0][1]}\n{tags[0][2]}",bg="lightblue",font=("helvetica",13))
        location_tags.place(relwidth=1,relheight=0.3,relx=0,rely=0.325)
        button_box = tk.Label(self.two_box,bg="lightblue")
        button_box.place(relwidth=1,relheight=0.3,relx=0,rely=0.675)

        if wikidata != "None":
            wiki_link = f"https://www.wikidata.org/wiki/{wikidata}"
            wiki_button = tk.Button(button_box,text="Location Wiki",bg="#7EDCFF",command=lambda:self.open_web(wiki_link),font="helvetica")
        
        else:
            wiki_button = tk.Button(button_box,text="Couldn't find Wiki",bg="#7EDCFF",font="Helvetica")
            
        wiki_button.place(relheight=1,relwidth=1,relx=0,rely=0)


    def format_three(self,got_attractions):
        self.three_box.place(relwidth=0.33333,relheight=0.6575,relx=0.66666,rely=0.34)
        name = got_attractions[2]['name']
        dist = got_attractions[2]['dist']
        dist = dist*0.001
        dist = "{:.1f}".format(dist)
        tags = [got_attractions[2]['kinds'].split(",")]
        try:
            wikidata = got_attractions[2]['wikidata']
        except:
            wikidata = "None"
      
        if len(name) > 25:
            name_and_place = tk.Label(self.three_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",12))
        
        elif len(name) > 35:
            name_and_place = tk.Label(self.three_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",10))
        
        else:
            name_and_place = tk.Label(self.three_box,text=f"{name}\n{dist} km from city center",bg="lightblue",font=("helvetica",14))
     
        name_and_place.place(relwidth=1,relheight=0.4,relx=0,rely=0)
        location_tags = tk.Label(self.three_box,text=f"Tags:\n{tags[0][0]}\n{tags[0][1]}\n{tags[0][2]}",bg="lightblue",font=("helvetica",13))
        location_tags.place(relwidth=1,relheight=0.3,relx=0,rely=0.325)

        button_box = tk.Label(self.three_box,bg="lightblue")
        button_box.place(relwidth=1,relheight=0.3,relx=0,rely=0.675)
        
        if wikidata != "None":
            wiki_link = f"https://www.wikidata.org/wiki/{wikidata}"
            wiki_button = tk.Button(button_box,text="Location Wiki",bg="#7EDCFF",command=lambda:self.open_web(wiki_link),font="helvetica")
        
        else:
            wiki_button = tk.Button(button_box,text="Couldn't find Wiki",bg="#7EDCFF",font="Helvetica")
            
        wiki_button.place(relheight=1,relwidth=1,relx=0,rely=0)

    def format_all(self,got_attractions):
        self.format_one(got_attractions)
        self.format_two(got_attractions)
        self.format_three(got_attractions)
