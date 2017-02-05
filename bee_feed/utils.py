from . import sql_utils
from . import rss_utils
from . import entries


def get_entries(db=None, named_urls=None):
    sql_ents = entries.Entries([])
    rss_ents = entries.Entries([])
    if db is not None:
        sql_ents = entries.Entries.from_db(
            sql_utils.get_entries(db))
    if named_urls is not None:
        rss_ents = entries.Entries.from_rss(
            rss_utils.get_entries(named_urls))
    ents = sql_ents + rss_ents
    # sort ents???
    return ents[:10]
