import re
import sys
import os
from socket import *

def ProcessCommandFlags(args = sys.argv[1:]):
    """ProcessCommandFlags([args]) -> Return a list of present command flags"""
    flags   = {}
    rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
    roption = '--(?P<option>\S*)'               # --key
    r = '(' + rkeyval + ')|(' + roption + ')'
    rc = re.compile(r)
    for a in args:
        try:
            rcg = rc.search(a).groupdict()
            if rcg.has_key('key'):
                flags[rcg['key']] = rcg['value']
            if rcg.has_key('option'):
                flags[rcg['option']] = rcg['option']
        except AttributeError:
            return None
    return flags
#end def ProcessCommandFlags

class SockClient(object):
    """Handles message sending"""
    def __init__(self):
        self.host = raw_input("Please enter a host: ")
        self.port = 21567
        self.addr = (self.host, self.port)

        sock = None
        for res in getaddrinfo(self.host, self.port, AF_UNSPEC, SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                sock = socket(af, socktype, proto)
            except error, msg:
                sock = None
                continue
            try:
                sock.connect(sa)
            except error, msg:
                sock.close()
                sock = None
                continue
            break
        if sock is None:
            raise RuntimeError, "could not connect socket"
        
        self.sock = sock
        self.mainloop()
    def remotemsg(self,msg):
        if not self.sock.send(msg):
            raise SystemExit, "failed to send message to remote server"
        del msg
    def mainloop(self):
        while 1:
            msg = raw_input(">> ")
            if len(msg) > 1024:
                print "Message is too large. Max length is 1024 characters, you input %s characters." % (len(msg))
                continue
            self.remotemsg(msg)
    def close(self):
        self.sock.shutdown(SHUT_RDWR)
        self.sock.close()
#end class SockClient

class SockServer(object):
    def __init__(self):
        self.host = ''
        self.port = 21567
        self.addr = (self.host, self.port)
        self.buf = 1024
        
        sock = None
	for res in getaddrinfo(self.host, self.port, AF_UNSPEC, SOCK_STREAM, 0, AI_PASSIVE):
	    af, socktype, proto, canonname, sa = res
	    try:
		sock = socket(af, socktype, proto)
	    except error, msg:
		sock = None
		continue
	    try:
		sock.bind(sa)
		sock.listen(1)
	    except error, msg:
		sock.close()
		sock = None
		continue
	    break
        if sock is None:
            raise RuntimeError, "could not open socket"

        self.sock,addr = sock.accept()
        self.mainloop()
    def mainloop(self):
        while 1:
            data = self.sock.recv(self.buf)
            if not data:
                    print "Remote user has terminated the session."
                    break
            else:
                    print "remote_user:",data
                    del data
        self.close()
    def close(self):
        self.sock.shutdown(SHUT_RDWR)
        self.sock.close()
#end class SockServer