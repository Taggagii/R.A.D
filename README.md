# R.A.D

## Background
The name R.A.D is an acronym standing for "Remote Application Deployer" and the inspiration for this name was stolen directly from [Jacob Albanese's](https://github.com/Jalbanese1441)
deployment bot, DAB. I made this bot because I needed a way to deploy code from a GitHub repo without having full control over someone's computer. This bot is built to be hardcoded with the repo name and link address as that lower's the chance that someone will try to take control of one's computer

## Controls
### run
Takes the hardcoded repo name and checks if it is installed, if it is, then the code will find a specified file inside, named "app.py" and run it in it's pipenv.
### download 
Deletes the previous download of the repo (if one exists) and grabs a new one from GitHub
### ping
Send's some general information about if the bot is running and if it's downloaded (can be used to see if the bot is currently runninging or if it's been broken by something
