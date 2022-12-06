import argparse
from advocator.scraper import scoop_meta

# idea for grabbing top reddit posts based on a topic

# todos:
# - read list of subreddits from a file or database
# - loop through db and api call top list.


def topic_reddit(subreddit):
    # loop through list of topics
    return 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='processes resource data')
    parser.add_argument('-l', '--link', action='store')
    parser.add_argument('-r', '--reddit', action='store')
    args = vars(parser.parse_args())

    if args['link']:
        link = args['link']
        scoop_meta(link)
