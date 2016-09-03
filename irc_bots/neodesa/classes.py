from neodesa import polldata

# Some Neo Testing
        
class Neo :
    print 'Class Neo, confirmed'
        
    def status(self) :
        return 'I\'m not complete yet...'

# Saws...bzz..bzz
        
class Saw :
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
                         
class Deck :
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
             reply = 'GOAL, SET: %s is the goal!' % goal
        except :
             reply = 'The card %s was not found' % goal
    
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
                        thedeck.remove(str(thedeck[0]))
                        pdraw[:] = []
                        pdraw.append(whois)
                        return '%s drew %s' % (name, thedeck[0])
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