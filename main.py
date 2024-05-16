import requests
from bs4 import BeautifulSoup

def main():
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

    # get an array of the content of each article
    wired_articles = wired_main_page.find_all("div", class_ = "SummaryItemContent-eiDYMl nLise summary-item__content")

    # iterate through and set title url parameters of each article
    for article in wired_articles:
        url_and_title = article.find("a", class_ = "SummaryItemHedLink-civMjp ejgyuy summary-item-tracking__hed-link summary-item__hed-link")
        url = url_and_title["href"]
        title = url_and_title.text

        print(f"{title}: {url}")

if __name__ == "__main__":
    main()