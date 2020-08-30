from advocator.scraper import yt_list, scrape_page

links = yt_list("Python")
print(links)

if __name__ == '__main__':
    scrape_page('https://www.django-rest-framework.org/api-guide/authentication/')