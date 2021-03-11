const discord = require("discord.js");
const { spawn } = require('child_process');
const client = new discord.Client(); 

const channelName = "819580264312995911";

const runningCommand = "run";

client.on("ready", () => {
    console.log(`Gitty has woken up`);
    channel = client.channels.cache.get(channelName);
});

var running = false;
var commandValue;

client.on("message", async message => {
    if (message.author.bot)
    {
        return;
    }
    if (message.channel.id !== channelName)
    {
        return;
    }
    
    var command = message.content;
    if (command === "help")
    {
        channel.send(`Type: "${runningCommand}"`);
    }
    if (command === runningCommand)
    {

        if (running)
        {
            spawn("kill.bat");
            running = false;
        }

        commandValue = spawn('Run Web Application.bat');
        running = true;

        commandValue.stdout.on("data", (data) => {
            console.log(`${data}`);
        });

        commandValue.stderr.on("data", (data) => {
            console.error(`${data}`);
        });

        commandValue.on("exit", (code) => {
            console.log("left with: " + code);
        })
        
    }

});



client.login("ODE5NTgzNTQxNzQxNDg2MTYw.YEoupw.ejwEnGQJWFpJH35czV1sXfbACOo");