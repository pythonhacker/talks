import socket
import select
import sys

class TwistedChatClient(object):
    """ Chat client with twisted chat server """

    def __init__(self, name, host='127.0.0.1', port=3490):
        self.name = name
        # Quit flag
        self.flag = False
        self.port = int(port)
        self.host = host
        # Initial prompt
        self.prompt='[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print('Connected to chat server@%d' % self.port)
        except socket.error as e:
            print('Could not connect to chat server @%d' % self.port)
            sys.exit(1)

    def chat(self):
        """ Main chat method """
        
        while not self.flag:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()

                # Wait for input from stdin & socket
                inputready, outputready,exceptrdy = select.select([0, self.sock], [],[])
                
                for i in inputready:
                    if i == 0:
                        data = sys.stdin.readline().strip()
                        if data: self.sock.send(self.name + ':' + data)
                    elif i == self.sock:
                        data = self.sock.recv(1024)
                        if not data:
                            print('Shutting down.')
                            self.flag = True
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
                            
            except KeyboardInterrupt:
                print('Interrupted.')
                self.sock.close()
                break
            
            
if __name__ == "__main__":

    if len(sys.argv)<3:
        sys.exit('Usage: %s chatid host portno' % sys.argv[0])
        
    client = TwistedChatClient(sys.argv[1],sys.argv[2], int(sys.argv[3]))
    client.chat()
