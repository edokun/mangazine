from models import Manga
import requests
import bs4

__API_BASE_URL = "https://doodle-manga-scraper.p.mashape.com"
__MANGA_BASE_URL = __API_BASE_URL + "/{siteid}/manga/{mangaid}/{chapterid}"
__API_KEY = "Mz7D0J6UuGmshhNukoJLus4IEzcIp1vc7DpjsnDxy25VptIsAi"
__X_MASHAPE_KEY = "wrIpZCP7H2mshF7sHe18Vo7LfYQRp1pU0AajsnA0FHrI0zQlWk"

class Source:
    MANGAFOX = "mangafox.me"
    MANGASTREAM = "mangastream.com"
    MANGAREADER = "mangareader.net"

def get_manga(manga_id, source):
    url = parse_url(manga_id, "", source)
    print("Calling the URL: " + url)

    response = requests.get(url,
      headers={
        "X-Mashape-Key": __X_MASHAPE_KEY,
        "Accept": "text/plain"
      }
    )

    manga = Manga.from_json(response.json())
    manga.print_general_info()
    return manga

def get_chapter_info(manga_id, chapter, source):
    url = parse_url(manga_id, chapter, source)
    print("Calling the URL: " + url)

    response = requests.get(url,
      headers={
        "X-Mashape-Key": __X_MASHAPE_KEY,
        "Accept": "text/plain"
      }
    )

    print(response)

    #manga = Manga.from_json(response.json())


def parse_url(manga_id, chapter, source):
    url = __MANGA_BASE_URL.replace("{mangaid}", manga_id)
    url = url.replace("{siteid}", source)
    url = url.replace("{chapterid}", str(chapter))
    print("Parsing URL: ", url)
    return url


def test_scrapper():
    response = requests.get('http://es.mangahere.co/manga/saint_young_men/c1/')
    soup = bs4.BeautifulSoup(response.text, "lxml")
    #link = soup.select('#image').get('src')
    img_array = [img.attrs.get('src') for img in soup.select('#image')]
    print(img_array[0])
