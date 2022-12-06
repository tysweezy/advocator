import argparse
from advocator.scraper import scoop_meta

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='processes resource data')
    parser.add_argument('-l', '--link', action='store')
    parser.add_argument('-r', '--reddit', action='store')
    args = vars(parser.parse_args())

    if args['link']:
        link = args['link']
        scoop_meta(link)
