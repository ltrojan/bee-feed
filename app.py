import feedparser
from bee_feed.urls import URLS


def gen_feed(urls):
    for url in urls:
        yield feedparser.parse(url)


if __name__ == '__main__':
    print list(gen_feed(URLS))
