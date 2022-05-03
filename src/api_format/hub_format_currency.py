import tkinter as tk
class FormatCurrency:
    def __init__(self,root):
        from logic.hub_logic import HubLogic
        self.hub_logic = HubLogic()
        self.amount2= 0
        self.currency_bg = tk.Label(root,bg="lightblue")
        self.currency_text = tk.Label(root,bg="lightblue")
        self.ratesum_text = tk.Label(root,bg="lightblue")
        self.currency_scale = tk.Scale(self.currency_bg, bg="#7EDCFF",
         from_=0,to=500,tickinterval=50,length=500,orient="horizontal",command=self.get_val)
        self.scale_text = tk.Label(self.currency_scale,bg="#7EDCFF",
         text="Try a different amount!",font=("helvetica",15))

    def get_val(self,val):
        self.amount2 = int(val)

    def format_all(self,country,currency_name,amount,ratesum,currency_code):

        self.currency_bg.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.currency_text.place(relx=0,rely=0,relheight=0.25,relwidth=1)
        self.ratesum_text.place(relx=0,rely=0.2,relheight=0.2,relwidth=1)
        self.currency_scale.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
        self.scale_text.place(relx=0.0125,rely=0.6,relheight=0.3,relwidth=0.3)

        info_text = tk.Label(self.currency_text,bg="lightblue",
         text=f"The official currency of {country} is: {currency_name}",font=("helvetica",18))
        info_text.place(relheight=1,relwidth=1,relx=0,rely=0)

        ratesum = f"{ratesum:.2f}"
        ratesum_text = tk.Label(self.ratesum_text,bg="lightblue",
         text=f"For {amount} Euro's, you'll get {ratesum} {currency_name}'s",font=("helvetica",18))
        ratesum_text.place(relheight=1,relwidth=1,relx=0,rely=0)

        currency_button = tk.Button(self.currency_scale,bg="darkblue",
         text="Exchange",font=("helvetica",15),fg="white",
         command=lambda:self.hub_logic.get_currency(self.amount2,
         country,currency_name,currency_code))
        currency_button.place(relx=0.65,rely=0.6,relheight=0.3,relwidth=0.3)
