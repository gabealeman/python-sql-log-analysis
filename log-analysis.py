#!/usr/bin/env python2.7
import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
        print("It worked")
    except:
        print("Error! Could not connect to database")

# 1. What are the most popular three articles of all time?

def most_popular():
    db, c = connect()
    query = """
               SELECT articles.title, count(log.path) as popularity
               FROM articles LEFT JOIN log
               ON log.path like CONCAT('%', articles.slug, '%')
               WHERE log.status != '404 NOT FOUND'
               GROUP BY articles.title
               ORDER BY popularity DESC
               LIMIT 3
           """
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("1. What are the most popular three articles of all time?")
    for r in result:
        print("%s - %s views" % (r[0], r[1]))

most_popular()