# Project Setup Instructions

Follow the steps below to set up and run the project on your local machine.

---

## Step 1: Install Dependencies

To install all required packages, use the following command:

```bash

pip install -r requirements.txt

```
---

## Step 2: Set Up Database Migration
Initialize Alembic for database migration by running:

```bash
alembic init alembic
```
---

## Step 3: Configure Database
In your .env file, configure the database connection by adding the following line:

```bash
DATABASE_URL=mysql+pymysql://root:Probing$7@localhost/mydb
```
Ensure the details (username, password, database name) match your MySQL setup.

---

## Step 4: Initialize a New Git Repository (Optional)
If you want to start tracking your project with Git, initialize a new Git repository using:

```
git init
Database Migrations with Alembic
```
---

# Creating New Migrations

Whenever you make changes to your database models, create a new migration file and apply the changes using the following commands:
```
alembic revision --autogenerate -m "Describe your changes"
alembic upgrade head
```
###Downgrading Migrations
To downgrade a migration, use the following command (replace 55c70d0954c6_adding_new_changes with the target revision ID):

```
alembic downgrade 55c70d0954c6_adding_new_changes
```

# Need Help?
Feel free to reach out if you have any questions or issues while setting up the project.


