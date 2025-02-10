# Playstation Website Study
INSERT IMAGE
- Deployed project can be found [here](https://ey-up-me-pup-44c5def591d6.herokuapp.com/).

## User experience
### Purpose
- This website is designed to mimic playstations store page with a few improvements. Users can still do what they used to before however now the website has some more 'gamer' related features. 
- It is designed to make the user have a more clear picture of the games they are buying now including patch notes to see if a game is regularly updated, a more expansive review section that includes bug reports etc.
- The target audience of this website would be Playstation based gamers.

## Agile methodology DO THIS SECTION
- Agile methodology is "a set of methods and practices where solutions evolve through collaboration between self-organizing, cross-functional teams" ([reference](https://www.agilealliance.org/agile-essentials/)).
- A project board was set-up to keep track of user stories. Each user story was assigned a 'MoSCoW' prioritisation (must have, should have, could have, won't have) tag. The board can be found [here](https://github.com/users/elamont174/projects/5/views/1).

### User stories DO THIS SECTION

1. USER STORY
* SUCCESS CRITERIA
- 

## Design
### Wireframes DO THIS SECTION
INSERT WIREFRAMES

### Colour Scheme 
The colour scheme follows the same as the object of my study, Playstations own website. My aim for this project was to mimic the original website as much as possible hoping to focus on the tech side of the development process. 

### Typography
- Google fonts were used to source the font styles.
- Since the website is based off Playstations own I found a font similar to it and have used it throughout the website.
- ![Shantell Sans example font](static/images/shantell-sans.png)

## Images DO THIS SECTION
IMAGES

## Features
### Homepage
- The header is as close to the object of study's header and no new features have been added as of such.

- The homepage is where you'll find a new feature where you can see 'Coming Soon' games in a carousel section, the aim of this is to show users in a dated organised section what is coming soon to the Playstation store. Previously on the original website it is a section rather than a easy to read carousel. 

INSERT IMAGE

### Staff review page


### User review
- One of the main things I refined from the object of studies page is the review section, as this is made for gamers I thought it needed a few more key features that it didnt have before. ADD THE FEATURES

INSERT IMAGE

### Editing a user review DO THIS SECTION
- 

INSERT

### Deleting a user review DO THIS SECTION
- 

INSERT

### Registering DO THIS SECTION
- 

INSERT

### Logging in DO THIS SECTION
- 

INSERT

### Logging out DO THIS SECTION
- 

INSERT

### The admin panel DO THIS SECTION
- 

INSERT

### Footer DO THIS SECTION
- Following the original website im basing this project off 

## Database DO THIS SECTION
- I used Code Institute's PostgreSQL database?

### Database planning DO THIS SECTION
- I used an Entity Relationship Diagram to plan my database.
- ![ERD diagram](static/images/epr.png.png)

### Creating a database DO THIS SECTION
1. Navigate to [PostgreSQL](https://dbs.ci-dbs.net/) from Code Institute.
2. Enter your student email address in the input field provided.
3. Click Submit.
4. Wait while the database is created.
5. Check your email.
6. You now have a URL you can use to connect your app to your database.

## Deployment 
- The website was deployed to Heroku and can be found [here](https://ey-up-me-pup-44c5def591d6.herokuapp.com/).

### Heroku DO THIS SECTION
* Heroku is a cloud platform that lets developers create, deploy, monitor and manage apps.
- You will need a Heroku log-in to be able to deploy a website to Heroku.
- Once you have logged into Heroku:
1. Click 'New' > 'Create new app'
2. Choose a unique name, choose your region and press 'Create app'
3. Click on 'Settings' and then 'Reveal Config Vars'
4. Add a key of 'DISABLE_COLLECTSTATIC' with a value of '1'.
5. Add a key of 'DATABASE_URL' - the value will be the URL you were emailed when creating your database.
6. Add a key of 'SECRET_KEY' - the value will be any random secret key (google 'secret key generator' and use it to generate a random string of numbers, letters and characters)
7. In your terminal, type the code you will need to install project requirements:
- pip3 install gunicorn~=20.1
- pip3 install -r requirements.txt
- pip3 freeze --local > requirements.txt
8. Create an 'env.py' file at the root directory which contains the following:
    - import os
    - 
    - os.environ["DATABASE_URL"]='CI database URL'
    - os.environ["SECRET_KEY"]=" Your secret key"
8. Create a file at the root directory called Procfile. In this file enter: "web: gunicorn my_project.wsgi" (without the quotes)
9. In settings.py, set DEBUG to False. 
- YOU SHOULD ALWAYS SET DEBUG TO FALSE BEFORE DEPLOYING FOR SECURITY
10. Add ",'.herokuapp.com' " (without the double quotes) to the ALLOWED_HOSTS list in settings.py
11. Add, commit and push your code.
12. Go back to Heroku, click on the 'Deploy' tab.
13. Connect your project to GitHub.
14. Scroll to the bottom and click 'Deploy Branch' and your project will be deployed!

### Cloning
- To clone a GitHub repository:
1. On GitHub.com, navigate to the repository you want to clone.
2. Click the "Code" button (found above the list of files).
3. Copy the URL for the repository.
4. Open Git Bash or your chosen terminal.
5. Navigate to the directory where you want to clone the repository.
6. Type: git clone https://github.com/elamont174/ey-up-me-pup.git
7. Press Enter to create your local clone.

### Forking
- 'Forking' the GitHub repository means creating a copy which can be viewed/changed without changing the original.
- To fork a GitHub repository:
1. Login to GitHub and navigate to the repository you want to fork.
2. Click the "Fork" button (found above the Settings button).
3. You will now have a copy of the original repository in your GitHub account.

*Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Run the server: python3 manage.py runserver
- Stop the app once it's loaded: CTRL+C or ⌘+C
- Make any necessary migrations: python3 manage.py makemigrations
- Migrate the data to the database: python3 manage.py migrate
- Create a superuser: python3 manage.py createsuperuser

## Technologies used 
- HTML was used to structure the content of the website.
- CSS were used to design the layout of the website.
- Bootstrap was used as a CSS framework to provide a grid structure and improve responsiveness.
- Python and Django were used to build the backend review framework.
- GitHub was used to host the repository and version control.
- Heroku was the hosting platform.

## Testing
- Please see [TESTING.md](TESTING.md) file for all testing.

## Credits DO THIS SECTION
- 
