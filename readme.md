# TBC Library

<p>TBC Library, an app that generates books and authors in sqlite database.
</p>
<p>The repo has one main module, database manager, that is responsible for creation and population of tables with fake data and reading information from them</p>
<p>When we run script, already existed tables are being droped, recreated and repopulated.</p>
<p>Then after database manager fetches information from the databases about:</p>

<ul>
    <li>books that have most of the pages.</li>
    <li>the average num of pages that books have.</li>
    <li>youngest authors.</li>
    <li>authors whome doesnt have books.</li>
    <li>authors with more then five books.</li>
    <li>books written by several authors.</li>
</ul>

### Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

#

### Prerequisites

- <img src="readme/assets/python.png" width="25" style="position: relative; top: 8px" /> _Python @3.X and up_

- Faker: A Python package for generating fake data. Check Faker <a href="https://faker.readthedocs.io/en/stable/" target="_blank">documentation</a> for more details.

- _SQLAlchhemy @2.X and up_ The database toolkit for python and Object Relational Mapper

- other libraries such as random, datetime and json generally are included with Python.

#

### Getting Started

1\. First of all you need to clone TBC-library repository from github:

```sh
git clone https://github.com/NikaKhiz/tbc-library.git
```

2\. your operating system may be using different versions of python interpreter , so first check it using next command:

```sh
python --version
```

or

```sh
python3 --version
```

3\. Generally its a good practice to work in virtual environment to avoid comflicts.

<p>to create virtual environment and activate it, run the following commands in a root directory: </p>

```sh
python -m venv venv
source venv/bin/activate
```

or

```sh
python3 -m venv venv
source venv/bin/activate
```

<p>these commands will create and activate virtual environment named venv</p>

<p>if you want to deactivate virtual environment, simply run the following command in terminal:</p>

```sh
deactivate
```

4\. Then after you will need to install all of the dependencies provided in requirements.txt file:

<p>for that run the following commands in a root directory from your terminal:</p>

```sh
pip install -r requirements.txt
```

5\. After that in the root directory, you can run command from the terminal:

```sh
python main.py
```

or

```sh
python3 main.py
```

### this command runs the script, populates db, and display the results in terminal!

### Project Structure

```bash
├─── readme
│   ├─── assets
- .gitignore
- books.db
- database_manager.py
- library.db
- main.py
- models.py
- readme.md
- requirements.txt
- utils.py
```
