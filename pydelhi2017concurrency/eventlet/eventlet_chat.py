# eventlet_chat.py
# Multi chat server using eventlet

import eventlet
from eventlet.green import socket

participants = set()

def new_chat_channel(conn):
    """ New chat channel for a given connection """
    
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
        server = eventlet.listen(('0.0.0.0', port))

        while True:
            new_connection, address = server.accept()
            print("Participant joined chat.")
            participants.add(new_connection)
            print(eventlet.spawn(new_chat_channel,
                                 new_connection))
    except (KeyboardInterrupt, SystemExit):
        print("ChatServer exiting.")
