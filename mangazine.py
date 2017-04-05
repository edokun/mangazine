#!/usr/bin/env python3
import utils
import sys
from utils import Source
#from models import Manga

def _check_version():
    if (sys.version_info < (3, 0)):
        sys.stderr.write("You need python 3.0 or later to run this script\n")
        exit(1)
        #print 'WARNING: This program was designed to work with Python 3, program might not work correctly with current version.'


def Main():
    _check_version()
    #manga = utils.get_manga("saint-oniisan", Source.MANGAFOX)
    manga = utils.get_chapter_info("saint-oniisan", 1, Source.MANGAREADER)

if __name__ == '__main__':
    Main()
