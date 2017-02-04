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
            date=data[1],
            text=data[2],
            ori='Local')

    @classmethod
    def from_rss(cls, ori, data):
        return cls(
            title=data['title'],
            date=data['published'],
            text=data['summary'],
            ori=ori)

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
    def from_rss(cls, ori, data):
        obj = cls(Entry.from_rss(ori, row) for row in data)
        obj.sort(key=lambda x: x.date)
        return obj
