song_play_table = "songplays"
users_table = "users"
songs_table = "songs"
artist_table = "artists"
time_table = "time"


# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS "+ song_play_table
user_table_drop = "DROP TABLE IF EXISTS " + users_table
song_table_drop = "DROP TABLE IF EXISTS " + songs_table
artist_table_drop = "DROP TABLE IF EXISTS " + artist_table
time_table_drop = "DROP TABLE IF EXISTS "+ time_table

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS """+song_play_table+""" (ID  VARCHAR PRIMARY KEY, start_time int, user_id varchar, level int, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar) 
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS """+users_table+""" (ID  VARCHAR PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar) 
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS """+songs_table+""" (ID  VARCHAR PRIMARY KEY, title varchar, artist_id VARCHAR, year int, duration int) 
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS """+artist_table +""" (ID  VARCHAR PRIMARY KEY, name varchar, location varchar, latitude int, longitude int) 

""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS """+time_table+""" (ID  SERIAL PRIMARY KEY, start_time date, hour int, day int, week int, month int, year int, weekday int) 
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO """+ song_play_table +""" (ID, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s,%s, %s, %s,%s, %s)
""")

user_table_insert = ("""
INSERT INTO """+ users_table +""" (ID, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s,%s)
""")

song_table_insert = ("""
INSERT INTO """+ songs_table +""" (ID, title, artist_id, year, duration) VALUES (%s, %s, %s, %s,%s)
""")

artist_table_insert = ("""
INSERT INTO """+ artist_table +""" (ID, name, location, latitude, longitude) VALUES (%s, %s, %s, %s,%s)

""")


time_table_insert = ("""
INSERT INTO """+ time_table +""" (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s,%s,%s, %s)

""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
