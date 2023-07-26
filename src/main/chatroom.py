import argparse
import textwrap
from server import Server
from client import Client

class ChatRoom:
    ''' Implements a little chatroom within the LAN.'''

    def __init__(self, args):
        self.args = args

    def launch(self):
        pass

    def create_server(self):
        pass

    def create_client(self):
        pass

def parse(sysargs):
    ''' Present the the interface options.'''
    parser = argparse.ArgumentParser(
        description='chatroom',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            chatroom.py -t 192.168.1.108 -p 5555 -l # Initialize a new chatroom with the specified address.
            chatroom.py -t 192.168.1.108 -p 5555 # connect to server.
        '''))
    parser.add_argument('-l', '--listen', action='store_true', help='Listen for incomming conections')
    parser.add_argument('-p', '--port', type=int, default=5555, help='Specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='Specified IP')
    return parser.parse_args(sysargs)

if __name__ == '__main__':
    args = parse(sys.argv[1:])
    chatroom = ChatRoom()
