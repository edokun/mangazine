from models import Manga
import requests

__API_BASE_URL = "https://doodle-manga-scraper.p.mashape.com"
__MANGA_BASE_URL = __API_BASE_URL + "/{siteid}/manga/{mangaid}/{chapterid}"
__API_KEY = "Mz7D0J6UuGmshhNukoJLus4IEzcIp1vc7DpjsnDxy25VptIsAi"
__X_MASHAPE_KEY = "wrIpZCP7H2mshF7sHe18Vo7LfYQRp1pU0AajsnA0FHrI0zQlWk"

class Source:
    MANGAFOX = "mangafox.me"
    MANGASTREAM = "mangastream.com"
    MANGAREADER = "mangareader.net"

def get_manga_info(manga_id, source):
    url = parse_url(manga_id, "", source)
    #url = API_BASE_URL + "/" + source + "/manga/" + manga_id
    #print("Calling the URL: " + url)
    response = requests.get(url,
      headers={
        "X-Mashape-Key": __X_MASHAPE_KEY,
        "Accept": "text/plain"
      }
    )
    # parsed_json = response.json()
    # print(parsed_json['info'])

    manga = Manga.from_json(response.json())
    return manga

def parse_url(manga_id, chapter, source):
    url = __MANGA_BASE_URL.replace("{mangaid}", manga_id)
    url = url.replace("{siteid}", source)
    url = url.replace("{chapterid}", str(chapter))
    return url

def get_chapter_info(manga_id, chapter, source):
    url = parse_url(manga_id, chapter, source)
