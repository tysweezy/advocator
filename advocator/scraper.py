import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class YoutubeScrape:

    def __init__(self, query):
        self.query = query
        self.search_url = 'https://www.youtube.com/results?'
        self.videolist = []

    def _scrape_links(self):
        params = urllib.parse.urlencode({ 'search_query': self.query })
        url = self.search_url + "%s" % params

        with urllib.request.urlopen(url) as f:
            soup = BeautifulSoup(f.read().decode('utf-8'), 'html.parser')
            content = soup.findAll('a',{'class':'yt-uix-tile-link'})
            for c in content:
                if '/watch?v=' in c['href']:
                    video = 'https://www.youtube.com' + c['href']
                    self.videolist.append(video)

    def links(self):
        self._scrape_links()
        return self.videolist

# youtube scraper
# vimeo scraper
# webpage scraper

