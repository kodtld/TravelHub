import tkinter as tk
class FormatCurrency:
    def __init__(self,root):
        from logic.hub_logic import HubLogic
        self.hub_logic = HubLogic()
        self.amount2= 0
        self.currency_text = tk.Label(root,bg="lightblue")
        self.ratesum_text = tk.Label(root,bg="lightblue")

    def format_all(self,country,currency_name,amount,ratesum):

        self.currency_text.place(relx=0,rely=0,relheight=0.25,relwidth=1)
        self.ratesum_text.place(relx=0,rely=0.2,relheight=0.2,relwidth=1)

        info_text = tk.Label(self.currency_text,bg="lightblue",
         text=f"The official currency of {country} is: {currency_name}",font=("helvetica",18))
        info_text.place(relheight=1,relwidth=1,relx=0,rely=0)

        ratesum = f"{ratesum:.2f}"
        ratesum_text = tk.Label(self.ratesum_text,bg="lightblue",
         text=f"For {amount} Euro's, you'll get {ratesum} {currency_name}'s",font=("helvetica",18))
        ratesum_text.place(relheight=1,relwidth=1,relx=0,rely=0)
