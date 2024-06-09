# BriefNews: A python news summarizer
## Overview
Have you ever clicked on an interesting article just to feel discouraged by the 3 or more pages you have to read to understand it? This python project takes news articles from ScienceNews.org and uses a NLP summarizing technique to shorten the content into only 8 sentences, keeping it brief and easy to digest while still retaining the information. 

The project has two implementations: one using a command line interface that allows you to choose an article topic and gives you every article ScienceNews has featured on the topic on a given day and another that implements a Tkinter GUI that displays a random featured article from a random topic. 

The Requests library helped the program crawl for raw html content from a given url and handled any html error codes and extracting information from a website. Beautiful Soup allowed us to parse the html and prettify the article's html. To implement the word and sentence weighted frequency tokenizer algorithms. Finally, I used tkinter for the GUI implementation.

[Command line implementation](commandLine_img.jpg)

[Tkinter implementation](tkinter_img.jpg)

## Installation
1. Fork this repository
2. Use git clone to install it to your local machine
3. Install libraries in [requirements.txt](requirements.txt)
4. Run either [test_commandLine.py](test_commandLine.py) or [main.py](main.py)
