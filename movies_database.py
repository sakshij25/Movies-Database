import sqlite3
connection = sqlite3.connect('movies.db')
print("Database opened successfully")

TABLE_NAME = "movies_table"
MOVIES_ID = "movies_id"
MOVIES_NAME = "movies_name"
MOVIES_DURATION = "movies_duration"
MOVIES_GENRE = "movies_genre"
MOVIES_REL_YEAR = "movies_year"
MOVIES_RATINGS = "movies_ratings"

connection.execute(" CREATE TABLE IF NOT EXISTS "
                   + TABLE_NAME
                   + " ( " + MOVIES_ID +
                   " INTEGER PRIMARY KEY " +
                   " AUTOINCREMENT, " +
                   MOVIES_NAME + " TEXT, " +
                   MOVIES_DURATION + " TEXT, " +
                   MOVIES_GENRE + " TEXT, " +
                   MOVIES_REL_YEAR + " INTEGER, " +
                   MOVIES_RATINGS +
                   " REAL); ")
print("table created successfully.")

def insert_record(name, duration, genre, release_year, ratings):
    connection.execute("INSERT INTO " + TABLE_NAME +
                       " (" + MOVIES_NAME + ", " +
                       MOVIES_DURATION + ", " +
                       MOVIES_GENRE + ", " +
                       MOVIES_REL_YEAR + ", " +
                       MOVIES_RATINGS +
                       ") VALUES(?,?,?,?,?);",
                       (name, duration, genre, release_year, ratings))
    connection.commit()

    print("Values inserted successfully.")

def retrieve_records():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
    return cursor