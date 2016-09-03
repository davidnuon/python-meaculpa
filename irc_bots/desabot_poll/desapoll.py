# -*- coding: utf-8 -*-

from __future__ import with_statement
import os
import string
import socket
import sys
import time
import traceback
import threading as t
import random as r
from config import *

c = socket.socket()

def rawsend(element) :
    c.send(element)

def chsend(msgtype, channel, msg) :
    rawsend("%s %s :%s\r\n" % (msgtype, channel, msg))

# Bot functions
class Bot :
    print 'Class Bot, confirmed'
    
    def end(self) :
        c.send('QUIT \r\n')
        return 'Goodbye good peoples!'
        
    def join(self, inp) :
        c.send('JOIN %s\r\n' % (inp))
        return 'Joined %s.' % inp

        
class Poll :
    print 'Class Poll, confirmed'

    def debug(self, target) :
        print 'Poll Info: ',polldata
        print 'Yes Count: ',polldata[0]
        print 'No Count: ',polldata[1]
        print 'Question: ',polldata[2]
        print 'Yes Voters: ',yvoters
        print 'No Voters: ',nvoters
        print 'Sans List ',tvoters
        self.owner = 'Checkup complete.'
        self.other = '=D That tickles, I\'ll make sure you die happy %s.' % target
        
    def set(self,que) :
        print 'Current Poll Data: ',polldata
        print 'Current question: ',polldata[2]
        polldata[2] = que
        print 'New Question: ',polldata[2]
        return 'Poll topic set as %s.' % polldata[2]
        
    def reset(self) :
        print 'Poll Info: ',polldata
        print 'Yes Count: ',polldata[0]
        print 'No Count: ',polldata[1]
        print 'Question: ',polldata[2]
        print 'Yes Voters: ',yvoters
        print 'No Voters: ',nvoters
        print 'Sans List ',tvoters
        yvoters[:]  = []
        nvoters[:]  = []
        tvoters[:]  = []
        polldata[0] = 0 
        polldata[1] = 0
        return 'Poll reset.'

# Class, Start! 
bot  = Bot()           
poll = Poll()

def parsemsg(msg) :
    # Breaks things up so 
    complete  = msg[1:].split(":", 1)
    info      = complete[0].split(" ")
    msgpart   = complete[1]
    sender    = info[0].split("!")
    ask       = msgpart.split(" ")

    cmd       = msgpart[1:].strip()
    receiver  = None
    msgpart   = msgpart.lower()
    gou       = cmd.split()
    lcmd      = cmd.lower()

    # html logging
    
    log = file("chatlog.html", "a")
    log.write('[%s] %s : %s<br>' % (time.strftime("%I:%M %p"), info[0], msgpart))
    log.close()
    
    class Message(t.Threading) :
    
        pmlock = t.Lock()
    
        def run(self): 
            print 'Class Message, Go'  
            
        def pm(msg):
            with pmlock:
                rawsend("PRIVMSG %s :%s\r\n" % (info[2], msg))
                
    m = Message()
                
    def error() :
        print "Exceptions: ";      print '-'*60
        traceback.print_exc(file=sys.stdout); print '-'*60        

    if msgpart[0] == '=' :
            #Poll
            if gou[0] == 'poll' :
                try :
                    if gou[1] == 'set' and sender[0] == owner :
                        cmd = cmd.replace('poll set ', '')
                        m.pm(poll.set(cmd))
                        error()
                    elif gou[1] == 'de' :
                        if sender[0] == owner :
                            m.pm(poll.debug(sender[0]).owner)
                        else :
                            m.pm(poll.debug(sender[0]).other)
                    elif gou[1] == 'reset' and sender[0] == owner : 
                        m.pm(poll.reset())
                        error()
                    elif gou[1] == 'yes' :
                        m.pm(poll.vote('yes', sender[1], sender[0]))
                        error()
                    elif gou[1] == 'no' :
                        m.pm(poll.vote('no', sender[1], sender[0]))
                        error()
                    elif gou[1] == 'info' :
                        m.pm(poll.pollinfo())
                        error()
                    elif gou[1] == 'voters' :
                        m.pm(poll.voterinfo())
                        error()
                except :
                    m.pm('syntax: =poll <action>')
                        
                else :
                    m.pm('What the hell are you talking about, %s?' % sender[0])

c.connect((host, port))
c.send("NICK %s\r\n" % (botnick))
rawsend("USER %s %s bla : %s \n" % (ident, host, realname)) 

    # Send user info
if botpass != "" :
    # identify with nickserv
    chsend("PRIVMSG", "NickServ", "IDENTIFY %s" % (botpass))

    # Join your channels


for n in chan :
    rawsend("JOIN %s\n" % n)
    rawsend("PRIVMSG %s :%s\r\n" % (n, 'Meh, I\'m just desabot with a longer name...'))
    print chan
    

while 1 :
    # Logging
    lineget = c.recv(4096); print lineget
    linedown = file("log.txt", "a")
    linedown.write(lineget)
    linedown.close()

    # Parse line for commads
    if lineget.find("PRIVMSG")!=-1 :
        parsemsg(lineget)
    if lineget.find('KICK')!=-1 :
        for chan in chan :
           rawsend("JOIN %s\n" % (chan))

    # Ping-Pong is a game of life or death
    lineget = lineget.rstrip()
    lineget = lineget.split()
    if lineget[0] == "PING" :
        c.send("PONG %s \n" % lineget[1])