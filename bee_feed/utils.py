import feedparser


def get_feed(url):
    return feedparser.parse(url)


def gen_feed(urls):
    for url in urls:
        yield get_feed(url)
