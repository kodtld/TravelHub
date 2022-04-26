from hashlib import new
import tkinter as tk
import webbrowser

class FormatNews:
    def __init__(self,root) -> None:
        self.root = root
        self.one_box = tk.Label(self.root, bg="darkblue")
        self.one_news_box = tk.Label(self.one_box,bg="lightblue")
        self.two_box = tk.Label(self.root, bg="darkblue")
        self.two_news_box = tk.Label(self.two_box,bg="lightblue")
        self.three_box = tk.Label(self.root, bg="darkblue")
        self.three_news_box = tk.Label(self.three_box,bg="lightblue")
        self.four_box = tk.Label(self.root, bg="darkblue")
        self.four_news_box = tk.Label(self.four_box,bg="lightblue")

    def open_web(self,link):
        webbrowser.open(link,new=new)

    def one_news(self,got_news):
        self.one_box.place(relx=0,rely=0.2,relwidth=1,relheight=0.2)
        self.one_news_box.place(relheight=1,relwidth=1,relx=0)

        if len(got_news['results'][0]['title']) > 100:
            one_box_title = tk.Label(self.one_news_box,
            text=(got_news['results'][0]['title']),bg="lightblue",
            font=("helvetica",12),justify=tk.LEFT)

        else:
            one_box_title = tk.Label(self.one_news_box,
            text=(got_news['results'][0]['title']),bg="lightblue",
            font=("helvetica",14),justify=tk.LEFT)

        one_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)

        one_box_source = tk.Label(self.one_news_box,
         text=f"Source: {got_news['results'][0]['source_id']}",bg="lightblue",
         font=("helvetica",13),justify=tk.RIGHT)
        one_box_source.place(relwidth=1,relheight=0.3,relx=0,rely=0.3)

        one_box_link = got_news['results'][0]['link']
        one_button = tk.Button(self.one_news_box,text="Visit article",
         command= lambda: self.open_web(one_box_link),bg="#7EDCFF",
         font=("helvetica",13),activebackground="lightblue",justify=tk.CENTER)
        one_button.place(relheight=0.3,relwidth=0.2,relx=0.4,rely=0.6)

    def two_news(self,got_news):
        self.two_box.place(relx=0,rely=0.4,relwidth=1,relheight=0.2)
        self.two_news_box.place(relheight=1,relwidth=1,relx=0)

        if len(got_news['results'][1]['title']) > 100:
            two_box_title = tk.Label(self.two_news_box,
            text=(got_news['results'][1]['title']),bg="lightblue",
            font=("helvetica",12),justify=tk.LEFT)

        else:
            two_box_title = tk.Label(self.two_news_box,
            text=(got_news['results'][1]['title']),bg="lightblue",
            font=("helvetica",14),justify=tk.LEFT)
        two_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)

        two_box_source = tk.Label(self.two_news_box,
         text=f"Source: {got_news['results'][1]['source_id']}",bg="lightblue",
         font=("helvetica",13),justify=tk.RIGHT)
        two_box_source.place(relwidth=1,relheight=0.3,relx=0,rely=0.3)

        two_box_link = got_news['results'][1]['link']
        two_button = tk.Button(self.two_news_box,text="Visit article",
         command= lambda: self.open_web(two_box_link),bg="#7EDCFF",
         font=("helvetica",13),activebackground="lightblue",justify=tk.CENTER)
        two_button.place(relheight=0.3,relwidth=0.2,relx=0.4,rely=0.6)

    def three_news(self,got_news):
        self.three_box.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)

        self.three_news_box.place(relheight=1,relwidth=1,relx=0)

        if len(got_news['results'][2]['title']) > 100:
            three_box_title = tk.Label(self.three_news_box,
            text=(got_news['results'][2]['title']),bg="lightblue",
            font=("helvetica",12),justify=tk.LEFT)

        else:
            three_box_title = tk.Label(self.three_news_box,
            text=(got_news['results'][2]['title']),bg="lightblue",
            font=("helvetica",14),justify=tk.LEFT)
        three_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)


        three_box_source = tk.Label(self.three_news_box,
         text=f"Source: {got_news['results'][2]['source_id']}",
         bg="lightblue",font=("helvetica",13),justify=tk.RIGHT)
        three_box_source.place(relwidth=1,relheight=0.3,relx=0,rely=0.3)

        three_box_link = got_news['results'][2]['link']
        three_button = tk.Button(self.three_news_box,text="Visit article",
         command= lambda: self.open_web(three_box_link),bg="#7EDCFF",
         font=("helvetica",13),activebackground="lightblue",justify=tk.CENTER)
        three_button.place(relheight=0.3,relwidth=0.2,relx=0.4,rely=0.6)

    def four_news(self,got_news):
        self.four_box.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)

        self.four_news_box.place(relheight=1,relwidth=1,relx=0)

        if len(got_news['results'][3]['title']) > 100:
            four_box_title = tk.Label(self.four_news_box,
            text=(got_news['results'][3]['title']),bg="lightblue",
            font=("helvetica",12),justify=tk.LEFT)

        else:
            four_box_title = tk.Label(self.four_news_box,
            text=(got_news['results'][3]['title']),bg="lightblue",
            font=("helvetica",14),justify=tk.LEFT)

        four_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)

        four_box_source = tk.Label(self.four_news_box,
         text=f"Source: {got_news['results'][3]['source_id']}",
        bg="lightblue",font=("helvetica",13),justify=tk.RIGHT)
        four_box_source.place(relwidth=1,relheight=0.3,relx=0,rely=0.3)

        four_box_link = got_news['results'][3]['link']
        four_button = tk.Button(self.four_news_box,text="Visit article",
         command= lambda: self.open_web(four_box_link),
         bg="#7EDCFF",font=("helvetica",13),
         activebackground="lightblue",justify=tk.CENTER)
        four_button.place(relheight=0.3,relwidth=0.2,relx=0.4,rely=0.6)

    def format_all(self,got_news):
        while True:
            try:
                self.one_news(got_news)
            except:
                one_box_title = tk.Label(self.one_news_box,
                 text="Couldn't find any news at the moment...",
                 font=("helvetica",14),justify=tk.LEFT,bg="lightblue")
                one_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
                break

            try:
                self.two_news(got_news)
            except:
                two_box_title = tk.Label(self.two_news_box,
                 text="Couldn't find any more news at the moment...",
                font=("helvetica",14),justify=tk.LEFT,bg="lightblue")
                two_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
                break

            try:
                self.three_news(got_news)
            except:
                three_box_title = tk.Label(self.three_news_box,
                 text="Couldn't find any more news at the moment...",
                 font=("helvetica",14),justify=tk.LEFT,bg="lightblue")
                three_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
                break

            try:
                self.four_news(got_news)
            except:
                four_box_title = tk.Label(self.four_news_box,
                 text="Couldn't find any more news at the moment...",
                 font=("helvetica",14),justify=tk.LEFT,bg="lightblue")
                four_box_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
                break
            break
