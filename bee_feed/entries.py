from dateutil import parser
import time


class Entry(object):
    def __init__(self, title, date, text, ori=None):
        self.title = title
        self.date = date
        self.text = text
        self.ori = ori or "NotSpec"

    @classmethod
    def from_db(cls, data):
        return cls(
            title=data[0],
            text=data[1],
            date=parser.parse(data[2]),
            ori='Blog')

    @classmethod
    def from_rss(cls, data):
        if 'ori' not in data:
            data['ori'] = 'RSS Not Specified'
        return cls(
            title=data['title'],
            date=parser.parse(data['published']),
            text=data['summary'],
            ori=data['ori'])

    def __repr__(self):
        return " ".join([
            "Entry",
            self.title,
            str(self.date)])


class Entries(list):

    def __init__(self, *ar, **kw):
        list.__init__(self, *ar, **kw)
        self.sort()

    @classmethod
    def from_db(cls, data):
        return cls(Entry.from_db(row) for row in data)

    @classmethod
    def from_rss(cls, data):
        return cls(Entry.from_rss(row) for row in data)

    def sort(self, *ar, **kw):
        if 'key' not in kw:
            kw['key'] = lambda x: time.mktime(x.date.timetuple())
        if 'reverse' not in kw:
            kw['reverse'] = True
        list.sort(self, *ar, **kw)

    def __getslice__(self, *ar, **kw):
        return self.__class__(list.__getslice__(self, *ar, **kw))

    def __add__(self, other):
        ret = self.__class__(list.__add__(self, other))
        ret.sort(
            key=lambda x: time.mktime(x.date.timetuple()),
            reverse=True)
        return ret
