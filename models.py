class Chapter:

    chapter_id = 0
    name = ""

    def __init__(self, chapter_id=0, name=""):
        self.chapter_id = chapter_id
        self.name = name

    @staticmethod
    def from_json(json_object):
        chapter = Chapter()
        chapter.chapter_id = json_object['chapterId']
        chapter.name = json_object['name']
        return chapter

class Manga:

    # Attributes
    name = ""
    href = ""
    author = []
    artist = []
    status = ""
    genres = []
    info = ""
    cover_url = ""
    last_update = ""
    chapters = []

    def __init__(self, name="", href="", author=None, artist=None, status="",
                 genres=None, cover_url="", info="", last_update="",
                 chapters=None):
        self.name = name
        self.href = href
        self.info = info
        self.cover_url = cover_url
        self.last_update = last_update

        if author is None:
            self.author = []
        else:
            self.author = author

        if artist is None:
            self.artist = []
        else:
            self.artist = artist

        self.status = status

        if genres is None:
            self.genres = []
        else:
            self.genres = genres

        if chapters is None:
            self.chapters = []
        else:
            self.chapters = chapters

    @staticmethod
    def from_json(json_object):
        manga = Manga()
        manga.name = json_object['name']
        manga.href = json_object['href']
        manga.author = json_object['author']
        manga.artist = json_object['artist']
        manga.status = json_object['status']
        manga.genres = json_object['genres']
        manga.info = json_object['info']
        manga.cover_url = json_object['cover']
        manga.last_update = json_object['lastUpdate']
        manga.chapters = []

        for chapter in json_object['chapters']:
            chapterObject = Chapter.from_json(chapter)
            manga.chapters.append(chapterObject)

        return manga
