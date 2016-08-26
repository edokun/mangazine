# Utils module

API_BASE_URL = "https://doodle-manga-scraper.p.mashape.com"
API_KEY = "Mz7D0J6UuGmshhNukoJLus4IEzcIp1vc7DpjsnDxy25VptIsAi"
X_MASHAPE_KEY = "wrIpZCP7H2mshF7sHe18Vo7LfYQRp1pU0AajsnA0FHrI0zQlWk"

def get_manga_info(manga_id, site):
    url = API_BASE_URL + "/" + site + "/manga/" + manga_id
    print("Calling the URL: " + url)
    response = requests.get(url,
      headers={
        "X-Mashape-Key": X_MASHAPE_KEY,
        "Accept": "text/plain"
      }
    )
    # parsed_json = response.json()
    # print(parsed_json['info'])

    manga = Manga.from_json(response.json())
    return manga
