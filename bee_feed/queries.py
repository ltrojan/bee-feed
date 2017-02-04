clean_db = """
drop table if exists entries;
"""


create_db = """
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null,
  created date
);
"""


get_entries = """
select title, text, created
from entries
order by created, id desc
limit 10
"""


add_entry = """
insert into entries (title, text, created) values (?, ?, ?)
"""
