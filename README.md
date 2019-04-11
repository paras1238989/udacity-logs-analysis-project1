# udacity-logs-analysis-project1
First Udacity project on logs analysis

Hello my name is Paras Agarkar and this project is the part of my Full Stack Nanodegree with Udacity.
Under the guidance of Omar Bellahsen

# About the project:

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

# Technology stack:
Python
PostgreSQL
Git
Vagrant

# Steps to run the program
1. Download and install Vagrant and VirtualBox.
2. Files for vagrant can be downloaded from https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip - This will help you install PostgreSQL, Python and other dependencies on the VM.
3. Start the Ubuntu Virtual Machine(VM) using : vagrant up
4. Connect to the Ubuntu VM using : vagrant ssh
5. Download data for the Database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
6. Extract the above data and import it in the database using : psql -d news -f newsdata.sql
7. Clone this git repository using : git clone https://github.com/paras1238989/udacity-logs-analysis-project1.git
8. Connect to news database using :psql news
9. Create a new view in the database using: 
                                            CREATE VIEW popularity_view AS (
					    SELECT title, author, count(*) as num 
					    FROM articles,log 
					    WHERE log.path=CONCAT('/article/',articles.slug) 
					    GROUP BY articles.title,articles.author 
					    ORDER BY num DESC
					    );
10. run the main.py file using : python main.py
11. The result similar to the output.txt will be displayed on the screen. 
