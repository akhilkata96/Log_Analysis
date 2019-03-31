#!/usr/bin/env python
import psycopg2
from datetime import datetime

# database
databasename = "news"
# connecting to database


def connection(databasename="news"):
    try:
        con = psycopg2.connect("dbname={}".format(databasename))
        cur = con.cursor()
        return con, cur
    except:
        print("No database found")


#  what are the most three popular articles of all time
top3_Articles = ("""select title,viewsarticlesloganalysis
        from akhilloganalysis_articles_views
        order by viewsarticlesloganalysis desc limit 3""")
# who are the most four popular article authors in all time
top4_Authors = ("""select authors.name,sum
    (akhilloganalysis_articles_views.viewsarticlesloganalysis) as
    viewsarticlesloganalysis from akhilloganalysis_articles_views,authors where
    authors.id = akhilloganalysis_articles_views.author
    group by authors.name order by viewsarticlesloganalysis desc;""")


# on which days did more than 1% of requests lead to errors
day_Errors = ("""select * from logudacityanalysis_errorlogview
        where 1.0 < logudacityanalysiserrorlogview;""")


# All Sql queries execution part
def sql_execution(query):
    con, cur = connection()
    cur.execute(query)
    return cur.fetchall()
    con.close()


def quer1_results(query_1):
    '''top most 3 articles print'''
    try:
        for tit, na in enumerate(query_1):
            print("\t" + str(tit+1) + "." + str(na[0]) + " - "+str(na[1]) +
                  " views")
    except Exception as error:
        print(error)


def quer2_results(query_2):
    '''top most 4 authors print'''
    try:
        for auth, nam in enumerate(query_2):
            print("\t" + str(auth+1) + "." + str(nam[0]) + "-" + str(nam[1]) +
                  " views")
    except Exception as error:
        print(error)


def quer3_errors(query_3):
    '''errors find in a day and date'''
    try:
        for res in query_3:
            date = res[0]
            date_error = res[1]
            print("        {}--{} %".format(date, date_error))
    except Exception as error:
        print(error)


if __name__ == '__main__':
    print(" (i).what are the most popular three articles in all time?")
    top3articles = sql_execution(top3_Articles)
    quer1_results(top3articles)
    print("\n")
    print(" (ii).who are the most popular article authors in all time?")
    top4authors = sql_execution(top4_Authors)
    quer2_results(top4authors)
    print("\n")
    print(" (iii).on which days did more than 1% of requests lead to errors?")
    errordays = sql_execution(day_Errors)
    quer3_errors(errordays)
    print("\n")
