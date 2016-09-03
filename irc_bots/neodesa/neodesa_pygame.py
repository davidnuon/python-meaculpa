# -*- coding: utf-8 -*-

import os
import string
import socket
import sys
import time
import traceback
import threading
import pygame
import random as r
from config import *

# pygame stuff

pygame.init()

width   = 640
height  = 400
font    = pygame.font.Font(None, 17)
screen  = pygame.display.set_mode((width, height))
refresh = pygame.display.flip
mousemo = pygame.MOUSEMOTION
line    = pygame.draw.line
x = y = 0

c = socket.socket()

# Poll Data

polldata = [0, 0, 'Is this a poll?']
yvoters  = []
nvoters  = []
tvoters  = []

# Card Game Data

thedeck = [
        'The Chainsaw Madman',
        'The Chuck Norris',
        'The Suicidal Bomber',
        'The Penguin',
        'The Paper',
        'The Rock',
        'The Nathangrubb',
        'The IRC Bot',
        'The Donut',
        'The Fireball',
        'The Cupcake',
        'The Fool',
        'The Lovers',
        'The Chariot',
        'The Empress',
        'The King',
        'The Bannana',
        'The PC',
        'The Blade',
        'The Poison',
        'The Cup',
        'The Death',
        'The Fly'
        ]

pdraw    = []    # Prevents multiple draws
splayers = []    # Player registry Name
players  = []    # Player Whois
dgoal    = ['']  # The Goal 

# Ignore

ignorel = []

# Über important

def rawsend(element) :
    c.send(element)

def chsend(msgtype, channel, msg) :
    rawsend("%s %s :%s\r\n" % (msgtype, channel, msg))
    
# Some Neo Testing
class Neo( threading.Thread ) :
    print 'Class Neo, confirmed'
        
    def status(self) :
        return 'I\'m not complete yet...'

# Saws...bzz..bzz
class Saw( threading.Thread ):
    print 'Class Saw, confirmed'
        
    def reg(self, target) :
        return 'It will be my pleasure to chainsaw %s with my shiny, new chainsaws' % target
    
    def owen(self, target) :
        return \
        'No, I will not target my master. Instead I will go after you %s' \
        % target

    def mysf(self, target) :
        return \
        'NO, I will not kill myself. Instead, I will hunt you down, extract every drop of blood from your body and drink it like Kool-Aid %s' \
        % target
    def notarget(self, case, target) :
        if   case  == 1 :
            return 'I\'m waiting...'
        elif case  == 2 :
            return 'If you don\'t tell me a target, I will chainsaw you in your sleep %s.' % target
        elif case  != 1 | 2 :
            print 'There was an error, but %s was the target.' % target
            return '[ERROR]'

# Polls
class Poll ( threading.Thread ):
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

    def vote(self, option, voterwhois, votername) :
        if option == 'yes' :
            try :
                tvoters.index(voterwhois)
                print 'lol %s is a bastard' % votername
                return 'You sick bastard, you tried voting twice.'
            except :
                polldata[0] = polldata[0] + 1
                print 'Poll Data: ',polldata
                yvoters.append(votername)
                print 'Added %s to yes' % votername
                tvoters.append(voterwhois)
                print 'Add %s to main sans-list' % voterwhois
                return 'Your poll has been counted %s. You have voted yes for "%s."' % (votername, polldata[2])
        elif option == 'no' :
            try :
                tvoters.index(voterwhois)
                print 'lol %s is a bastard' % votername
                return 'You sick bastard, you tried voting twice.'
            except :
                polldata[1] = polldata[1] + 1
                print 'Poll Data: ',polldata
                nvoters.append(votername)
                print 'Added %s to no' % votername
                tvoters.append(voterwhois)
                print 'Add %s to main sans-list' % voterwhois
                return 'Your poll has been counted %s. You have voted no for "%s."' % (votername, polldata[2])
        else :
            return '[ERROR]'

    def pollinfo(self) :
        print polldata
        yes = polldata[0]
        no = polldata[1]
        que = polldata[2]
        return '"%s" Yes : %s - No : %s' % (que,yes,no)
    
    def voterinfo(self) :
         if tvoters != [] :
                print 'Yes voters: ',yvoters
                print 'No voters: ',nvoters
                ye = str(yvoters)
                ne = str(nvoters)
                ye = str(ye).lstrip('[')
                ye = str(ye)[0:-1]
                ne = str(ne).lstrip('[')
                ne = str(ne)[0:-1]
                print 'yes: ',ye
                print 'no: ',ne
                if nvoters == [] :
                    ne = 'nobody'
                if yvoters == [] :
                    ye = 'nobody'
                return 'Yes : %s - No : %s' % (ye,ne)
         else :
                return 'Nobody has voted yet.'

# For the game of Fishing             
class Deck( threading.Thread ):
    print 'Class Deck, confirmed'

    def shuffle(self) :
        r.shuffle(thedeck)
        return 'Deck Shuffled.'
    
    def reset(self) :
        thedeck[:] = defudeck
        return 'Deck reloaded'
        
    def set(self, goal) :
        try :
             defudeck.index(goal)
             dgoal[0] = goal
             print goal
             return 'GOAL, SET: %s is the goal!' % goal
        except :
             return 'The card %s was not found' % goal
    
    def players(self) :        
        print splayers
        ye = str(splayers)
        ye = str(ye).lstrip('[')
        ye = str(ye)[0:-1]
        if splayers == [] :
             ye = 'nobody'
        return 'Current players : %s' % ye
        
    def register(self, name, whois) :
            try :
                players.index(whois)
                return '%s, you have already registered.' % name
            except :
                players.append(whois)
                splayers.append(name)
                return '%s, added to playlist.' % name
    def rm(self, name, whois) :
            try :
                players.remove(whois)
                splayers.remove(name)
                return '%s, you have been erased.' % name
            except :
                return '%s, you weren\'t playing.' % name
    
    def clear(self) :
            players[:] = []
            splayers[:] = []
            return 'Players list cleared.'
            
    def draw(self, name, whois) :
        print 'Draw. got there!'
        if whois in players :
            print 'Checking if %s is in players...' % whois
            try:
                try:
                    pdraw.index(whois)
                    return 'You sick bastard, you tried to draw twice.'
                except:
                    if thedeck[0] != dgoal[0] :
                        drawcard = str(thedeck[0])
                        thedeck.remove(str(thedeck[0]))
                        pdraw[:] = []
                        pdraw.append(whois)
                        return '%s drew %s' % (name, drawcard)
                    else:
                        print '%s won.' % name
                        thedeck.remove(str(thedeck[0]))
                        pdraw[:] = []
                        pdraw.append(whois)
                        return '%s drew %s, he wins!' % (name,dgoal[0])
            except :
                        error()
                        return 'There aren\'t any cards in the deck =('
        else :
            return 'You sick bastard, you can\'t play.'

    def show(self) :
        try : 
            return '%s was on top of the deck.' % str(thedeck[0])
        except :
            return 'There aren\'t any cards in the deck =('

    def contents(self) :
        try :
            print thedeck
            ye = str(thedeck)
            ye = str(ye).lstrip('[')
            ye = str(ye).lstrip('\'')
            ye = str(ye)[0:-1]
            return 'Deck Contents: %s.' % str(ye)
        except :
            return 'There aren\'t any cards in the deck =('

# Bot functions
class Bot(threading.Thread) :
    print 'Class Bot, confirmed'
    
    def end(self) :
        c.send('QUIT \r\n')
        return 'Goodbye good peoples!'
        
    def join(self, inp) :
        c.send('JOIN %s\r\n' % (inp))
        return 'Joined %s.' % inp

# Calls stuff 
class Call(threading.Thread) :
    print 'Class Call, confirmed'
    
    def now(self) :
        g = time.localtime()
        print g
        return'The date is: %s/%s/%s and the time is %s PST' % (g[1],g[2],g[0],time.strftime("%I:%M %p"))

# Ignore Class
class Ignore(threading.Thread) :
    print 'Class Ignore, confirmed'
    
    def add(self, target) :
        try :
            ignorel.index(target)
            return '%s is dead to me.' % target
        except :
            ignorel.append(target)
            return '%s will now be dead to me.' % target

    def rm(self, target) :
            ignorel.remove(target)
            return '%s will no longer be ignored.' % target
    
    def show(self) :
        print 'I am ignoring %s right now.' % ignorel
        return ignorel

# Class, Start! 
bot  = Bot()           
neo  = Neo()
saw  = Saw()
call = Call()
poll = Poll()
deck = Deck()
ignore = Ignore()

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
    
    def send(msg) :
        rawsend("PRIVMSG %s :%s\r\n" % (info[2], msg))
                
    def error() :
        print "Exceptions: ";      print '-'*60
        traceback.print_exc(file=sys.stdout); print '-'*60        
    
    if msgpart[0] == '=' :
        if sender[0] in ignorel :
            send('Go away, %s' % sender[0])
        else :
            try :
                #Neo
                if cmd == 'neo' :
                    send(neo.status())

                # cmd.exe = FUN </sarcasm>
                elif gou[0] == 'cmd' and sender[0] == owner:
                    yos = cmd.replace('cmd ','')
                    send(os.popen('cmd.exe /c ' + yos).read().replace('\n', ''))

                #ignore add 
                elif gou[0] == 'ignore' and sender[0] == owner:          
                    if gou[1] == 'add' :
                        send(ignore.add(gou[2]))
                    elif gou[1] == 'rm' :
                        send(ignore.rm(gou[2]))
                    elif gou[1] == 'show' :
                        send(ignore.show())
                    else :
                        send('syntax: ignore <action> <target>') 
                        
                #Ends the bot
                elif gou[0] == 'end' and sender[0] == owner:
                    send(bot.end())
                    
               #Joins channels
                elif gou[0] == 'join' and sender[0] == owner:
                    yos = cmd.replace('join ','')
                    send(bot.join(yos))
                    
                #Call, makes things more logical
                elif gou[0] == 'call' :
                    try :
                        if gou[1] == 'now' :
                            send(call.now())
                    except :
                        send('The call was not answered.')
                        
                #Saws
                elif gou[0] == 'saw' :
                    try :
                        if gou[1] == 'de' :
                            send('I love cleaning my chainsaws.')
                        elif lcmd.find('dn_desaku')  != -1 :
                            send(saw.owen(sender[0]))
                        elif lcmd.find('owner')      != -1 :
                            send(saw.owen(sender[0]))
                        elif lcmd.find('master')     != -1 :
                            send(saw.owen(sender[0]))
                        elif lcmd.find('myself')     != -1 :
                            send(saw.mysf(sender[0]))
                        elif lcmd.find('my_self')    != -1 :
                            send(saw.mysf(sender[0]))
                        elif lcmd.find('desabot')    != -1 :
                            send(saw.mysf(sender[0]))
                        elif lcmd.find('neo')        != -1 :
                            send(saw.mysf(sender[0]))
                        elif lcmd.find('neodesabot') != -1 :
                            send(saw.mysf(sender[0]))
                        else :
                            send(saw.reg(cmd.replace('saw ', '')))
                    except :
                        if sender[0] != owner :
                            send(saw.notarget(2, sender[0]))
                        else :
                            send(saw.notarget(1, owner))
                            
                #Poll
                elif gou[0] == 'poll' :
                    try :
                        if gou[1] == 'set' and sender[0] == owner :
                            cmd = cmd.replace('poll set ', '')
                            send(poll.set(cmd))
                            error()
                        elif gou[1] == 'de' :
                            if sender[0] == owner :
                                send(poll.debug(sender[0]).owner)
                            else :
                                send(poll.debug(sender[0]).other)
                        elif gou[1] == 'reset' and sender[0] == owner : 
                            send(poll.reset())
                            error()
                        elif gou[1] == 'yes' :
                            send(poll.vote('yes', sender[1], sender[0]))
                            error()
                        elif gou[1] == 'no' :
                            send(poll.vote('no', sender[1], sender[0]))
                            error()
                        elif gou[1] == 'info' :
                            send(poll.pollinfo())
                            error()
                        elif gou[1] == 'voters' :
                            send(poll.voterinfo())
                            error()
                    except :
                        send('syntax: +poll <action>')
                        
                #Card game
                elif gou[0] == 'deck' :
                    try:
                        if gou[1] == 'shuffle' and sender[0] == owner :
                            send(deck.shuffle())
                        elif gou[1] == 'reload' and sender[0] == owner :
                            send(deck.reset())
                        elif gou[1] == 'set' and sender[0] == owner :
                            yos = cmd.replace('deck set ', '')
                            send(deck.set(yos))
                        elif gou[1] == 'players' :
                            send(deck.players())
                        elif gou[1] == 'add'  :
                            send(deck.register(sender[0], sender[1]))
                        elif gou[1] == 'rm' :
                            send(deck.rm(sender[0], sender[1]))
                        elif gou[1] == 'clear' and sender[0] == owner:
                            send(deck.clear())
                        elif gou[1] == 'draw' :
                            send(deck.draw(sender[0], sender[1]))
                        elif gou[1] == 'show' and sender[0] == owner :
                            send(deck.show())
                        elif gou[1] == 'cont' and sender[0] == owner :
                            send(deck.contents())
                    except:
                        send('syntax: +deck <action>')
                else :
                    send('What the hell are you talking about, %s?' % sender[0])
                
                # Channel Commands
            except:
                send('What the hell are you talking about, %s?' % sender[0])
                
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
    rawsend("PRIVMSG %s :%s\r\n" % (n, 'Hello good peoples, I\'m the new and improved desabot'))
    print chan
    

while 1 :
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        break
        
    elif event.type == mousemo :
        x, y =  event.pos
        print x, y
    screen.fill((100, 100, 205))
    text = font.render('%s, %s' % (x ,y), True, (255,255, 255))
    
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    screen.blit(text, textRect)

    line(screen, (0, 0, 0), (0, 0), (x, y))
    line(screen, (255, 0, 0), (width, height), (x, y))
    line(screen, (0, 225, 0), (0, height), (x, y))
    line(screen, (0, 0, 225), (width, 0),   (x, y))
    line(screen, (0, 100, 200), (width, y), (0, y))
    line(screen, (0, 100, 40), (x, height), (x, 0))
    refresh()

    # Logging
    lineget = c.recv(4096); print lineget
    linedown = file("log.txt", "a")
    linedown.write(lineget)
    linedown.close()

    # Parse line for commads
    if lineget.find("PRIVMSG")!=-1 :
        parsemsg(lineget)
    if lineget.find('KICK #grubbn neodesabot')!=-1 :
        chan = '#grubbn'
        rawsend("JOIN %s\n" % (chan))
        rawsend("PRIVMSG %s :%s\r\n" % (chan, 'Hello good peoples, I\'m the new and improved desabot'))
    
    # Ping-Pong is a game of life or death
    lineget = lineget.rstrip()
    lineget = lineget.split()
    if lineget[0] == "PING" :
        c.send("PONG %s \n" % lineget[1])