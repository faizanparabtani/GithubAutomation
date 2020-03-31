# GithubAutomation
Making the whole process of initialize tracking project with git, creating and connecting with a Github repository online with just one button click!
This is a simple 2 script program which automates the stage of project starting.

# What does it do?
1) Performs git init on the repository specified.
2) Logins for you automatically to Github.
3) Creates a new Repository, name matching with local repository name.
4) Connects local repository to the Github Repository so youre able to collaborate in just 10 seconds!

# Setup
Make sure you have the dependencies in place
There are a couple of things to be added in the 2 scripts

## Shell Script
Add your Github Username where specified.

## Python Script
Add ChromeDriver Path, Github Username and Password.

## Dependencies
1) Python
  Libraries
  a)Selenium
  b)webdriver_manager
2) git Bash
3) Chromewebdriver https://chromedriver.chromium.org/downloads

#How Does It Work?

Run the shell script from bash/terminal/cmd as ./create_project.sh <path_of_the_project>.
Example
If I want my project in Documents folder I will run the command
.\create_project.sh C:\Users\Asus\Documents

You will be prompted to enter a Repository name.
This Repository name will be same on your local machine as well as Github.

Sit back and within 10 seconds you will be having an online Github Repository connected to your system.





