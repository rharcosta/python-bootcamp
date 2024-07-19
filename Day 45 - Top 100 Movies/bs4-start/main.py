from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as webpage:
    content = webpage.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# all the anchor tags
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # the value in the anchor tags
    print(tag.getText())
    # the value of all links in the anchor tags
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# anchor inside the paragraph
company_url = soup.select_one(selector="p a")
print(company_url)
# id = name
name = soup.select_one(selector="#name")
print(name)

# class heading
headings = soup.select(".heading")
print(headings)
