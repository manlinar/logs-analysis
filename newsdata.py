#!/usr/bin/env python2
import psycopg2
DBNAME = 'news'
db = psycopg2.connect(database = DBNAME)
c = db.cursor()


query1 = """
            SELECT articles.title, count(*) as views
            FROM articles 
            JOIN log ON log.path = concat( '/article/', articles.slug)
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;
         """

c.execute(query1)
results = c.fetchall()

print ''
print 'The three most popular articles of all time are: '
print ''

for result in results:
	print '  {}  -  {} views'.format(result[0], result[1])
print ''

query2 = """
            SELECT authors.name, count(*) as views
            FROM ((articles 
            JOIN log ON log.path = concat( '/article/', articles.slug))
            JOIN authors ON articles.author = authors.id)
            GROUP BY authors.name
            ORDER BY views DESC;
    """

c.execute(query2)
results = c.fetchall()

print ''
print 'The most popular article authors of all time are: '
print ''

for result in results:
    print '  {}  -  {} views '.format(result[0], result[1])
print ''

#  table1 is a table that consists of 2 columns.The 1st is the column of the days and the 2nd is the column
#  of the number of all the requests that happened each day.

# table2 is a table that consinsts of  the column of days and the column 
# with the number of the requests with status '404 NOT FOUND' that happened each day.

# table3 is a table that consists of the column of the day and the column with 
# the percentage of the requests that led to an error each day.

query3 = """
                WITH table1 AS (
                SELECT date(log.time) AS day, count(*) AS number_of_requests
                FROM log
                GROUP BY day
                ORDER BY day
               )
                , table2 AS (
                SELECT  date(log.time) AS day, count(*) AS number_of_errors
                FROM log
                WHERE status != '200 OK'
                GROUP BY day
                ORDER BY day
               )
                , table3 AS (
                SELECT table1.day, 
                table2.number_of_errors::decimal * 100 / table1.number_of_requests
                AS error_percentage
                FROM table1 
                JOIN table2 ON table1.day = table2.day
              )
                SELECT * FROM table3 WHERE error_percentage > 1 ;
        """
c.execute(query3)
results = c.fetchall()

print ''
print 'The days that more than 1% of the requests led to errors are: '
print ''

for result in results:
	print '  {day: %B %e, %Y}  -  {table3:.3}% errors '.format(day=result[0], table3=result[1])
print ''

db.close()





