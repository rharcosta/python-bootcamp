import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

title = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies = title[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in movies:
        file.write(f"{item}\n")
