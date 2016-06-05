#!/usr/bin/env python3


import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")

'''
Posible options:
download <mangaId>
if no chapter parameter provided will download first chatper only
-c --chapters <chapter>
    (divided by , or range using [n-n], or single number, or word first, last)
-d --download-directory <location>
(the structure will be manga_name/chapter_number using 3 digits/3 digits file name.jpg)
-p --provider <provider> will specify source to download manga from, if not specified
will use any

list-providers

'''
