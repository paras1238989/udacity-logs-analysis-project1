#! /usr/bin/env python

# -*- coding: utf-8 -*-

# Paras Agarkar
# Udacity Project - 1 Log analysis


import psycopg2

DBNAME = "news"


def execute_query(query):
    ''' Makes a query to the news database '''
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


# What are the most popular three articles of all time?
query1 = ''' SELECT articles.title,count(*) AS count
FROM articles JOIN log
ON log.path LIKE concat('/article/%', articles.slug)
GROUP BY articles.title
ORDER BY count DESC
LIMIT 3; '''

# Who are the most popular article authors of all time?
query2 = ''' SELECT author.name, sum(view.num) AS views
FROM popularity_view AS view, authors AS author
WHERE author.id=view.author
GROUP BY author.name
ORDER BY views desc
LIMIT 3; '''

# On which days did more than 1% of requests lead to errors?
query3 = ''' SELECT *
FROM (
SELECT date(time),
round(100.0*sum(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 end)/
count(log.status),4) AS error
FROM log GROUP BY date(time)
ORDER BY error DESC) AS subq
WHERE error > 1; '''


def print_query1_result(query):
    results = execute_query(query)
    print('\n1. The 3 most popular articles of all time are:\n')
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def print_query2_result(query):
    results = execute_query(query)
    print('\n2. The most popular article authors of all time are:\n')
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def print_query3_result(query):
    results = execute_query(query)
    print('\n3. Days with more than 1% of request that lead to an error:\n')
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' %')


# print out results
print_query1_result(query1)
print_query2_result(query2)
print_query3_result(query3)
