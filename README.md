code challenge
Date, 2024/12/15 By God'swill Omuka

  1.Description
## Project Structure
- `app.py`: Main file to interact with the models.
- `/database`: Contains setup and database connection files.
- `/models`: Includes the core models (Author, Article, Magazine).
- `/tests`: Provides tests to ensure correct functionality.

## Models
- **Author**: Represents an author who writes articles. Each author can have multiple articles across various magazines.
- **Magazine**: Represents a magazine where articles are published. A magazine can have multiple authors.
- **Article**: Represents an article written by an author, and published in a magazine. Articles link authors and magazines.

## Core Features
- Create and retrieve authors, magazines, and articles.
- Query authors' articles and related magazines.
- Retrieve article titles and authors contributing to magazines.

  2.Getting Started
1. Clone this repository.
2. Run `pipenv install` to install dependencies.
3. Use `pipenv shell` to enter the virtual environment.
4. Run `python3 app.py` to test the database.


  -Installation Clone this repository to your local machine: git clone https://github.com/SamTomashi/Moringa-FT09-phase-3-code-challenge.git

  -Navigate into the project folder: Copy code cd 
Moringa-FT09-phase-3-code-challenge.git

  3.language used 
python

license The content of this site is licensed under the MIT license Copyright (c) 2024.