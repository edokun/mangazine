#!/usr/bin/env python3
import utils
from utils import Source
#from models import Manga


def Main():
    #manga = utils.get_manga("saint-oniisan", Source.MANGAFOX)
    #manga = utils.get_chapter_info("saint-oniisan", 1, Source.MANGASTREAM)
    utils.test_scrapper()

if __name__ == '__main__':
    Main()
