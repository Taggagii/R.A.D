import discord
import os
import subprocess as sub
import psutil

client = discord.Client()

my_path = os.getcwd()
program_instance = False

def run_command(command, return_output = True):
    value = sub.Popen(command, stdout = sub.PIPE, stderr = sub.PIPE)
    if return_output:
        return value.communicate()
    
def kill():
    global program_instance
    if not program_instance:
        return;
    process = psutil.Process(program_instance.pid)
    for proc in process.children(recursive = True):
        proc.kill()
    process.kill()
    program_instance = False

def download_from_git():
    #pull from git
    sub.Popen("git clone https://github.com/taggagii/web-application")

def run(download = False):
    global program_instance
    folders = run_command("dir")
    if "web-application" not in folders or download:
        download_from_git()
    kill()
    path = my_path+"\\web-application"
    #installing values in pipenv
    install_command_instance = sub.Popen("pipenv install", cwd = path)
    install_command_instance.communicate()
    
    program_instance = sub.Popen("pipenv run app.py", cwd = path)



@client.event
async def on_ready():
    print("Gitty woke")



@client.event
async def on_message(message):
    if message.author.bot or not message.channel.id == 819580264312995911:
        return;
    command = message.content

    checker = lambda command_name: command == command_name

    if checker("run"):
        run()

    if checker("kill"):
        kill()

    if checker("download"):
        download_from_git()

    if checker("run download"):
        run(download = True)
        
with open(".key", "r") as key:
    client.run(key.read())

