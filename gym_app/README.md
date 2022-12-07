### CodeClan Project - Gym App with Python/Flask

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-brief">Project Brief</a>
      <ul>
        <li><a href="#rules">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
<!--     <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

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


- Database with path to image (one-to-one)
- Gym can set custom definition of premium hours
- Membership type can be started and stopped

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
   git clone https://github.com/kelsiesmurphy/CC_Project_AdventureGrid.git
   ```
2. Navigate to the folder using terminal
3. Create the database
   ```sh
   psql -d experience_manager -f db/experience_manager.sql
   ```
4. Seed the database with pre-set data by running the console.py file
   ```sh
   python3 console.py
   ```
5. Run Flask
   ```sh
   flask run
   ```
6. Open in browser (Google Chrome is recommended): http://127.0.0.1:4999
7. To stop the server enter ctrl + c in your Terminal
