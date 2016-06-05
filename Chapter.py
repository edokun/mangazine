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
