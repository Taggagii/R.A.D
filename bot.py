import discord
import os
import subprocess as sub
import psutil

client = discord.Client()

my_path = os.getcwd()
program_instance = False
currently_installed = os.path.isdir("web-application")

def run_command(command):
    value = sub.Popen(command, stdout = sub.PIPE, stderr = sub.PIPE)
    return value.communicate()
    
def kill():
    global program_instance
    if not program_instance:
        return "Program instance not initiated";
    process = psutil.Process(program_instance.pid)
    for proc in process.children(recursive = True):
        proc.kill()
    process.kill()
    program_instance = False
    return "Instance Killed"

def delete_if_exists():
    global currently_installed
    kill()
    if currently_installed:
        os.system("rmdir /S /Q web-application")
        while currently_installed:
            currently_installed = os.path.isdir("web-application")


def download_from_git():
    #pull from git
    global currently_installed
    kill()
    delete_if_exists()
    instance = sub.Popen("git clone https://github.com/taggagii/web-application")
    instance.communicate()
    currently_installed = True
    return "Successfully downloaded"
    
def run(download = False):
    global program_instance
    folders = run_command("dir")
    if not currently_installed or download:
        download_from_git()
    kill()
    path = my_path+"\\web-application"
    #installing values in pipenv
    install_command_instance = sub.Popen("pipenv install", cwd = path)
    install_command_instance.communicate()
    
    program_instance = sub.Popen("pipenv run app.py", cwd = path)
    return "App Running"

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
        await message.channel.send(run())

    if checker("kill"):
        await message.channel.send(kill())

    if checker("download"):
        await message.channel.send(download_from_git())

    if checker("run download"):
        await message.channel.send(run(download = True))
        
with open(".key", "r") as key:
    client.run(key.read())

