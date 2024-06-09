import helpers
from nlp_summarizer import summarize

def test_commandLine() -> None:
    """Command line implementation for the summarize() and getArticles() functions"""
    # handle user input for article topic and get ResultSet
    choice: str = input("Please pick a news article topic from tech, space, physics, life, humans, or earth. ")
    article_list = helpers.getArticles(choice.lower())

    # iterate through and set title url parameters of each article
    for article in article_list:
        # from wired main page, get url and title of each article
        url_and_title = article.find("a")
        url = url_and_title["href"]
        title = url_and_title.text

        # use getContent to get article html, handle exceptions, and convert to BeautifulSoup
        article_page = helpers.getContent(url)

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
        summary = " ".join(summarize(full_text))
        print(f"{summary}")

if __name__ == "__main__":
    test_commandLine()