# Project Anemone

## Team

### Members

- Ivan Kostanjevec
  - School: VS
  - Short description: Ivan is a highly motivated software developer with 1.5 years of experience. He has a strong understanding of Java and React. Ivan is confident in his ability to contribute to the project and is looking forward to working with the team.
  - Skill levels:
    - Javascript
    - React.js
    - Java

- Enzo Jolidon
  - School: HEG Genève
  - Short description: Enzo JOLIDON is a highly motivated software developer with 1 and half years of experience in [related technology/field]. He has a strong understanding of data base structure, marketing, and code optimisation. Enzo is confident in his ability to contribute to the project and is looking forward to working with the team.
  - Skill levels:
    - Javascript
    - Python

- Fredy Rodriguez
  - School: Neuchâtel
  - Short description: Fredy is a highly motivated software developer with 1 year of experience in code and projects. He has a strong understanding of customer relation, reading code, and soft skills. Fredy is confident in his ability to contribute to the project and is looking forward to working with the team.
  - Skill levels:
    - JavaScript
    - Java

- Marvin Yohannes
  - School: Geneva
  - Short description: Marvin is a highly motivated software developer with 1 year of experience in code. He has a strong understanding of customer relation, reading code, and soft skills. Marvin is confident in his ability to contribute to the project and is looking forward to working with the team.
  - Skill levels:
    - Python

- Cindy Lopes Godinho (not in project anymore)
  - School: Haute école de Gestion de Genève (HEG)
  - Short description: Cindy is a highly motivated software developer with 1.5 of experience. She has a strong understanding of JavaScript and Python. Cindy is confident in her ability to contribute to the project and is looking forward to working with the team.
  - Skill levels:
    - Python => Good
    - Javascript => Not to bad
    - PHP => Not to bad
    - Pl/Sql => Basics
    - Java => Bad

### Professor Responsible
Christiane Jungius

### Means of Communication
- [Teams](https://teams.microsoft.com/l/team/19%3ajm4VyNKKk_l-duXbNetcjXE8cco0EGKKDD_oz2Pl5DQ1%40thread.tacv2/conversations?groupId=75ea3a7c-2843-4595-b17b-289de91de09e&tenantId=a372f724-c0b2-4ea0-abfb-0eb8c6f84e40) for general and quick discussions

## Mockups

We made four different screen [mockups](/misc/mockup.jpg), with some popups on the sides.

## Setup

### Prerequisites

- [Node.js](https://nodejs.org/en/)
- [Python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

### Installation

1. Install NPM packages
   ```shell
   npm install
   ```
   
2. Install Python packages
   ```shell
    pip install -r requirements.txt
    ```
   
3. Create the database
    ```shell
    python manage.py migrate
    ```
   
4. Load all fixtures in the correct order
    ```shell
    python manage.py loaddata data
    ```
   
5. Run the Django server
    ```shell
    python manage.py runserver
    ```

6. Run the node server
    ```shell
    npm run dev
    ```
