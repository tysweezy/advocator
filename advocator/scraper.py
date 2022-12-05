from typing import List
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def parse_properties(soup, items: List[str]) -> dict:
    """
    Grabs list of metadata properties and transforms data
    into a dictionary.

    TODO: add way to retrieve primative metadata such as name='description'
    NOTE: Not sure if I like soup being coupled and as a param in this method.
    """
    tags = dict()
    for i in items:
        prop = soup.find('meta', attrs={'property': i}) or soup.find(
            'meta', attrs={'name': i})

        if prop is not None:
            tag = {i: prop['content']}
            tags.update(tag)
        else:
            print(f"meta tag {i} not found")
    return tags


def scoop_meta(url):
    # scarpe meta tags, images, content
    with urllib.request.urlopen(url) as page:
        soup = BeautifulSoup(page.read().decode('utf-8'), 'html.parser')
        """
        title = soup.find('meta', attrs={'name': 'title'})
        desc = soup.find('meta', attrs={'name': 'description'})

        print(f"title: {title['content']}")
        print(f"description: {desc['content']}")
        """
        social_props = parse_properties(
            soup, ['og:title', 'og:image', 'og:url', 'title', 'description'])
        print(f"social properties: {social_props}")
