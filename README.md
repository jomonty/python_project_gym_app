# CodeClan Project - Gym App with Python/Flask

<br>

# Project Brief

### Gym

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

### MVP

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

### Inspired By

[Glofox](https://www.glofox.com/club-solution/), [Pike13](https://www.pike13.com/pike13-scheduling-software-demo)

### Possible Extensions

- Classes could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
- The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings. 


### Rules

The project must be built using only:

* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg2 library

It must **NOT** use:

* Any Object Relational Mapper (e.g. ActiveRecord)
* JavaScript. At all. Don't even think about it.
* Any pre-built CSS libraries, such as Bootstrap.
* Authentication. Assume that the user already has secure access to the app.

<br>

# Getting Started

### Prerequisites

To run this app, you must install: 
* psychopg
  ```sh
  pip3 install psycopg2
  ```

* Flask
  ```sh
  pip3 install Flask
  ```

* Postgresql



### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/jomonty/codeclan_python_project.git
   ```
2. Navigate to the folder using terminal
3. Create the database
   ```sh
   createdb gym_app
   ```
4. Create the database
   ```sh
   psql -d gym_app -f db/gym_app.sql
   ```
5. Seed the database with pre-set data by running the console.py file
   ```sh
   python3 console.py
   ```
6. Run Flask
   ```sh
   flask run
   ```
7. Open in browser: http://127.0.0.1:4999
8. To stop the server enter ctrl + c in your Terminal
