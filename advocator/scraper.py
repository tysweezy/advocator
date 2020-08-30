import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def scrape_page(url):
    # scarpe meta tags, images, content
    with urllib.request.urlopen(url) as page:
        soup = BeautifulSoup(page.read().decode('utf-8', 'html.parser'))
        content = soup.findAll('meta')
        for m in content:
            print('meta: ', m)


def yt_list(query, element=None):
    """
    Grabs list of relevant youtube vids. 

    TODO: Since I am only doing an initial search..
    might be better to use YT API in this case.
    """
    search_url = 'https://www.youtube.com/results?'
    video_list = []

    """
    element may change over time
    that's why we set a default
    element. In that event, we
    can set element when we
    instantiate the class
    """
    if element is not None:
        element = element
    else:
       element = 'yt-uix-tile-link'

    params = urllib.parse.urlencode({ 'search_query': query })
    url = search_url + "%s" % params

    with urllib.request.urlopen(url) as f:
        soup = BeautifulSoup(f.read().decode('utf-8'), 'html.parser', f)
        content = soup.findAll('a', {'class': element })
        print('content: ', content)
        for c in content:
            if '/watch?v=' in c['href']:
                video = 'https://www.youtube.com' + c['href']
                videolist.append(video)

    return video_list