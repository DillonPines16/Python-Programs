from irc1 import *
import os
import random
import uuid

channel = "#freebsd"
server = "irc.freenode.net"
nickname = "PickleRick"

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
