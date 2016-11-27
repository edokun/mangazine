#!/usr/bin/env python3
import utils
from utils import Source
#from models import Manga


def Main():
    manga = utils.get_manga_info("saint-oniisan", Source.MANGAFOX)
    #print('manga name: ', manga.name)
    #utils.parse_url("saint-oniisan", 1, Source.MANGAFOX)


if __name__ == '__main__':
    Main()
