# WORDEL
This is a Python-based word game, where the user has to guess the correct word, using clues from previous guesses. For the user to win. They must guess the correct word or words depending on the game mode.

[Link to deployed version.](https://ci-project3.herokuapp.com/)

# User Experience
The game is strictly teminal based, so all user interaction is through the terminal. It is hosted on Heroku that is a reliable host that allows for a wide range of languages used.

## Gameplay
Due to the limits of the terminal, I thought a simple word game like the newly popular wordle would be a great game to port to the terminal. Where the gameplay is functionally the same as it would be elsewhere. Leading to easy gameplay that anyone can do.

## Idea
I took heavy inspiration from the game Wordle created by Josh Wardle, that was very popular as of late. I have greatly enjoyed the game and think that is suitable for anyone to play. I really enjoy the inclusiveness of the game, allowing it to cross generations and bring people together.

To help streamline the development of the project I created a flowchart on [Lucid Chart](https://www.lucidchart.com/)

![Flow Chart](/assets/images/flowchart.png)

Once I had the outline of the project I started with the code for the project. I decided to go a step further than the original and add options to guess multiple words to add difficulty to the game. I wanted the game to be simple to use, but allow the more confident players to go for a greater challenge.


### Goal

1. Create a great text based game in python. That is easily played in the terminal.

2. For the game to be enjoyable for anyone who wants to pick it up.

3. For their to be a clear goal for the game that is easily understood but harder to accomplish.

4. Utlise the current popularity of word games to attract a large audience base.

### Target Audience
I want the game to be accesible to as many people as possible. For those who enjoy both hard and easy word based puzzles.

### User Stories

As a developer I want to...
- I want to create a simple game that is enoyable for all ages.
- I want the player to be engaged and have a clear sense of what to do.
- I want to give clear instructions for how to play.
- I want to create a game that can be played many times, with the help of other people or alone.
- I want them to feel a sense of accomplishment when they complete the game.


As a new user, I want to...
- To understand the game quickly.
- To be able to play the game.
- To have a clear goal for the game.
- To easily distuingish how to move forward in the game.
- A clear sense of what they are doing right or wrong.
- To be engaged and enjoy themselves.
- To be able to play again once the game is completed.
- To have a new word every game so it feels fresh and challenging every time.

As a returning user, I want to...
- To be able to choose different game modes.
- To feel a sense of growth and accomplishment from the game.
- To feel like the game is fresh and enjoyable every time they come back.

# Features

## Landing Page
There is only one page on the website. The terminal was designed by Code Institute.

- I created an intro using pyfiglet to engage the user:
    ![Welcome](/assets/images/welcome.png)

- The table the user uses as a refrence
    ![Wordle Table](/assets/images/wordletable.png)

- The win message
    ![Win message](/assets/images/win.png)

- The lose message.
    ![Lose message](/assets/images/lose.png)

- Clear Terminal
After every guess the terminal clears for a seamless experience.

# Technology Used

I have used several technologies to complete this website.
- [Python](https://www.python.org/):
    - Python is the core programming language used to write the project.
- [GitHub](https://github.com/dashboard):
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/):
    - Used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitPod](https://gitpod.io/workspaces):
    - Used as the development environment.
- [Heroku](https://heroku.com/):
    -Used to deploy my application.
- [Lucid Chart](https://www.lucidchart.com/):
    - Used to create my flow chart of the story.
- [Pep8](http://pep8online.com/):
    - Used to check my code against Pep8 requirements.
- [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet)
    - Used to add design to some aspects such as welcome intro, winner and loser messages
- [OS Clear](https://www.geeksforgeeks.org/clear-screen-python/)
    - Used to clear the terminal for cleaner viewing of print statements
- [Colored text](https://www.codegrepper.com/code-examples/python/python+colored+text+in+console)
    - Used to color the text for the guesses

# Testing

Once the application was complete it went through testing. I asked several people to try out the app, and do everything possible to break the app. I located several issues with the app thanks to this. Including some where the table would keep some of the previous games guesses, and the terminal clearing when it shouldn't.
Thanks to the testing I managed to make the game a lot more stable and enjoyable to use.

# Peer Review

Code Insitute Peer Review via Slack Channel


# Code Validation
I ran my code through [PEP8 Online Validator](http://pep8online.com/) and corrected many of the errors in my code.
- lines too long
- missing blanks
- changing comparison conditions
- wrong indentation
- trailing white spaces
![pep8 validator](/assets/images/testing.png)
The errors left are for the print statements in the instructions.


Unsolved Bugs:
- Each letter is taking as their own entity, so any letter that appears twice in your guess would come back correct, even if there is only one letter in the answer.

## Gitpod and GitHub

To use the terminal designed by The Code Institute I used the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).
This allows the code that is used to run the terminal to be viewed in the browser.

## Steps:

* Click create a new repository.
* Give the repository a name.
* Under Repository template pick the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).
* Click create repository
- Use GIT ADD.
- GIT COMMIT -m "Comments"
- GIT PUSH
- To commit the code and push to Github

## Forking the Github Repository

- Locate the desired Github repository.
- In the top right corner click the Fork button.
- The repository has been forked and you can now work 0on the copy.

## Cloning a Github repository

- Locate the desired Github repository.
- Use the code button and copy the link.
- Open Gitpod and select your directory where you want the clone to be created.
- Type git clone in the terminal and paste the link in.
- The clone will be created


## Creating an Application with Heroku

I used the video tutorial provided by The Code Institute to create a Heroku account, add the details of the app and deploy the application to a live environment.

- Log in to Heroku [Heroku](https://dashboard.heroku.com/)
- Click New 
- Give the app a name and choose the region
- Click on settings first and set the Reveal Config Vars
- PORT  = Key 8000 = Value
- If using CREDS please make sure this has been added to the requirements file.
- Add build pack include Python and Node.js
- The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
- Click Deploy at the top to go to the Deployment settings
- Choose GitHub as the deployment method
- Search for your app and connect
- Use Automatic deploys if you would like a new build when changes are pushed to GitHub from Gitpod
- Use Manual deploy for a new build every time this button is clicked.
- Once completed click View App.