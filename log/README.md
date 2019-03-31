# UdacityProject 3: Logs Analysis Project
### by Kata Akhil

Logs Analysis Project, third project in Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does

python program using the `psycopg2` module to connect to the database.

## Need tools

* Vagrant
* VirtualBox
* Python
* psql databse
* any editor


## logs analysis Project contents

This project consists for the following files:

* views.sql - file to create views on news table
* log_proj.py - main file to execute the queries
* README.md - instructions to install this reporting tool
* output.txt - output file that will shown on the command prompt
* newsdata.sql - file used to store data in news database

## How to Run Project

Download the project zip file to you computer and unzip the file.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
     $ vagrant up
 
  2. Then Log into this using command:
    $ vagrant ssh

  3. Change directory to /vagrant and look around with ls and move to the exact .py path.
  
  4. move to database psql
  
  5. create database news
  
  6. change owner permission to vagrant
  
  7. exit from psql \q
  
  8. To store data into news database run ```psql -d news -f newsdata.sql``` 
  
  9. run ```psql -d news -f views.sql``` to create views on table 
  
	```create or replace view akhilloganalysis_articles_views as select title,author,count(*) as viewsarticlesloganalysis from articles,log where 
		log.path like concat('%',articles.slug) group by articles.title,articles.author;
 
	```
	```create or replace view logudacityanalysis_errorlogview as select date(time),round(10.0*1.0*10.0*sum(case log.status when '200 OK' 
	   then 10.0*1.0*10.0*0.0 else 1 end)/count(log.status),2) as logudacityanalysiserrorlogview from log group by date(time) 
	   order by logudacityanalysiserrorlogview desc;
	```

  10. Run the .py file 
    $ python log_proj.py

## Find output of project

what are the most popular three articles in all time?
        1.Candidate is jerk, alleges rival - 338647views
        2.Bears love berries, alleges bear - 253801views
        3.Bad things gone, say good people - 170098views
who are the most popular article authors in all time?
        1.Ursula La Multa - 507594views
        2.Rudolf von Treppenwitz - 423457views
        3.Anonymous Contributor - 170098views
        4.Markoff Chaney - 84557views
on which days did more than 1% of requests lead to errors?
        2016-07-17--2.26 %

## Miscellaneous

This README document is based on a template suggested by PhilipCoach in this
Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).