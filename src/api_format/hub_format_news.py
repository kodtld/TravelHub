from hashlib import new
import tkinter as tk
import webbrowser

class FormatNews:
    def open_web(self,link):
        webbrowser.open(link,new=new)

    def form_news(self,root,title,source,link,i):
        y_val = (i+1)*0.2
        news_box = tk.Label(root, bg="darkblue")
        news_box_cont = tk.Label(news_box,bg="lightblue")
        news_box.place(relx=0,rely=y_val,relwidth=1,relheight=0.2)
        news_box_cont.place(relheight=1,relwidth=1,relx=0)


        if len(title) > 100:
            f_size = 8
        if len(title) > 80:
            f_size = 12
        else:
            f_size = 14

        one_box_title = tk.Label(news_box_cont,
         text=(title),bg="lightblue",
         font=("helvetica",f_size),justify=tk.LEFT)
        one_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)

        one_box_source = tk.Label(news_box_cont,
         text=f"Source: {source}",bg="lightblue",
         font=("helvetica",13),justify=tk.RIGHT)
        one_box_source.place(relwidth=1,relheight=0.3,relx=0,rely=0.3)

        one_box_link = link
        one_button = tk.Button(news_box_cont,text="Visit article",
         command= lambda: self.open_web(one_box_link),bg="#7EDCFF",
         font=("helvetica",13),activebackground="lightblue",justify=tk.CENTER)
        one_button.place(relheight=0.3,relwidth=0.2,relx=0.4,rely=0.6)
