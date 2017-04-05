from models import Manga
from models import ChapterInfo
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

def __call_api(url):
    response = requests.get(url,
      headers={
        "X-Mashape-Key": __X_MASHAPE_KEY,
        "Accept": "text/plain"
      }
    )

    return response


def get_manga(manga_id, source):
    url = __parse_url(manga_id, "", source)
    print("Calling the URL: " + url)
    response = __call_api(url)

    manga = Manga.from_json(response.json())
    manga.print_general_info()
    return manga

def get_chapter_info(manga_id, chapter, source):
    url = __parse_url(manga_id, chapter, source)
    print("Calling the URL: " + url)
    response = __call_api(url)

    chapterInfo = ChapterInfo.from_json(response.json())
    chapterInfo.print_general_info()
    return chapterInfo


def __parse_url(manga_id, chapter, source):
    url = __MANGA_BASE_URL.replace("{mangaid}", manga_id)
    url = url.replace("{siteid}", source)
    url = url.replace("{chapterid}", str(chapter))
    print("Parsing URL: ", url)
    return url
