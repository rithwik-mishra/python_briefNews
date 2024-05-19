import requests
from bs4 import BeautifulSoup

def getWiredArticles():
    # define all URLs to crawl from
    wired_url = "https://www.wired.com/category/science/"

    # get raw webpage content
    wired_content = requests.get(wired_url)

    # check if html request was successful
    if wired_content.status_code == 200:
        wired_html = wired_content.text
    else:
        raise Exception(f"failed to fetch content from {wired_url}")

    # parse html and extract articles
    wired_main_page = BeautifulSoup(wired_html, "html.parser")

    # get a set of the content of each article
    wired_articles = wired_main_page.find_all("div", class_ = "SummaryItemContent-eiDYMl nLise summary-item__content")
    return wired_articles

def main():
    wired_articles = getWiredArticles()
    # iterate through and set title url parameters of each article
    for article in wired_articles:
        # from wired main page, get url and title of each article
        url_and_title = article.find("a", class_ = "SummaryItemHedLink-civMjp ejgyuy summary-item-tracking__hed-link summary-item__hed-link")
        url = "https://www.wired.com" + url_and_title["href"]
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
        text_array = article_page.find_all("p")
        full_text = ""
        for text_p in text_array:
            full_text += text_p.text


        print(f"{title}: {url}")
        print(f"{full_text}")

if __name__ == "__main__":
    main()