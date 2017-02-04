import itertools
import feedparser


class NamedURLs(dict):
    def add_named_url(self, name, url):
        self[name] = url


def get_feed(url):
    return feedparser.parse(url)


def gen_entries(named_urls):
    for ori, url in named_urls.iteritems():
        for ent in get_feed(url)['entries']:
            ent['ori'] = ori
            yield ent


def get_entries(named_urls, num=10):
    return itertools.islice(gen_entries(named_urls), 10)
