# Project Setup Instructions

Follow the steps below to set up and run the project on your local machine.

---

## Step 1: Install Dependencies

To install all required packages, use the following command:

```bash

pip install -r requirements.txt

```


Step 2: Set Up Database Migration
Initialize Alembic for database migration by running:

bash
Copy code
alembic init alembic
Step 3: Configure Database
In your .env file, configure the database connection by adding the following line:

bash
Copy code
DATABASE_URL=mysql+pymysql://root:Probing$7@localhost/mydb
Ensure the details (username, password, database name) match your MySQL setup.

Step 4: Initialize a New Git Repository (Optional)
If you want to start tracking your project with Git, initialize a new Git repository using:

bash
Copy code
git init
Database Migrations with Alembic
Creating New Migrations
Whenever you make changes to your database models, create a new migration file and apply the changes using the following commands:

bash
Copy code
alembic revision --autogenerate -m "Describe your changes"
alembic upgrade head
Downgrading Migrations
To downgrade a migration, use the following command (replace 55c70d0954c6_adding_new_changes with the target revision ID):

bash
Copy code
alembic downgrade 55c70d0954c6_adding_new_changes
Need Help?
Feel free to reach out if you have any questions or issues while setting up the project.




### Explanation:

1. **Headings**: 
   - `#` for a primary heading.
   - `##` for a secondary heading.
   - `###` for subheadings.

2. **Code blocks**: 
   - Use triple backticks (```` ``` ````) for multi-line code blocks.
   - You can specify the language (`bash`, `python`, etc.) to highlight syntax correctly.

3. **Horizontal rules**: 
   - Use three dashes (`---`) for horizontal rules to create separation between sections.

### Previewing the README:

- If you're working in a text editor like **VSCode**, it has a built-in Markdown preview that will display the formatting as it will appear on GitHub or any Markdown-supporting platform.
  
- **On GitHub**, when you upload the README file, you can view it from your repository's home page. GitHub will render the Markdown appropriately.

Ensure your file is saved with the `.md` extension (e.g., `README.md`) for Markdown to be interpreted correctly.

Let me know if you need more help with this!
