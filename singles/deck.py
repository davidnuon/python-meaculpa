import random as r
import sys
import os
import string
import textwrap as t

# The Card Set will be a 52 + Jokers Set

cardset = [
'A of Spades',
'2 of Spades',
'3 of Spades',
'4 of Spades',
'5 of Spades',
'6 of Spades',
'7 of Spades',
'8 of Spades',
'9 of Spades',
'10 of Spades',
'J of Spades',
'Q of Spades',
'K of Spades',
'A of Clubs',
'2 of Clubs',
'3 of Clubs',
'4 of Clubs',
'5 of Clubs',
'6 of Clubs',
'7 of Clubs',
'8 of Clubs',
'9 of Clubs',
'10 of Clubs',
'J of Clubs',
'Q of Clubs',
'K of Clubs',
'A of Hearts',
'2 of Hearts',
'3 of Hearts',
'4 of Hearts',
'5 of Hearts',
'6 of Hearts',
'7 of Hearts',
'8 of Hearts',
'9 of Hearts',
'10 of Hearts',
'J of Hearts',
'Q of Hearts',
'K of Hearts',
'A of Diamonds',
'2 of Diamonds',
'3 of Diamonds',
'4 of Diamonds',
'5 of Diamonds',
'6 of Diamonds',
'7 of Diamonds',
'8 of Diamonds',
'9 of Diamonds',
'10 of Diamonds',
'J of Diamonds',
'Q of Diamonds',
'K of Diamonds',
'Joker',
'Joker']

deck     = [] # The current deck
reversec = [] # Reverse (Face Down) Cards
openc    = [] # Open (Face Up) Cards
table    = [] # Cards on the table
hand     = [] # Cards you are holding
deck = cardset
r.shuffle(deck)

def term() :
    
    parse = raw_input('[H: %s]\[D: %s]\[T: %s] $ ' % (len(hand), len(deck), len(table)))
    arg   = parse.split(' ')
    cmd   = arg[0]
    
    if cmd == 'echo' :
        if parse[5:] == '' :
            print 'Syntax: echo <string>'
        else :
            print parse[5:]
    elif cmd == 'draw' :
        if len(deck) == 0 : print 'The deck is out of cards.\n'
        else :
            try :
                draws = int(arg[1])
                if draws > len(deck) : draws = len(deck)
                draws = '~'*draws
                for n in draws : 
                    hand[len(hand):] = [deck[0]]
                    print 'You drew The %s.' % deck[0]
                    deck[:] = deck[1:]
                print ''
            except(IndexError) :
                hand[len(hand):] = [deck[0]]
                print 'You drew The %s.\n' % deck[0]
                deck[:] = deck[1:]
            except(ValueError) :
                print 've'
                hand[len(hand):] = [deck[0]]
                print 'You drew The %s.\n' % deck[0]
                deck[:] = deck[1:]
    elif cmd == 'set' :
        if len(hand) == 0 : print '''You have no cards in your hand to place on the table'''
        else :
            try :
                if str(arg[1]).isdigit :
                    try :
                        ind = int(arg[1])
                        if arg[2] == 'open' :
                            table.append(str(hand[ind - 1]) + ':o')
                            print '%s has been set on the table.\n' % hand[ind -1]
                            hand.remove(hand[ind - 1])
                        elif arg[2] == 'reverse' :
                            table.append(str(hand[ind - 1]) + ':r')
                            print 'A reverse card has been set.\n'
                            hand.remove(hand[ind - 1])
                    except(IndexError) :
                        table.append(str(hand[ind - 1]) + ':o')
                        hand.remove(hand[ind - 1])
                    except(ValueError) : 
                        print 'Please input a valid number.'
                else :
                    print 'Please indicate the card to be set.'    
            except(IndexError) :
                print 'Please indicate the card to be set.'
    elif cmd in ['list','show'] :
        if arg[1] == 'hand' :    
            if len(hand) > 0 :
                c = 0
                handlist = ''
                for n in hand :
                    if c == 3 :
                        handlist = handlist + '\n'
                        c = 0
                    handlist = handlist + '%s, ' % n
                    c = c + 1
                print handlist[:-2]
                print '-'*25
                print 'Hand Count: %s\n' % len(hand) 
            else :
                print 'There aren\'t any cards in your hand.\n'
        if arg[1] == 'deck' :    
            if len(deck) > 0 :
                c = 0
                decklist = ''
                for n in deck:
                    if c == 3 :
                        decklist = decklist + '\n'
                        c = 0
                    decklist = decklist + '%s, ' % n
                    c = c + 1
                print decklist[:-2]
                print '-'*25
                print 'Deck Count: %s\n' % len(deck) 
            else :
                print 'There aren\'t any cards in the deck. \n'
        if arg[1] == 'table' :
            print table
    elif cmd in ['exit','quit','end'] :
        sys.exit()
    else :
        print 'Type in \'help\' for details.\n'
        
while 1 :
    term()
