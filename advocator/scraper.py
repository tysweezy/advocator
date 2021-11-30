from typing import List
from requests_html import HTMLSession
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# todos:
# - create list based on common terms. (ie python, algorithms)
# - loop through and and make request via duckduckgo or google.
# - store link/page in a datastore
# - curate content, filter and dont store duplicates.


def parse_properties(soup, items: List[str]) -> dict:
    """
    Grabs list of metadata properties and transforms data
    into a dictionary.

    TODO: add way to retrieve primative metadata such as name='description'
    NOTE: Not sure if I like soup being coupled and as a param in this method.
    """
    tags = dict()
    for i in items:
        prop = soup.find('meta', attrs={'property': i})

        if i is not None:
            tag = {i: prop['content']}
            tags.update(tag)
        else:
            print(f"meta tag {i} not found")
    return tags




def scrape_page(url):
    # scarpe meta tags, images, content
    with urllib.request.urlopen(url) as page:
        soup = BeautifulSoup(page.read().decode('utf-8'), 'html.parser')
        # content = soup.findAll('meta')
        # print(type(content))

        # site meta info
        """
        title = soup.find('meta', attrs={'name': 'title'})
        desc = soup.find('meta', attrs={'name': 'description'})

        print(f"title: {title['content']}")
        print(f"description: {desc['content']}")
        """

        social_props = parse_properties(soup, ['og:title', 'og:image', 'og:url'])
        print(f"social properties: {social_props}")


def yt_list(query, element=None):
    """
    Grabs list of relevant youtube vids
    from search results.
    """
    search_url = 'https://www.youtube.com/results?'
    video_list = []

    params = urllib.parse.urlencode({ 'search_query': query })
    url = search_url + "%s" % params

    session = HTMLSession()
    res = session.get(url)
    # becuase of js rendering :/
    # https://requests.readthedocs.io/projects/requests-html/en/latest/#javascript-support
    res.html.render()

    links = res.html.find('a#video-title')
    for l in links:
        video = list(l.links)[0]
        video_list.append(video)

    return video_list
