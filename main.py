import requests
from bs4 import BeautifulSoup
from nlp_summarizer import summarize

def getTechArticles():
    # define URL to crawl from
    tech_url = "https://www.sciencenews.org/topic/tech"

    # get raw webpage content
    tech_content = requests.get(tech_url)

    # check if html request was successful
    if tech_content.status_code == 200:
        tech_html = tech_content.text
    else:
        raise Exception(f"failed to fetch content from {tech_url}")

    # parse html and extract articles
    tech_main_page = BeautifulSoup(tech_html, "html.parser")

    # get a set of the content of each article
    tech_articles = tech_main_page.find_all("h3", class_ = "post-item-river__title___vyz1w")
    return tech_articles

def main():
    tech_articles = getTechArticles()
    # iterate through and set title url parameters of each article
    for article in tech_articles:
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
    main()