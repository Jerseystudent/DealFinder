# Import the pycord library into your runtime. 
import discord

# Assign the discord client to an object, we call client.
# All discord actions will act on this variable.
client = discord.Client()

# This is a function.
# It executes whenever the bot has successfully initialised. 
# In this case, it simply prints "We have logged in ..." to the terminal.
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# This function executes whenever the bot has received a new message.
# This can be a DM or a message in a channel that the bot can see.
@client.event
async def on_message(message):
    # If the message starts with $hello, respond with Hello!
    if message.content.startswith("$alright babs"):
        await message.channel.send("Alright there babs :wales:")
        
    if message.content.startswith("$deal"):
        splitMsg = message.content.split(' ')
        backTogether = ""
        for i in range(1,len(splitMsg)):
            backTogether = backTogether + splitMsg[i] + " "

        messageAck = "looking for a deal for: " + backTogether + " \U0001F911"
        await message.channel.send(messageAck)

        
        studentBean = []
        for i in range(1,len(splitMsg)):
            studentBean.append(splitMsg[i])
            studentBean.append("-")
            
        beanLink = "https://www.studentbeans.com/student-discount/uk/"
        for i in range(0,len(studentBean)-1):
            beanLink = beanLink + studentBean[i]
        messageBean = "studentbeans: " + beanLink
        await message.channel.send(messageBean)

        totum = []
        for i in range(1,len(splitMsg)):
            totum.append(splitMsg[i])
            totum.append("-")
            
        totumLink = "https://www.totum.com/se/student-discount/"
        for i in range(0,len(studentBean)-1):
            totumLink = totumLink + totum[i]
        messageTotum= "totum: " + totumLink
        await message.channel.send(messageTotum)

        unidays = []
        for i in range(1,len(splitMsg)):
            unidays.append(splitMsg[i])
            
        unidaysLink = "https://www.myunidays.com/GB/en-GB/partners/"
        for i in range(0,len(unidays)):
            unidaysLink = unidaysLink + unidays[i]
        unidaysLink = unidaysLink + "/view"
        messageUnidays= "unidays: " + unidaysLink
        await message.channel.send(messageUnidays)

    if message.content.startswith("$help"):
        helpMessage1= "**To test if its online, do $alright babs**"
        helpMessage2= "**To find a deal, do $deal <business name>**"
        helpMessage3= "**To get help, do $help**"
        await message.channel.send(helpMessage1)
        await message.channel.send(helpMessage2)
        await message.channel.send(helpMessage3)


# Discord API token needed below to run properly
client.run("")


