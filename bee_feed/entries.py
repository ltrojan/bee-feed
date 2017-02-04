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
            date=data[2],
            ori='Blog')

    @classmethod
    def from_rss(cls, data):
        if 'ori' not in data:
            data['ori'] = 'RSS Not Specified'
        return cls(
            title=data['title'],
            date=data['published'],
            text=data['summary'],
            ori=data['ori'])

    def __repr__(self):
        return " ".join([
            "Entry",
            self.title,
            self.date])


class Entries(list):

    @classmethod
    def from_db(cls, data):
        obj = cls(Entry.from_db(row) for row in data)
        obj.sort(key=lambda x: x.date)
        return obj

    @classmethod
    def from_rss(cls, data):
        obj = cls(Entry.from_rss(row) for row in data)
        obj.sort(key=lambda x: x.date)
        return obj

    def __add__(self, other):
        ret = self.__class__(list.__add__(self, other))
        # sort ret??
        return ret
