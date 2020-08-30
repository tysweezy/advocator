from requests_html import HTMLSession
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def scrape_page(url):
    # scarpe meta tags, images, content
    with urllib.request.urlopen(url) as page:
        soup = BeautifulSoup(page.read().decode('utf-8'), 'html.parser')
        content = soup.findAll('meta')
        for m in content:
            print('meta: ', m)


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