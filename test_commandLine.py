import requests
from bs4 import BeautifulSoup, ResultSet
from nlp_summarizer import summarize

# create global topics_list variable
topics_list: list[str] = ["tech", "space", "physics", "life", "humans", "earth"]

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

    # get raw webpage content
    article_content = requests.get(website_url)

    # check if html request was successful
    if article_content.status_code == 200:
        article_html = article_content.text
    else:
        raise Exception(f"failed to fetch content from {website_url}")

    # parse html and extract articles
    article_main_page = BeautifulSoup(article_html, "html.parser")

    # get a set of the content of each article
    article_list = article_main_page.find_all("h3", class_ = "post-item-river__title___vyz1w")
    return article_list

def test_commandLine() -> None:
    """Command line implementation for the summarize() and getArticles() functions"""
    # handle user input for article topic and get ResultSet
    choice: str = input("Please pick a news article topic from tech, space, physics, life, humans, or earth. ")
    article_list = getArticles(choice.lower())

    # iterate through and set title url parameters of each article
    for article in article_list:
        # from wired main page, get url and title of each article
        url_and_title = article.find("a")
        url = url_and_title["href"]
        title = url_and_title.text

        # get raw webpage content 
        article_content = requests.get(url)

        # check request status
        if article_content.status_code == 200:
            article_html = article_content.text
        else:
            raise Exception(f"Failed to fetch content from {url}")

        # parse article html and extract all text into one string
        article_page = BeautifulSoup(article_html, "html.parser")

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


        print(f"{title}: {url}")
        summary = summarize(full_text)
        print(f"{summary}")

if __name__ == "__main__":
    test_commandLine()