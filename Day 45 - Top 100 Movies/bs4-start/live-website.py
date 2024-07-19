import requests
from bs4 import BeautifulSoup

# to check what is allowed to take: root + / robots.txt
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles_texts = []
articles_links = []

articles = soup.find_all(name="a", class_="storylink")
for article_tag in articles:
    # taking the title
    text = article_tag.getText()
    articles_texts.append(text)
    # taking the link
    link = article_tag.get("href")
    articles_links.append(link)

# taking the number
article_up = [int(score.getText().split(".")[0]) for score in soup.find_all(name="span", class_="rank")]

print(f"{article_up}\n{articles_texts}\n{articles_links}")

# the largest number
largest_number = max(article_up)
largest_index = article_up.index(largest_number)

largest_text = articles_texts[largest_index]
largest_link = articles_links[largest_index]

print(f"\nLargest Number:\n{largest_number}. {largest_text}\n{largest_link}")
