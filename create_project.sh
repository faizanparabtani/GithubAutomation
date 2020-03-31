#!/bin/sh
project_path=`pwd`
cd $1
echo 'Enter Folder name'
read folder_name
mkdir $folder_name
cd $folder_name
fold=$folder_name
#Initialization of Folder as a Git tracked project
git init
cd "$project_path"
#Python Script called with the folder name as the Repository name
python webscraper.py "$folder_name"
cd $1
cd $folder_name
sleep 10
#Linking git to Github
#Replace <Github User> with your Github Username
git remote add origin https://github.com/<Github User>/$fold.git


$SHELL
