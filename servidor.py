import xmlrpc.server

class MyServer:
    def add(self, a, b):
        return a + b
    
class Dealer:
    dealer_hand = [5, 8]

    def dealer_hand_sum():
        sum = 
        return dealer_hand.sum

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_instance(MyServer())
server.serve_forever()