from std import *

if __name__ == '__main__':
    flags = ProcessCommandFlags()
    if flags.has_key('server'):
        socket = SockServer()
    elif flags.has_key('client'):
        socket = SockClient()
    else:
        print \
        """
chat [OPTION]

    --server - Run chat server
    --client - run chat client
        """
