import requests
import random
from bs4 import BeautifulSoup, ResultSet

# create global topics_list variable
topics_list: list[str] = ["tech", "space", "physics", "life", "humans", "earth"]

def getContent(url: str) -> BeautifulSoup:
    """A function that returns the prettified html content of a given url while handling status getRequest status errors."""
    # get raw webpage content 
    article_content = requests.get(url)

    # check request status
    if article_content.status_code == 200:
        article_html = article_content.text
    else:
        raise Exception(f"Failed to fetch content from {url}")

    # parse article html and extract all text into one string
    article_page = BeautifulSoup(article_html, "html.parser")

    return article_page

def getArticles(topic: str) -> ResultSet:
    """A function that returns a ResultSet of all the articles from ScienceNews.org that match a given topic parameter."""
    # define variable to store sciencenews incomplete URL
    website_url = "https://www.sciencenews.org/topic/"

    # loop until user picks a valid topic
    while topic not in topics_list:
        print("Invalid topic.")
        topic = input("Please pick a news article topic from tech, space, physics, life, humans, or earth. ")
    
    # concatenate url with valid topic
    website_url += topic

    # parse html and extract articles
    article_main_page = getContent(website_url)

    # get a set of the content of each article
    article_list = article_main_page.find_all("h3", class_ = "post-item-river__title___vyz1w")
    return article_list

def randomArticle() -> tuple:
    """A function that returns a tuple of 3 strings: a url, title, and full_text string for a random article from the site."""
    # use random.choice to choose a single article of random topic
    chosen_topic = random.choice(topics_list)
    article_list = getArticles(chosen_topic)
    chosen_article = random.choice(article_list)

    # find url and title for chosen article
    url_and_title = chosen_article.find("a")
    url = url_and_title["href"]
    title = url_and_title.text

    article_page = getContent(url)

    # since articles on sciencenews.org have two different classes for article text,
    # use a try catch to handle any NoneType exceptions by trying both class definitions
    try:
        text_array = article_page.find("div", "rich-text single__rich-text___RmCDp").find_all("p")        
    except:
        text_array = article_page.find("div", "rich-text rich-text--with-sidebar single__rich-text___RmCDp").find_all("p")

    # iterate through text_array and concat into one string
    full_text = ""
    for text_p in text_array:
        full_text += text_p.text + " "
    
    return url, title, full_text