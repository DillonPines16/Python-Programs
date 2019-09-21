from irc1 import *
import os
import random
import uuid

channel = "" ## Insert the IRC channel you would like to connect to.
server = "" ## Insert the server you would like to connect to.
nickname = "" ## Insert your desired username.

randFile = str(uuid.uuid4())
textFile = ".txt"
NewFile = randFile + textFile

irc = IRC()
irc.connect(server, channel, nickname)

while 1:
    text = irc.get_text()
    print text

    outF = open(NewFile, "a")
    for line in text:
        outF.write(line)
