# Logs Analysis Project


Logs Analysis Project, part of the Udacity
[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project purpose
To write SQL queries to answer the following questions about a PostgreSQL
database containing the logs of a fictional newspaper website.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Project contents
This project consists of the following files:

* `newsdata.py` - The Python program that connects to the PostgreSQL
  database, executes the SQL queries and displays the results.
* `README.md` - This read me file.
* `newsdata_output.txt` - This is plain text file that is a copy of what the program printed out.



## Prerequisites
The project code requires the following software:

* Python 2.7.12
* psycopg2 2.7.5
* PostgreSQL 9.5.14
* Vagrant
* VirtualBox
* [FSND Vagrant Configuration]( https://github.com/udacity/fullstack-nanodegree-vm)



## How to Run the Project

After installing [Virtual box](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html), clone this repository into the text-based interface of your operating system. (e.g. the terminal
window in Linux, the command prompt in Windows)
    ```
    git clone https://github.com/manlinar/logs-analysis
    ```

* Then go into the directory where the `Vagrantfile` is. 

    ```
    cd logs-analysis
    ```
* Bring up the VM with the following command:

    ```
    vagrant up
    ```

* Then: 

    ```
    vagrant ssh
    ```
* and after that:
    ```
    cd /vagrant
    ```

* Download the project zip file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to your computer and unzip the file.Put this file into the vagrant directory, which is shared with your virtual machine. Then run the following command to load the logs into the database:

  ```
    psql -d news -f newsdata.sql
  ```

* Running the reporting tool
The logs reporting tool is executed with the following command:

  ```
  python2 newsdata.py
  ```

* The answers to the three questions should now be displayed.

## Helpful Resources
1.Github Repository:[StevenWooding](https://github.com/SteveWooding/fsnd-logs-analysis-project)

2.Useful Site: [Stack Overflow](https://stackoverflow.com/)

3.Udacity Student's Forum: [Udacity Forum](https://study-hall.udacity.com/sg-617415-1968/rooms/community:nd004:en-us-general?contextType=room)