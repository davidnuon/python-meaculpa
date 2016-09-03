# -*- coding: utf-8 -*-

import sys, traceback
import string
import socket
import os
import time
import random as r
from constants import *
deck = [
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
pdraw = []
#poll stuff
poll = [0, 0, 'Is this a poll?']
yvoters = []
nvoters = []
tvoters = []
dvoters = []
dgoal = ['']
players = []
splayers = []
ignore = []
gword = 'google'
hint = '000'

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
#TEXT FIND FOLLOWS:
# Anti Swearing
    if (msgpart.find('chainsaw')|msgpart.find('chainsaws')!=-1) :
        s.send("PRIVMSG %s :Mine is way bigger than yours  %s\r\n" % (info[2], sender[0]))
    if (msgpart.find(gword)!=-1) :
        s.send("PRIVMSG %s :%s has won! The word was %s !\r\n" % (info[2], sender[0], gword))
    if msgpart.find('über')!=-1 :
        s.send("PRIVMSG %s :Ja, es ist sehr gut,  %s\r\n" % (info[2], sender[0]))
    if msgpart.find('uber')!=-1 :
        s.send("PRIVMSG %s :Ja, es ist sehr gut,  %s\r\n" % (info[2], sender[0]))
# If saying hi
    if (msgpart.find('hi desabot')!=-1) | (msgpart.find('hello\
desabot')!=-1) | (msgpart.find('sup desabot')!=-1) | (msgpart.find('hey\
desabot')!=-1):
	   s.send("PRIVMSG %s :hello %s\r\n" % (info[2], sender[0]))
# If leaving
    if ((msgpart.find('bye')!=-1) | (msgpart.find('see yah')!=-1) |
(msgpart.find('later')!=-1) | (msgpart.find('goodbye')!=-1) |
(msgpart.find('g2g')!=-1) | (msgpart.find('gtg')!=-1)):
	   s.send("PRIVMSG %s :bye %s\r\n" % (info[2], sender[0]))
# If brb
    if (msgpart.find('brb')!=-1) | (msgpart.find('BRB')!=-1):
   	    s.send("PRIVMSG %s :k %s\r\n" % (info[2], sender[0]))

def factoids(cmd,channel,sender,receiver):
    if sender[0] in ignore :
        reply = 'I refuse to acknowledge the existence of %s.' % sender[0]
    else :
        print cmd
        reply = "%s I have no idea what you're talking about" % (sender[0])
#================= '=' commands follow: ========================================
        if cmd.find('join')!=-1 and sender[0] in (OWNER, ADMIN, ADMIN2):
           chan = cmd.split(' ')
           print cmd
           s.send('JOIN %s\r\n' % (chan[1]))
           reply = 'done'
        if cmd == 'part' and sender[0] in (OWNER, ADMIN, ADMIN2, MODE[0] == '+e'):
           s.send("PRIVMSG %s : Bye\r\n" % (channel))
           s.send('PART %s\r\n' % (channel))
#dance #########################################################################
        if cmd == 'dance':
    	    reply = 'ACTION dances'
#hint ########################################################################
        if cmd == 'clue' :
            reply = 'The hint is: %s' % hint
#chuck ########################################################################
        if cmd == "chuck" :
            r.shuffle(chucklist)
            reply = chucklist[0]
#lol ###########################################################################
        if cmd == "end" and sender[0] == OWNER:
            reply = 'I\'m off to sharpen my sadism claws...'
            s.send('QUIT \r\n')
#lol ###########################################################################
        if cmd == "lol" :
            reply = 'What\'s so funny ' + sender[0] + '?'
#hin ###########################################################################
        if cmd.startswith("hin ") | cmd.startswith("hin")== 1 :
            gou = cmd.split()
            try :
                if gou[1] != 'dn_desaku':
    	            reply = 'ACTION watches as %s burns to a crisp as giant fireballs hit him (or her) one by one.' % gou[1]
                if gou[1] != 'desabot':
    	            reply = 'ACTION watches as %s burns to a crisp as giant fireballs hit him (or her) one by one.' % sender[0]
                else :
    	            reply = 'No, ' + sender[0] + ' I will protect my master with my corpse.'
            except : 
    	       reply = 'No fires today...'
#sui ###########################################################################
        if cmd.startswith("sui ") | cmd.startswith("sui")== 1 :
            gou = cmd.split()
            try :
                if gou[1] == 'dn_desaku':
    	            reply = 'No, ' + sender[0] + ' I will protect my master with my corpse.'
                if gou[1] == 'desabot':
                    reply = 'ACTION watches as %s undergoes Chinese water torture. Watching, as every drop that falls on his forehead slowly kills him. ' % sender[0]
                if gou[1] == 'wtf':
                    reply = 'It is a very heinous way to execute someone. A very large container with a ball under it is placed resting on the victim\'s forehead. The person is obviously restrained so he cannot move. Then the container is filled with water one drop at a time. As hours then days pass, the weight of the container gets heavier and heavier until it crushes the person\'s skull, killing them.'
                else :
                   print 'No Chinese water torture.'
                   reply = 'ACTION watches as %s undergoes Chinese water tourture. Watching, as every drop that falls on his forehead slowly kills him. ' % gou[1]
            except : 
    	       reply = 'No tourture today...'
#=D ############################################################################
        if cmd.startswith("praise ") | cmd.startswith("praise")== 1 :
                gou = cmd.split()
                try :
                    if gou[1] != ' ' :
                        reply = 'You rock %s!' % gou[1]
                    else :
                        if gou[1] == 'desabot' :
                            reply = 'Thank you, %s' % sender[0]
                        else :
                            print 'wtf, how did I get here?'
                except :
                     if sender[0] != 'dn_desaku' :
                        reply = 'I\'m going to make sure it hurts when you pee ' + sender[0] + '.'
                     else :
                        reply = 'I know you love me, master.'
#mood ##########################################################################
        if cmd == 'mood' :
            mood = [ ')-_-)', '=D', ')><)', '=)', ':O', ')`_`)', ')=_=)',  ')0_0)', ')_o_)', ')T_T)', ')><)>[go away]', ')>_>)', ')*_*)', ')#_#)', ':F', 'You know what? I FEEL GRRREAT!! Now get the hell out of my sight =D %s' % sender[0] ]
            r.shuffle(mood)
            reply = mood[0]
#apol ##########################################################################
        if cmd == 'apol' :
                if sender[0] != 'dn_desaku':
                    reply = 'I\'m sorry, everbody. And ' + sender[0] + ', I\'m sorry I attacked you while you weren\'t looking. I know that I should\'ve done it while you and I were facing face to face.'
                else:
                    reply = 'I\'m sorry for all the pain I have caused everybody'
#call ##########################################################################
        if cmd.startswith("call ") | cmd.startswith("call")== 1 :
            gou = cmd.split()
            try :
                if gou[1] == 'title' :
                    r.shuffle(persons)
                    reply = persons[0]
                if gou[1] == 'now' :
                    g = time.localtime()
                    print g
                    reply = 'The date is: ' + str(g[1]) + '/' + str(g[2]) + '/' + str(g[0]) + ' and time is: ' + str(g[3]) + ':' + str(g[4])
                if gou[1] == 'poll' :
                        print poll
                        print 3
                        yes = poll[0]
                        no = poll[1]
                        que = poll[2]
                        reply = '"%s" Yes : %s - No : %s' % (que,yes,no)
                if gou[1] == 'voters' :
                    if tvoters != [] :
                            print yvoters
                            print nvoters
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
                            reply = 'Yes : %s - No : %s' % (ye,ne)
                    else :
                            reply = 'Nobody has voted yet.'
            except :
                reply = "The call was not answered"
#ls ############################################################################
        if cmd.startswith("ls ") | cmd.startswith("ls")== 1 :
            gou = cmd.split()
            try :
                reply = os.popen('cmd.exe /c dir').read().replace('\n', ' ')
            except :
                reply = "The call was not answered"
#gnu ###########################################################################
        if cmd.startswith("gnu ") | cmd.startswith("gun")== 1 :
                gou = cmd.split()
                try :
                    reply = 'GNU/' + gou[1]
                except :
                    reply = sender[0] + " , you are not American, you are French!"
##hug ##########################################################################
        if cmd.startswith("hug ") | cmd.startswith("hug")== 1 :
                   gou = cmd.split()
                   try :
                       reply = 'ACTION hugs %s' % gou[1]
                   except :
                       reply = sender[0] + " , can I hug you?"
#slap ##########################################################################
        if cmd.startswith("slap ") | cmd.startswith("slap")== 1 :
                   gou = cmd.split()
                   try :
                       reply = 'ACTION slaps a large trout about with %s' % gou[1]
                   except :
                       reply = sender[0] + " , can I hug you?"
#random death ##################################################################
        if cmd.startswith("ü ") | cmd.startswith("ü")== 1 :
                   gou = cmd.split()
                   try :
                       r.shuffle(death)
                       if gou[1] == 'dn_desaku' :
                           reply = 'Meh, he\'ll be fine'
                       else :
                          reply = gou[1] + death[0]
                   except :
                       reply = sender[0] + " , can I hug you?"
#ignore ########################################################################
        if cmd.startswith("ignore" ) | cmd.startswith("ignore ") == 1 and sender[0] == OWNER :
                    gou = cmd.split()
                    try :
                        if gou[1] == 'add' :
                                cmd = cmd.replace('ignore add ', '')
                                if cmd == OWNER :
                                    reply = 'I will not ignore my master.'
                                else :
                                    ignore.append(cmd)
                                    reply = '%s will be ignored.' % cmd
                        if gou[1] == 'rm' :
                            cmd = cmd.replace('ignore rm ', '')
                            ignore.remove(cmd)
                            reply = '%s will no longer be ignored.' % cmd
                    except :
                        reply = 'Who shall I ignore?'                            
#üa ############################################################################
        if cmd.startswith("üa ") | cmd.startswith("üa")== 1 :
                   gou = cmd.split()
                   try :
                       r.shuffle(death)
                       if gou[1] == 'dn_desaku' :
                           reply = 'Meh, he\'ll be fine, in America.'
                       else :
                          reply = gou[1] + death[0] + ' In America.'
                   except :
                       reply = sender[0] + " , you are French and you fail D:<."
#feed ##########################################################################
        if cmd.startswith("feed") | cmd.startswith("feed ")== 1 :
                    gou = cmd.split()
                    try :
                         if  gou[1] != 'pho' :
                             koi = cmd.replace('feed ', '')
                             reply = 'Nasty, ' + koi + ' tastes like crap.'
                         elif gou[1] == 'dn_desaku' :
                             reply = 'I will not eat my master.'
                         elif gou [1] == 'blood' :
                             reply = 'Yummy, licking blood off of chainsaw blades is fun.'
                         else :
                             reply = 'Yummy, Pho is my favorite :)'
                    except :
                        reply = 'Feed me!'
                        print 'error'
#eat ###########################################################################
        if cmd.startswith("eat") | cmd.startswith("eat ") == 1:
                    koi = cmd.replace('eat ','')
                    try :
                        if koi != '' :
                            print koi
                            reply = 'ACTION eats every bit of %s' % koi
                        else :
                            reply = 'I\'m not hungry'
                    except :
                        reply = 'I\'m not hungry'
#oits #########################################################################
        if cmd.startswith("oits") | cmd.startswith("oits ") == 1:
                    gou = cmd.split()
                    try:
                        if gou[1] != ' ' :
                            word = gou[1]
                            cc = len(word)
                            thing = []
                            a = 0
                            f = 0
                            nuword = ''
                            while a < cc :
                                thing.append(word[a])
                                a = a + 1
                                print thing
                            r.shuffle(thing)
                            print thing
                            while f < cc :
                                nuword = nuword + thing[f]
                                f = f + 1
                                print nuword
                            reply = nuword
                    except:
                        reply = 'Please enter a word to mix'
#saw ###########################################################################
        if cmd.startswith("saw ") | cmd.startswith("saw")== 1 :
                check = ['saw', '']
                gou = cmd.split()
                cmdl = cmd.lower()
                try :
                    if cmdl.find('desabot') != -1 :
                        reply = 'NO. I will kill you myself. I will hunt you down, chainsaw you and drink your blood like summer Kool-aid ' + sender[0] + '.'
                    elif cmdl.find('me') != -1 :
                        if sender[0] != 'dn_desaku' :
                            reply = 'I will gladly take your life and drink your tears with a straw ' + sender[0] + '.'
                        else :
                            reply = 'No, dude I will not kill you.'
                    elif cmdl.find('owner') != -1 :
                        reply = 'You sick bastard, I will not chainsaw my master. Instead, I will go after you ' + sender[0] + '.'
                    elif cmdl.find('master') != -1 :
                        reply = 'You sick bastard, I will not chainsaw my master. Instead, I will go after you ' + sender[0] + '.'
                    elif cmdl.find('dn_desaku') == -1 :
                        koi = cmd.replace('saw ', '')
                        if koi in check :
                            pass
                        else :
                            reply = 'It will be my pleasure to chainsaw ' + koi + ' for you ' + sender[0] + '.'
                    else :
                        reply = 'You sick bastard, I will not chainsaw my master. Instead, I will go after you ' + sender[0] + '.'
                except :
                     if sender[0] != 'dn_desaku' :
                        reply = 'If you don\'t tell me a target, I will saw you in half and lap up your blood ' + sender[0] + '.'
                     else :
                        reply = 'I\'m waiting...'
#punish ########################################################################
        if cmd == 'punish' :
                if sender[0] == OWNER :
                   reply = 'Yes master, I will accept my punishment'
                else :
                   reply = 'I will throw hot tar on you, %s.' % sender[0]
#neo ########################################################################
        if cmd == 'neodesabot' :
                if sender[0] == OWNER :
                   reply = 'Yes, I cannot wait unit you improve me.'
                else :
                   reply = '%s, I\'ll make sure I give you my old chainsaws =D' % sender[0]
#debug #########################################################################
        if cmd == 'de' :
                print 'Owner: ',OWNER
                print 'Ignore list: ',ignore
                print 'Card players whois info: ',players
                print 'Card players: ',splayers
                print 'Last draw: ',pdraw 
                print 'Draw goal: ',dgoal[0]
                print 'Sender Info: ',sender
                print 'Poll Info: ',poll
                print 'Yes Count: ',poll[0]
                print 'No Count: ',poll[1]
                print 'Question: ',poll[2]
                print 'Yes Voters: ',yvoters
                print 'No Voters: ',nvoters
                print 'Sans List ',tvoters
                print 'Debug Voters ',dvoters
                if sender[0] != OWNER :
                    reply = 'That tickles. =D I\'ll make sure your death is very pleasurable.'
                else :
                    reply = 'Checkup complete.'
#poll ####################################################################
        if cmd.startswith('poll') | cmd.startswith('poll ') :
                gou = cmd.split()
                try :
                    if gou[1] == 'set' and sender[0] == OWNER :
                        print poll #behold, debug!
                        print poll[2]
                        cmd = cmd.replace('poll set ', '')
                        poll[2] = cmd
                        reply = 'Poll topic set.'
                    if gou[1] == 'reset' and sender[0] == OWNER : 
                        print 'Ignore list: ',ignore
                        print 'Poll Info: ',poll
                        print 'Yes Count: ',poll[0]
                        print 'No Count: ',poll[1]
                        print 'Question: ',poll[2]
                        print 'Yes Voters: ',yvoters
                        print 'No Voters: ',nvoters
                        print 'Sans List ',tvoters
                        print 'Debug Voters ',dvoters
                        yvoters[:] = []
                        nvoters[:] = []
                        tvoters[:] = []
                        poll[0] = 0 
                        poll[1] = 0
                        reply = 'Poll reset.'
                    if gou[1] == 'yes' :
                        try :
                            tvoters.index(sender[1])
                            reply = 'You sick bastard, you tried voting twice'
                            print 'lol %s is a bastard' % sender[0]
                            print 1.5
                        except :
                            poll[0] = poll[0] + 1
                            print poll
                            print 1
                            reply = 'Your poll has been counted %s. You have voted yes for "%s."' % (sender[0], poll[2])
                            yvoters.append(sender[0])
                            print 'add to yes'
                            tvoters.append(sender[1])
                            print 'add to main sans-list'
                    if gou[1] == 'no' :
                        try :
                            tvoters.index(sender[1])
                            reply = 'You sick bastard, you tried voting twice'
                            print 'lol %s is a bastard' % sender[0]
                            print 2.5
                        except :
                            poll[1] = poll[1] + 1
                            print poll
                            print 2
                            reply = 'Your poll has been counted %s. You have voted no for "%s."' % (sender[0], poll[2])
                            nvoters.append(sender[0])
                            print 'add to yes'
                            tvoters.append(sender[1])
                            print 'add to main sans-list'
                    if gou[1] == 'call' :
                        print poll
                        print 3
                        yes = poll[0]
                        no = poll[1]
                        que = poll[2]
                        reply = '"%s" Yes : %s - No : %s' % (que,yes,no)
                    if gou[1] == 'voters' :
                     if tvoters != [] :
                            print yvoters
                            print nvoters
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
                            reply = 'Yes : %s - No : %s' % (ye,ne)
                     else :
                            reply = 'Nobody has voted yet.'
                except :
                    reply = 'Enter a valid command please.'
#cards game ####################################################################
        if cmd.startswith("deck ") | cmd.startswith("deck")== 1 :
                gou = cmd.split() 
                try:
                    if gou[1] == 'shuffle' and sender[0] == OWNER :
                        r.shuffle(deck)
                        reply = 'Deck Shuffled.'
                    if gou[1] == 'reload' and sender[0] == OWNER :
                        deck[:] = ddeck
                        reply = 'Deck reloaded'
                    if gou[1] == 'set' and sender[0] == OWNER :
                        cmd = cmd.replace('deck set ', '')
                        try :
                             ddeck.index(cmd)
                             dgoal[0] = cmd
                             print cmd
                             reply = 'GOAL, SET: %s is the goal!' % cmd
                        except :
                             reply = 'The card %s was not found' % cmd
                    if gou[1] == 'players' :
                            print splayers
                            ye = str(splayers)
                            ye = str(ye).lstrip('[')
                            ye = str(ye)[0:-1]
                            if splayers == [] :
                                 ye = 'nobody'
                            reply = 'Current players : %s' % ye
                    if gou[1] == 'add'  :
                        try :
                            players.index(sender[1])
                            reply = '%s, you have already registered.' % sender[0]
                        except :
                            players.append(sender[1])
                            splayers.append(sender[0])
                            reply = '%s, added to playlist.' % sender[0]
                    if gou[1] == 'rm' :
                        try :
                            players.remove(sender[1])
                            splayers.remove(sender[0])
                            reply = '%s, you have been erased.' % sender[0]
                        except :
                            reply = '%s, you weren\'t playing.' % sender[0]
                    if gou[1] == 'clear' and sender[0] == OWNER:
                            players[:] = []
                            splayers[:] = []
                            reply = 'Players list cleared.'
                    if gou[1] == 'draw' :
                        if sender[1] in players :
                            try:
                                try:
                                    pdraw.index(sender[1])
                                    reply = 'You sick bastard, you tried to draw twice.'
                                    print '%s is a bastard.' % sender[0]
                                except:
                                    if deck[0] != dgoal[0] :
                                        reply = '%s drew %s' % (sender[0],deck[0])
                                        print '%s drew a card.' % sender[0]
                                        deck.remove(str(deck[0]))
                                        pdraw[:] = []
                                        pdraw.append(sender[1])
                                    else:
                                        reply = '%s drew %s, he wins!' % (sender[0],dgoal[0])
                                        print '%s won.' % sender[0]
                                        deck.remove(str(deck[0]))
                                        pdraw[:] = []
                                        pdraw.append(sender[1])
                            except :
                                        print 1
                                        print "Exception in user code:"
                                        print '-'*60
                                        traceback.print_exc(file=sys.stdout)
                                        print '-'*60
                                        reply = 'There aren\'t any cards in the deck =('
                        else :
                            reply = 'You sick bastard, you can\'t play.'
                    if gou[1] == 'show' and sender[0] == OWNER :
                        try : 
                            reply = '%s was on top of the deck.' % str(deck[0])
                        except :
                            reply = 'There aren\'t any cards in the deck =('
                    if gou[1] == 'cont' and sender[0] == OWNER :
                        try :
                            print deck
                            ye = str(deck)
                            ye = str(ye).lstrip('[')
                            ye = str(ye).lstrip('\'')
                            ye = str(ye)[0:-1]
                            reply = 'Deck Contents: %s.' % str(ye)
                        except :
                            reply = 'There aren\'t any cards in the deck =('
                except:
                    reply = 'syntax: =deck <action>'
################################################################################
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
    if line[0] == 'PING':
    	s.send('PONG %s \n' %line[1])