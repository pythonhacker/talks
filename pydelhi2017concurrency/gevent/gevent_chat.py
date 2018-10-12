""" Multiuser chat server using gevent """


import gevent
from gevent import monkey
from gevent import socket
from gevent.server import StreamServer

monkey.patch_all()

participants = set()

def new_chat_channel(conn, address):
    """ New chat channel for a given connection """

    participants.add(conn)
    data = conn.recv(1024)
    
    while data:
        print("Chat:", data.strip())
        for p in participants:
            try:
                if p is not conn:  
                    user, msg = data.split(':')
                    p.send('\n#[' + user + ']>>> says ' + msg)
            except socket.error as e:
                # ignore broken pipes, they just mean the participant
                # closed its connection already
                if e[0] != 32:
                    raise
        data = conn.recv(1024)

    participants.remove(conn)
    print("Participant left chat.")

if __name__ == "__main__":
    port = 3001
    try:
        print("ChatServer starting up on port", port)
        server = StreamServer(('0.0.0.0', port), new_chat_channel)
        server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        print("ChatServer exiting.")
