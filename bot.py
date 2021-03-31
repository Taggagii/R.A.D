import discord
import os
import subprocess as sub
import psutil
import math

client = discord.Client()

my_path = os.getcwd()
path = my_path+"\\web-application"
program_instance = False
currently_installed = os.path.isdir("web-application")
sub.Popen("pip install pipenv")

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
    if not currently_installed or download:
        download_from_git()
    kill()
    
    #installing values in pipenv
    install_command_instance = sub.Popen("pipenv install", cwd = path)
    install_command_instance.communicate()
    
    program_instance = sub.Popen("pipenv run app.py", cwd = path)
    import time
    time.sleep(5)
    return "App Running"

@client.event
async def on_ready():
    print("Gitty woke")

def remove_repeats(values, exceptions = []):
    newList = []
    [newList.append(value) for value in values if value not in newList or value in exceptions]
    return newList

def fix_user_log():
    #fixing repeats
    values = open("web-application/User-Logs.txt", "r").readlines()
    values = remove_repeats(values, ["-----WebSite Restart---"])
    with open("web-application/User-Logs.txt", "w") as file:
        file.write("\n".join(values))

@client.event
async def on_message(message):
    global currently_installed
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
        
    if checker("ping"):
        currently_installed = os.path.isdir("web-application")
        await message.channel.send("Running:" + f"\n{program_instance=}, {currently_installed=}")

    if checker("show log"):
        if currently_installed:
            fix_user_log()
            values = open("web-application/User-Logs.txt", "r").read()
            length_of_output = len(values)
            number_of_sections = math.ceil(length_of_output / 2000)
            section_length = math.ceil(length_of_output / number_of_sections)
            for i in range(number_of_sections):
                index = i * section_length
                await message.channel.send(values[index:index + section_length])
            
                
            
with open(".key", "r") as key:
    client.run(key.read())

