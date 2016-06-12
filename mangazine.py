#!/usr/bin/env python3

import argparse


def Main():
    # Top level parser
    parser = argparse.ArgumentParser(description='Mangazine an application \
        to download manga.')
    parser.add_argument('-p', '--provider',
                        nargs=1,
                        choices=['mangafox', 'mangastream', 'mangareader'],
                        metavar='provider',
                        help='Specifies provider to download manga from, \
                        by default is mangafox, possible options are \
                        mangafox, mangastream, mangareader',
                        default='mangafox')
    subparsers = parser.add_subparsers()

    # create the parser for the "a" command
    parser_a = subparsers.add_parser('download')
    parser_a.add_argument('mangaId', type=int)
    # create the parser for the "b" command
    parser_b = subparsers.add_parser('info')
    parser_b.add_argument('mangaId')

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    Main()
