import string
import socket
from config import *
from dict import *

import time
import os
import random as r

c = socket.socket( )

def rawsend(element) :
    c.send(element)
def chsend(msgtype, channel, msg) :
    rawsend("%s %s :%s\r\n" % (msgtype, channel, msg))

class ownr :
    def __init__(self) :
        print "Passed owner"
            
    def say(self, reciever, message) :
        c.send("PRIVMSG %s :%s\r\n" % (reciever, message))
    def quit(self, reason) :
        c.send("QUIT %s\r\n" % (reason))
    def nick(self, nickname) :
        c.send("NICK %s\r\n" % (nickname))
    def join(self, channel) :
        c.send("JOIN %s\n" % (channel))
    def part(self, channel) :
        c.send("PART %s\r\n" % (channel))

                
class opr :
    def __init__(self) :
        print "Passed opr"
    def kick(self, channel, person, reason) :
        if person not in unkickable :
            c.send("KICK %s %s %s\r\n" % (channel, person, reason))
        else :
            send("%s is not kickable" % (person))
    def topic(self, channel, response) :
        response = ' '.join(op[1:])
        c.send('TOPIC %s :%s \n' % (channel, response))
    def ban(self, channel, person) :
        if person not in unbanable :
	    c.send("MODE %s +b: %s*!*@*.*\r\n" % (channel, person))  
        else :
            send("%s is not banable" % (person))
    def unban(self, channel, person) :
        c.send("MODE %s -b: %s*!*@*.*\r\n" % (channel, person))
    def oper(self, channel, person) :
        c.send("MODE %s +o %s \n" % (channel, person))
    def deop(self, channel, person) :
        if person not in deoperable :
            c.send("MODE %s -o %s \n" % (channel, person))
        else :
            send("%s is not deopable" % (person))
    def voice(self, channel, person) :
        c.send('MODE %s +v %s \n' % (channel, person))
    def devoice(self, channel, person) :
        c.send('MODE %s -v %s \n' % (channel, person))
        
class comd :
        def __init__(self) :
            print "passed comd"
            
        def chuck(self) :
            r.shuffle(chucklist)
            chuck = chucklist[0]
            send(chuck)
        def random(self) :
            random = r.random()
            send(random)
        def fortune(self) :  
            fortune = os.popen('fortune -s').read().replace('\n', ' ')
            send(fortune)
        def list(self) :
            List = os.popen('ls /').read().replace('\n', ' ')
            send(List)
        def time(self) :
            Time = time.strftime("%H:%M")
            send("The current time is %s Pacific Time\r\n" % (Time))            
        def stfu(self) :
            if op[1] == owner :
                send("%s, I will not tell my master to shut up" % (sender[0]))
            elif op[1] == "grubbot" :
                if sender[0] == owner :
                    send("Sorry "+owner+", I'll quiet down")
                else :
                    send("Don't tell me to shut up %s" % (sender[0]))
            elif sender[0] == op[1] :
                send("You need to tell yourself to shut up %s? How pathetic" %\
                (sender[0]))
            else :
                send("%s wants you to shut up %s" % (sender[0], op[1]))     
        def contact(self, pers) :  
            chsend("PRIVMSG", pers,"%s wants you in %s" % (sender[0], info[2]))
            send("I have contacted %s for you" % (pers))
            
class parrot :
    def __init__(self) :
        print  "Parrot passed"
    def add(person) :
        parrotL.append(person) 
        send("I will now repeat everything %s says" % (person))
    def rm(person) :
        parrotL.remove(person) 
        send("I'll stop copying %s now" % (person))
    def list() :
        send(parrotL)
comd = comd() 
opr = opr()
parrot = parrot()
        
def parsemsg(msg) :
    complete = msg[1:].split(":", 1)
    info = complete[0].split(" ")
    msgpart = complete[1]
    sender = info[0].split("!")
    ask = msgpart.split(" ")

    cmd  = msgpart[1:].strip()
    receiver = None
    msgpart = msgpart.lower()
    op = cmd.split()
    
    def send(msg) :
        rawsend("PRIVMSG %s :%s\r\n" % (info[2], msg))
    if msgpart[0] == "~" :
        # Operator Commands
        if cmd == "ban" and sender[0] in admin :         
            opr.ban(info[2], op[1])
            opr.kick(info[2], op[1], "Youre_banned")
        elif cmd == "unban" and sender[0] in admin :
            opr.unban(info[2], op[1])
        elif op[0] == 'kick' :
            try :
                opr.kick(info[2], op[1], op[2])    
                send("%s has been elminated" % (op[1]))
            except :
                try :
                    opr.kick(info[2], op[1], "grubbot")
                    send("%s has been elminated" % (op[1]))
                except :
                    send("WHY!!??")    
                send("Oreos are good.")
        elif cmd == "op" and sender[0] in admin :
            opr.oper(info[2], op[1])
            send("%s is now a channel operator" % (op[1]))
        elif cmd == "deop" and sender[0] in admin :
            opr.deop(info[2], op[1])
            send("%s is now not a channel operator" % (op[1]))    
        elif cmd == "voice" and sender[0] in admin :
            opr.voice(info[2], op[1])
            send("%s has been voiced" % (op[1]))           
        elif cmd == "devoice" and sender[0] in admin :
            opr.devoice(info[2], op[1])
            send("%s has been devoiced" % (op[1]))           
        elif cmd == "topic" and sender[0] in admin :
            response = ' '.join(op[1:])
            opr.topic(info[2], response)
            send("The topic now is %s" % (response))

        # Owner functions
        elif cmd == "ignore" and sender[0] == owner :
            if op[1] == "add" :
                ignore.append(op[2]) 
                send("I will now ignore whatever %s says" % (op[2]))
            elif op[1] == "rm" :
                ignore.remove(op[2])
                send("I will now pay attention to %s" % (op[2]))

        elif cmd == "quit" and sender[0] in (owner) :
            try :
                if op[1] == "reset" :
                    send("Be back!")
                    chsend("QUIT", "", "resetting")
                    os.system("./run") 
                elif op[1] == "exit" :
                    send("Exiting..!")
                    ownr.quit(op[1])
                else :
                    send("Can not exit")
            except :
                send("Not enough arguments. Use \"~quit exit\" to exit or \
\"~quit reset\" to reset")
            
        elif cmd == "join" and sender[0] == owner :
            join(op[1])
            send("Joined %s" % (op[1]))
        elif cmd == "part" and sender[0] == owner :
            try :
                ownr.part(op[1])
            except :
                owner.part(info[2])
        elif cmd == "say" and sender[0] == owner :
            response = ' '.join(op[2:])
            ownr.say(op[1], response)
        elif cmd == "nick" and sender[0] == owner :
            ownr.nick(op[1])
            send("Nick changed to %s" % (op[1]))
            
            
        # Public functions
        elif sender[0] not in ignore :
            if cmd == "" :
                send("You did not input a command")   
            elif cmd == "chuck" :
                comd.chuck()
            elif cmd == "random" :
                comd.random()
            elif cmd == "fortune" :
                comd.fortune()
            elif cmd == "list" :
                comd.list()
            elif cmd == "time" :
                comd.time()
                
            # Functions that have arguments
            elif cmd == "stfu" :
                comd.stfu()
            elif cmd == "contact" :
                comd.contact(op[1])            
            elif cmd == "parrot" and sender[0] in admin:
                if op[1] == "add" :
                    parrot.add(op[2])                
                elif op[1] == "rm" :
                    parrot.rm(op[2]) 
                elif op[1] == "list" :
                    parrot.list()
                else :
                    send("Invalid argument (%s)" % (op[1]))                   
            else :
                send("Repeat that one again?")
    # Text search
    if sender[0] not in ignore :
        if sender[0] in parrotL :
            send(msgpart)
            
        if (msgpart.startswith(sender[0])) :
            send("I'm glad you know your name, %s" % (sender[0]))
            
        if (msgpart.find("hugs "+botnick)!=-1) :
            send("Get away from me %s!!!" % (sender[0]))
    
        if (msgpart.find("kick me")!=-1) :
            send("My Pleasure!")
            opr.kick(info[2], sender[0], "bye")
            send("Pwnt, bitch")
   
        if ((msgpart.find("hi "+botnick)!=-1) | \
        (msgpart.find("hello "+botnick)!=-1) |
        (msgpart.find("hey "+botnick)!=-1)) :
            send("hello %s" % (sender[0]))
    
        if (msgpart.find("M$")!=-1 | (msgpart.find("Micro$oft")!=-1) |\
            (msgpart.find("microshit")!=-1)) :
            send("Stop being a troll, %s" % (sender[0]))

""" Connecting to the IRC server. """
ownr = ownr()
c.connect((host, port))
ownr.nick(botnick) # Declare your nick
rawsend("USER %s %s bla : %s \n" % (ident, host, realname)) # Send user info
if botpass != "" :
    # identify with nickserv
    chsend("PRIVMSG", "NickServ", "IDENTIFY %s" % (botpass))

# Join your channels
for chan in chan :
    ownr.join(chan)

while True :
    # Recovers anything that happens, prints it, then writes it to file
    rec = c.recv(4096); print rec
    record = file("raw", "a"); record.write(rec); record.close()
    # If it finds any commands given to it, it parses them
    if rec.find("PRIVMSG")!=-1 :
        parsemsg(rec)

    """ Prevents the bot from timing out, if it does, it alerts the server that
    it's alive by playing ping pong """
    rec = rec.rstrip()
    rec = rec.split()
    if rec[0] == "PING" :
        c.send("PONG %s \n" % rec[1])
