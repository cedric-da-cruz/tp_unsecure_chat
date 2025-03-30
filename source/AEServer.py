import msgpack  # On change pickle par msgpack
import logging
from simple_server import SimpleServer


#meme type que simple server
class AEServer(SimpleServer):
    def __init__(self, recv_port: int, broadcast_port: int) -> None:
        super().__init__(recv_port, broadcast_port)
        
        self._serial_function = msgpack.packb #qui remplace pickle dump precedemment
        self._deserial_function = msgpack.unpackb #qui remplace pickle load precedemment

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    server = AEServer(6666, 6667)
    
    try:
        while True:
            server.update()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()