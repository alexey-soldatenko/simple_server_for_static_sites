import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from server.server import WebServer

HOST = '127.0.0.1'
PORT = 8080

server = WebServer(HOST, PORT)
server.main_loop()
