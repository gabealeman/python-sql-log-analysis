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

# 2. Who are the most popular article authors of all time?


def author_popularity():

    db, c = connect()
    query = """
     SELECT authors.name,
       sum(top.popularity) AS views
        FROM authors,
            (SELECT articles.author AS author_id,
         count(log.path) AS popularity
        FROM articles
        LEFT JOIN log ON log.path LIKE CONCAT('%', articles.slug, '%')
        WHERE log.status != '404 NOT FOUND'
        GROUP BY articles.author) AS top
        WHERE top.author_id = authors.id
        GROUP BY authors.name
        ORDER BY views DESC
    """
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("Who are the most popular article authors of all time?")
    for r in result:
            print("%s - %s views" % (r[0], r[1]))

author_popularity()

# 3. On which days did more than 1% of requests lead to errors?


def errors():
    db, c = connect()
    query = """
        SELECT *
        FROM
          (SELECT a.time::date,
            round(
            (count(a.status)::numeric * 100 / bit_or(b.total)::numeric), 1)
            AS yield
           FROM log AS a,
            (SELECT TIME::date,
              count(*) AS total
            FROM log
            GROUP BY TIME::date) AS b
           WHERE a.time::date = b.time::date
             AND a.status = '404 NOT FOUND'
           GROUP BY a.time::date) AS c
        WHERE c.yield > 1
    """
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("3. On which days did more than 1% of requests lead to errors?")
    for r in result:
        print("%s - %s%%" % (r[0], r[1]))

errors()
