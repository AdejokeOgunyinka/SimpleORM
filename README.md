# Building a simple ORM

In this project, you will encounter and/or use the following
- SQLite Database & Working with sqlite3 module
- PostgreSQL Server & Working with psycopg2 module

## Convections / Coding Styles

- Ensure you appropriately name your functions, classes and modules using the expected naming convections
- Ensure to have exactly two(2) empty lines after your imports within modules for the sake of readability
- Ensure to be consistent with usage of string quotes. Lets stick with using single quotes except in situations where double quotes are required

## Project Description

In this project, we want to manage data presented in CSV format in the `data` folder, namely `authors.csv` & `books.csv`. These CSV files contains data about authors and the books they have written and published. Check them out to understand the kind of data you will be working with in this project.

Our objective here is to first have data in the CSV files transfer into a database and then perform operations (such as select, update, delete etc,) on the transfered data.

The implementations for this project goes in the `src` folder, and we have created the modules `authors.py` & `books.py` with each having a class defined, where the class have series of methods also defined and responsible for performing the required operations. You are expected to complete the implementations for these methods and ensure to conform to the TDD methodology as you do so.

Note the following when completing the implementation for `authors.py`
- You will be dealing with a PostgreSQL server here and interacting with it using `psycopg2` module
- Data will be read/written to a PostgreSQL database named `projectdb`
- Authors table that will be created in the database must be named `authors`

Note the following when completing the implementation for `books.py`
- You will be dealing with an SQLite database here and interacting with it using `sqlite3` module
- Data will be read/written to an SQLite database named `projectdb.sqlite`
- Books table that will be created in the database must be named `books`

We have also created the `main.py` module for you to showcase the different ways you would use your implementations. Note that the structure is entirely up to you, but ensure to play around with every aspect of your implementations within this module. Note that content of this module will also be reviewed as it will add to your total points

## Delivery Requirements

- Create a PR template of your choice into the `.github` folder to be used for PRs you will raise later
- Complete the expected implementations based on the project description and also write unit tests for all your implementations
- Do not push the following files and folders to Github by simply ignoring them in the `.gitignore` file - (`projectdb.sqlite`, `__pycache__`)
- When done and all tests are passing, raise a PR with a good title and body structured based on the content of the PR template you created at the beginning
