from advocater.scraper import YoutubeScrape

yt = YoutubeScrape("Golang Tutorials")
links = yt.links()

print(links)