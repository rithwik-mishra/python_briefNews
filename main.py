import requests
from bs4 import BeautifulSoup
#from nlp_summarizer import summarize
from test_commandLine import getArticles, topics_list
import random
import tkinter as tk
from tkinter import ttk

def randomArticle() -> tuple:
    # use random.choice to choose a single article of random topic
    chosen_topic = random.choice(topics_list)
    article_list = getArticles(chosen_topic)
    chosen_article = random.choice(article_list)

    # find url and title for chosen article
    url_and_title = chosen_article.find("a")
    url = url_and_title["href"]
    title = url_and_title.text

    # get raw webpage content
    article_content = requests.get(url)

    #check request status


def main() -> None:
    """Tkinter implementation for BriefNews."""
    # initializing tkinter window
    root = tk.Tk()
    root.title("Python BriefNews")
    #root.configure(background="grey")
    root.geometry("700x700")
    root.resizable(False, False)

    # title label
    title_label = ttk.Label(root, text="BriefNews", font=("Arial", 30))
    title_label.place(relx = 0.5, rely = 0.05, anchor="n")



    root.mainloop()



if __name__ == "__main__":
    main()