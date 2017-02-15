clean_db_full = """
drop table if exists users;
drop table if exists entries;
"""

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


create_db_full = """
create table users (
  id integer primary key autoincrement,
  name text not null,
  password text not null,
  email text not null,
  admin bool,
  updates bool
);


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
