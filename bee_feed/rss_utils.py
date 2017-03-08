import itertools
import feedparser


class NamedURLs(dict):
    def add_named_url(self, name, url):
        self[name] = url


def get_feed(url):
    return feedparser.parse(url)


def gen_entries(named_urls):
    for ori, url in named_urls.items():
        for ent in get_feed(url)['entries']:
            ent['ori'] = ori
            yield ent


def get_entries(named_urls, num=None):
    gen = gen_entries(named_urls)
    if num is None:
        return list(gen)
    return itertools.islice(gen, num)
