import helpers
from nlp_summarizer import summarize
import tkinter as tk
from tkinter import ttk
from webbrowser import open_new

"""Tkinter implementation for BriefNews."""


def onClick() -> None:
    url, title, full_text = helpers.randomArticle()

    full_summary = summarize(full_text)
    first_half = "      " + (" ".join(full_summary[0:3])) + "\n\n"
    full_text = first_half + ("     " + " ".join(full_summary[3:7]))

    article_label.config(text=title)
    text_label.config(text=full_text)


# get initial random article url, title, and text and assign to global vars
url, title, full_text = helpers.randomArticle()

# get summary for full text
full_summary = summarize(full_text)
first_half = "    " + (" ".join(full_summary[0:3])) + "\n\n"
full_text = first_half + ("         " + " ".join(full_summary[3:7]))

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
article_label = ttk.Label(root, text=title, font=("Georgia", 16), background="antique white", wraplength=400, anchor="center")
article_label.place(relx = 0.22, rely = 0.12)

# article url label
url_label = ttk.Label(root, text="Full Article", font=("Georgia", 12), background="antique white", foreground="blue", cursor="hand2")
url_label.bind("<Button-1>", lambda a: open_new(url))
url_label.place(relx = 0.43, rely = 0.28)

# article first half text label
text_label = ttk.Label(root, text= "       " + full_text, font=("Georgia", 10), background="antique white", wraplength=600)
text_label.place(relx = 0.08, rely = 0.35)

# next article button
next_button = tk.Button(root, text= "Next", font=("Georgia", 12), background="antique white", command= onClick)
next_button.place(relx= 0.45, rely = 0.95)
root.update()

root.mainloop()