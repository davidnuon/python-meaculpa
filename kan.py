ken = ['this', 'is', 'a', 'test']

def tan(test):
   return test + str(len(test))


import random
import string

password = lambda x: "".join(random.choice(string.punctuation + string.letters
                + string.digits) for i in xrange(x))
                
gan = lambda x : "".join(str(x) for i in xrange(x))

print password(3)
print gan(3)
map(print, ken)