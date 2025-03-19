import zmq
import json

def listen_to_chat():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:6667")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")  # S'abonner à tous les messages

    print("Listening to all messages...")
    while True:
        try:
            # Recevoir le message sous forme de bytes
            message_bytes = socket.recv()
            print(f"Received : {message_bytes}")
        except zmq.ZMQError as e:
            print(f"Error receiving message: {e}")
            break

if __name__ == "__main__":
    listen_to_chat()