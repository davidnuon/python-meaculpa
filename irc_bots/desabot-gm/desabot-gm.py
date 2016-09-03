# -*- coding: utf-8 -*-

import sys, traceback
import string
import socket
import os
import time
import random as r
from gamedata import *

def send(self, to, msg):
	"""Sends a message "msg" to "to" """
        s.send('PRIVMSG %s :%s\r\n' % (to, msg))

def sendresponse(self, to, msg, nick):
        """Personalized version of send."""
    	msg = msg.replace('[nick]', nick)
    	s.send('PRIVMSG %s :%s\r\n' % (to, msg))

def me(s): return ctcp('ACTION %s' % s)

def rightnow():
    "Return a string representing the current time and date."
    return time.strftime('%X on %x',time.localtime(time.time()))

def factoidsdict():
    f = open('data.txt', 'r')
    toggle = True
    for line in f:
	if toggle:
		key = line.rstrip()
    		toggle = False
    	else:
		value = line.rstrip()
		toggle = True
		TABLE[key] = value
    f.close()
       
def parsemsg(msg): 
    complete=msg[1:].split(':',1)
    info=complete[0].split(' ')
    msgpart=complete[1]
    sender=info[0].split('!')
    ask=msgpart.split(' ')

    if msgpart[0]=='`' and sender[0] in (OWNER, ADMIN, ADMIN2, MODE == '+e'):
        cmd=msgpart[1:].split(' ')
	response=cmd[1].split(' ')
	# ` commands follow:
	if cmd[0]=='say':
	    response = ' '.join(cmd[2:])
	    s.send('PRIVMSG %s :%s' % (cmd[1], response))
	if cmd[0]=='notify':
	    s.send('notify %s %s\n' % (cmd[1], cmd[2]))
        if cmd[0]=='op':
            s.send('MODE %s +o %s \n' % (info[2], cmd[1]))
	if cmd[0]=='kill':
	    s.send('kick %s %s %s\r\n' % (cmd[1], cmd[2], cmd[3]))
	    s.send('PRIVMSG %s :%s, I hope you know what you are doing.\n' % (info[2], sender[0]))
        if cmd[0]=='deop':
            s.send('MODE %s -o %s \n' % (info[2], cmd[1]))
	    reply = 'muhahahaha'   
###### SAVE BOOKMARK POINT ######
	if cmd[0]=='part':
            s.send('PART %s\r\n' % (info[2]))
        if cmd[0]=='voice':
            s.send('MODE %s +v %s \n' % (info[2], cmd[1]))
	    reply = 'Oh, but it was so quiet'
        if cmd[0]=='devoice':
            s.send('MODE %s -v %s \n' % (info[2], cmd[1]))
	    reply = 'Much better'
	if cmd[0]=='invite':
	    s.send('invite %s %s\n' % (cmd[1], info[2]))
	if cmd[0]=='kick':
	    s.send('kick %s %s\r\n' % (info[2], cmd[1]))
	if cmd[0]=='part' and sender[0] == OWNER :
	    s.send('part %s %s\r\n' % (info[2], cmd[1]))
        if cmd[0]=='sys':
            syscmd(msgpart[1:],info[2])

    if msgpart[0]=='-' and (sender[0] == OWNER or sender[0] == ADMIN and MODE[0] == '+e'):
        cmd=msgpart[1:]
        s.send('%s \n' % (cmd))
        print 'cmd= %s' % (cmd)

    if msgpart[0]=='=':
        cmd=msgpart[1:].strip()
	receiver = None
	if cmd.find('|')!=-1:
		cmd = cmd.split('|')
		receiver = cmd[1].strip()
		cmd = cmd[0].strip()
	channel=info[2]
	factoids(cmd,channel,sender,receiver)
	msgpart = msgpart.lower()
	
	
def factoids(cmd,channel,sender,receiver):
    print cmd
    reply = "%s I have no idea what you're talking about" % (sender[0])
    if cmd.startswith("+") and sender[0] in (OWNER, ADMIN, ADMIN2, TEACHER, TEACHER2, MODE == '+e'):
	try:
		var = cmd[1:].split(' as ', 1)
     	        key=var[0].lower()
		value=var[1]
        except:
                reply = 'I am sorry, your syntax is wrong. Correct syntax is =+[key] is [def]'
                pass
        else:
      	        if TABLE.get(key) is None: reply = "Reply for =%s was added" % (key)
                elif TABLE.get(key)!=None: reply = "Reply =%s overwritten" % (key)
                TABLE[key]='%s' % value

    if TABLE.get(cmd)!= None: reply = TABLE.get(cmd)

    if cmd == 'save' and sender[0] in (OWNER, ADMIN, ADMIN2, TEACHER, TEACHER2, MODE == '+e'):
       keys = sorted(TABLE.keys())
       replies=file('data.txt','w')
       for key in keys: replies.write('%s\n%s\n' % (key, TABLE.get(key)))
       reply = 'I will remember this.'

# '=' commands follow:
    if cmd.find('join')!=-1 and sender[0] in (OWNER, ADMIN, ADMIN2):
       chan = cmd.split(' ')
       print cmd
       s.send('JOIN %s\r\n' % (chan[1]))
       reply = 'done'
    if cmd == 'part' and sender[0] in (OWNER, ADMIN, ADMIN2, MODE[0] == '+e'):
       s.send("PRIVMSG %s : Bye\r\n" % (channel))
       s.send('PART %s\r\n' % (channel))
    if receiver != None:
	s.send('PRIVMSG %s :%s, %s\n' % (channel, receiver, reply))
    elif receiver == None:
	s.send('PRIVMSG %s :%s\n' % (channel, reply))

def syscmd(commandline,channel):
	cmd=commandline.replace('sys ',' ')
	cmd=cmd.rstrip()
	os.system(cmd+' >temp.txt')
	a=open('temp.txt')
	ot=a.read()
	ot.replace('n','|')
	a.close()
	s.send('PRIVMSG %s :%s\n' % (channel, ot))
	return 0

#Connection
factoidsdict()
s=socket.socket( )
s.connect((HOST, PORT))
s.send('NICK %s \n' % (NICK)) #Tells nick server nickname
s.send('USER %s %s bla : %s \n' % (IDENT, HOST, REALNAME))
 #Tells user Identity, current host, and actual name
s.send('PRIVMSG NickServ :IDENTIFY %s\r\n' % (PASS))
s.send('PRIVMSG ChanServ :OP %s\r\n' % (CHAN))

while 1:  #While True
    line=s.recv(4096)
    print line
    log = file('log.txt', 'a')
    log.write(line)
    log.close()
    if line.find('Welcome to the freenode IRC Network')!=-1:
        s.send('JOIN %s\n' % (CHAN))
        s.send('JOIN %s\n' % (CHAN2))
    if line.find('KICK #grubbN desabot :grubbot')!=-1:
        s.send('JOIN %s\n' % (CHAN))
    if line.find('KICK #grubbN desabot :')!=-1:
        s.send('JOIN %s\n' % (CHAN))
    if line.find('grubbot kicked desabot: grubbot')!=-1:
        s.send('JOIN %s\n' % (CHAN))        
    if line.find('KICK #grubbN desabot :asshole')!=-1:
        s.send('JOIN %s\n' % (CHAN))
    if line.find('kicked desabot:')!=-1:
        s.send('JOIN %s\n' % (CHAN))
	s.send('PRIVMSG %s :Hello good people, I\'m dn_desaku\'s bot.\r\n' % (CHAN))
	s.send('PRIVMSG NickServ :IDENTIFY %s\r\n' % (PASS))
	s.send('PRIVMSG ChanServ :OP %s\r\n' % (CHAN))
    if line.find('PRIVMSG')!=-1:
        parsemsg(line)
    line=line.rstrip()
    line=line.split()
    if(line[0]=='PING'):
    	s.send('PONG %s \n' %line[1])