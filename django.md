pip install Django

## Creating a django project:
django-admin startproject ProjectName

## manage.py
- used to execute commands on the django project.

## settings.py
- configuration settings
- where we install an app into the project
    - add appName to `INSTALLED_APPS` list

## urls.py
- table of contents
- routs, urls we can visit

## Run the server
- python manage.py runserver

# A Django Project:
May consist of one or more Django applications.
Can have multiple apps that operate within it.

## A Django App:
python manage.py startapp appName

- use the project's settings file to install a app

### views.py
- what does a user see when they visit a particular route

## Template Inheritance
html page inherits from the layout page
same structure only need to write what differs between the pages

{% extends "appName/layout.html" %}

## Sessions
Django knows who you are and stores your session info

create all the default tables in django's database:
- python manage.py migrate


# Lecture 4 SQL, Models and Migrations

## SQL
The data has types: represent categories of information

**SQLite Types**:
- TEXT: A string
- NUMERIC: Number like data, date, bool, 
- INTEGER: -1, 0, 1
- REAL: 2.8
- BLOB: Binary Large Object

**Creating a Table**:

Table name and column names, with types, additional constraints.

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES
('New York', 'London', 415),
('Shanghai', 'Paris', 760),
('Istanbul', 'Tokyo', 700),
('New York', 'Paris', 435),
('Moscow', 'Paris', 245),
('Lima', 'New York', 455);

**Constraints:**

![SQLite Constraints](images/SQLite_constraints.png)

**Insert Data Into Table**:

INSERT INTO flights
    (origin, destination, duration)
    VALUES ('New York', 'London', 415);

- Add a new row to the flights table
- in parenthesis comma sep list for which we will provide values

**Select Data From Table**:

SELECT * FROM flights;
- select all

- SELECT origin, destination FROM flights;
- SELECT origin, destination FROM flights WHERE id = 3;
- SELECT * FROM flights WHERE origin = "New York";

**Create DB**:

touch flights.sql
New-Item flights.sql

sqlite3 flights.sql

view tables:
- .tables

INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Port Elizabeth', 60);  
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Joburg', 420);        
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Durban', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 350);
INSERT INTO flights (origin, destination, duration) VALUES ('Tokyo', 'Paris', 350);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 350);

**Organize The data better**:
`.mode columns`
`.headers yes`

select * from flights where origin = 'New York';
select * from flights where duration > 400;

select * from flights where duration > 400
    and destination = 'Joburg';

**Selecting all the duplicate occurrences that don't occur first, min(id)**
SELECT * FROM flights 
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM flights 
    GROUP BY origin, destination, duration
);

**Delete all the duplicate occurrences that don't occur first, min(id)**
DELETE FROM flights 
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM flights 
    GROUP BY origin, destination, duration
);

INSERT INTO flights (id, origin, destination, duration) VALUES (2, 'New York', 'Lima', 350);

**Select all flights where origin in 'New York' or 'Lima'**
select * from flights where origin in ('New York', 'Lima');

**Select Using a pattern**
- %: Any characters maybe zero maybe more
select * from flights where origin like '%a%';

**Functions**:
- average
- count
- max
- min
- sum

### Update, change data in the DB
**Update**: I would like to update a table

update flights
    set duration = 430
    where origin = 'Cape Town' and destination = 'Joburg';


### Delete data

Delete whole table:
DROP TABLE IF EXISTS flights;

delete from flights where destination = 'Lima'

### Other Clauses:
- limit
    - select * from flights limit 5;
- order by
```shell
sqlite> select * from flights order by origin;
id  origin     destination     duration
--  ---------  --------------  --------
3   Cape Town  Port Elizabeth  60
4   Cape Town  Joburg          430
5   Cape Town  Durban          130
7   Istanbul   Joburg          420
11  Lima       New York        350
9   Moscow     Paris           350
1   New York   London          415
8   New York   Durban          700
6   Shanghai   Port Elizabeth  60
10  Tokyo      Paris           350

sqlite> select * from flights order by duration;  
id  origin     destination     duration
--  ---------  --------------  --------
3   Cape Town  Port Elizabeth  60
6   Shanghai   Port Elizabeth  60
5   Cape Town  Durban          130
9   Moscow     Paris           350
10  Tokyo      Paris           350
11  Lima       New York        350
1   New York   London          415
7   Istanbul   Joburg          420
4   Cape Town  Joburg          430
8   New York   Durban          700
```

- group by
    - Group a bunch of flights together
    - having
        - **Constraint** you can place on group by
        - e.g. group by origin and having count >= 3, at least three flights from that city
```shell
sqlite> select * from flights group by origin;
id  origin     destination     duration
--  ---------  --------------  --------
3   Cape Town  Port Elizabeth  60      
7   Istanbul   Joburg          420     
11  Lima       New York        350     
9   Moscow     Paris           350     
1   New York   London          415     
6   Shanghai   Port Elizabeth  60
10  Tokyo      Paris           350

sqlite> select origin from flights group by origin having count(*) >= 2; 
origin   
---------
Cape Town
New York
```


## Foreign Keys
A reference to a key in another table.

The ability to relate tables to one another.

Connect two different tables together by way of a foreign key, they id of the airport in the airports table is used to represent the airport in the flights table where only the id is used to indicate the origin and destination.
- multiple airports in a city

- flights = one type of object
- airports = another type of object


CREATE TABLE airports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    city TEXT NOT NULL
);

INSERT INTO airports (code, city) VALUES
('JFK', 'New York'),
('PVG', 'Shanghai'),
('IST', 'Istanbul'),
('LHR', 'London'),
('SVO', 'Moscow'),
('LIM', 'Lima'),
('CDG', 'Paris'),
('NRT', 'Tokyo');

CREATE TABLE passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    flight_id INTEGER,
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);

INSERT INTO passengers (first, last, flight_id) VALUES
('Harry', 'Potter', 1),
('Ron', 'Weasley', 1),
('Hermione', 'Granger', 2),
('Draco', 'Malfoy', 4),
('Luna', 'Lovegood', 6),
('Ginny', 'Weasley', 6);

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);

INSERT INTO people (first, last) VALUES
('Harry', 'Potter'),
('Ron', 'Weasley'),
('Hermione', 'Granger'),
('Draco', 'Malfoy'),
('Luna', 'Lovegood'),
('Ginny', 'Weasley');

### Table relationships:
- Foreign Keys
- Many 2 one
- One to many
    - One flight is associated with many different passengers
- many 2 many
    - A flight has more than one passenger
    - some of those passengers are on multiple flights

- A table for people and then a separate table for mapping people to flights and flights to people.
    - passengers table: person_id and flight_id

Our tables:
- airports
    - any airport might appear on multiple different flights:
        - one2many
- flights
- people
- passengers
    - many2many mapping between people and flights
        - people can take multiple flights and each flight can consist of multiple people.

## Join
takes multiple tables and joins them together.

**Where every passenger is associated with one flight:

```shell
sqlite> select * from flights;
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       415
2   Shanghai  Paris        760
3   Istanbul  Tokyo        700
4   New York  Paris        435
5   Moscow    Paris        245
6   Lima      New York     455

sqlite> select * from passengers; 
id  first     last      flight_id
--  --------  --------  ---------
1   Harry     Potter    1
2   Ron       Weasley   1
3   Hermione  Granger   2
4   Draco     Malfoy    4
5   Luna      Lovegood  6
6   Ginny     Weasley   6

SELECT first, origin, destination
    FROM flights JOIN passengers
ON passengers.flight_id = flights.id;

first     origin    destination
--------  --------  -----------
Harry     New York  London
Ron       New York  London
Hermione  Shanghai  Paris
Draco     New York  Paris
Luna      Lima      New York
Ginny     Lima      New York
```

## JOINs
- JOIN / INNER JOIN
    - Take two tables, cross compare and only return where there is a match on both sides.
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN

## Optimizations we can make to make our queries more efficient:
- CREATE INDEX
    - makes querying on a particular column much more efficient
    - `CREATE INDEX` name_index ON passengers (last);
        - expect to be looking up passengers by their last name.

## SQL Injection
--

## Race Conditions
Multiple things happening in parallel threads simultaneously.
- conflicts on simultaneous queries and updates.
- Use a lock for the transaction.

# Django Models
A way of representing data inside of an

Create a new django project:
django-admin startproject airline

Create App:
python manage.py startapp flights

project -> settings.py
- add app to INSTALLED_APPS

project -> urls.py
- add path to urlpatterns

Before we create urls in airline\flights\urls.py:
- create some models
    - way of creating a python class which is going to represent data that we want django to store inside a DB.
    - every model is a python class representing each of the main tables we want to store information for.
- Make migrations to create the DB according to the models created

`python manage.py makemigrations`

apply migration:
`python manage.py migrate`

## Open django's shell:
- python manage.py shell
- Allows you to write python commands that get excuted on the web application.

**Insert Data Into application**
```shell
(venv) PS D:\Andre\webDevelopment\CS50\lecture_4_DBs\airline> python manage.py shell
In [1]: from flights.models import Flight
In [2]: f = Flight(origin="New York", destination="London", duration=415)
In [3]: f.save()

In [4]: flights = Flight.objects.all()
In [9]: flight = flights.first()
In [10]: flight
Out[10]: <Flight: 1: New York to London>
In [12]: flight.id, flight.origin, flight.destination, flight.duration
Out[12]: (1, 'New York', 'London', 415)

In [13]: flight.delete()
Out[13]: (1, {'flights.Flight': 1})

In [14]: Flight.objects.all()
Out[14]: <QuerySet []>
```
