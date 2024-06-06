import helpers
from nlp_summarizer import summarize
import tkinter as tk
from tkinter import ttk
from webbrowser import open_new

"""Tkinter implementation for BriefNews."""


def onClick() -> None:
    url, title, full_text = helpers.randomArticle()
    summarized_text = summarize(full_text)
    article_label.config(text=title)
    url_label.config(text=url)
    text_label.config(text=summarized_text)


# get initial random article url, title, and text and assign to global vars
url, title, full_text = helpers.randomArticle()

# get summary for full text
summarized_text = summarize(full_text)

# initializing tkinter window
root = tk.Tk()
root.title("Python BriefNews")
root.configure(background="antique white")
root.geometry("700x760")
root.resizable(False, False)

# app title label
title_label = ttk.Label(root, text="BriefNews", font=("Algerian", 40), background="antique white")
title_label.place(relx = 0.5, rely = 0.05, anchor="n")

# article title label
article_label = ttk.Label(root, text=title, font=("Georgia", 16), background="antique white", wraplength=400)
article_label.place(relx = 0.22, rely = 0.12)

# article url label
url_label = ttk.Label(root, text=url, font=("Georgia", 12), background="antique white", foreground="blue", cursor="hand2", wraplength=400)
url_label.bind("<Button-1>", lambda a: open_new(url))
url_label.place(relx = 0.22, rely = 0.28)

# article text label
text_label = ttk.Label(root, text= summarized_text, font=("Georgia", 10), background="antique white", wraplength=600)
text_label.place(relx = 0.08, rely = 0.35)

# next article button
next_button = tk.Button(root, text= "Next", font=("Georgia", 12), background="antique white", command= onClick)
next_button.place(relx= 0.5, rely = 0.9)
root.update()

root.mainloop()