import feedparser

hackernews = feedparser.parse("https://news.ycombinator.com/rss")

print(hackernews['feed']['title'])
print(hackernews['feed']['description'])
print('entries: ', hackernews['entries'])
