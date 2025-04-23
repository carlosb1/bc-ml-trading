# client.py
import zmq
import os
import dotenv

dotenv.load_dotenv()

zmq_port = os.getenv('ZMQ_PORT', 5555)
print("Using port {}".format(zmq_port))
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://0.0.0.0:{zmq_port}")  # assumes a server is running

while True:
    print("Waiting for message...")
    msg = socket.recv_string()
    print("Received:", msg)
    socket.send_string("previsioned!")
    print("Sent reply.")