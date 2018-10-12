# twisted_chat_server.py
        
from twisted.internet import protocol, reactor

transports = {}

class Chat(protocol.Protocol):
    """ Chat protocol """

    def connectionMade(self):
        self._peer = self.transport.getPeer()

    def dataReceived(self, data):
        user, msg = data.split(":")
        transports[user] = self.transport

        for key in transports.keys():
            if key != msg:
                transports[key].write('\n#[' + user + "]>>> " + msg)

class ChatFactory(protocol.Factory):
    """ Chat protocol factory """
    
    def buildProtocol(self, addr):
        return Chat()

if __name__ == "__main__":
    reactor.listenTCP(3490, ChatFactory())
    reactor.run()
