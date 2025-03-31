import msgpack
import logging
from AEServer import AEServer

class RogueServer(AEServer):
    def __init__(self, recv_port: int, broadcast_port: int) -> None:
        super().__init__(recv_port, broadcast_port)
        self._serial_function = msgpack.packb
        self._deserial_function = msgpack.unpackb
        logging.basicConfig(level=logging.DEBUG)

    def on_message(self, packet: bytes, frame: dict):
        """ Intercepte et modifie les messages avant de les renvoyer """
        if frame["nick"] not in self._clients:
            self._log.error(f"Client '{frame['nick']}' n'est pas connecté, impossible d'envoyer le message.")
            return None, self._serial_function({"response": "ko"})

        logging.info(f"Message avant modification : {frame.get('message', '')}")

        try:
            if "message" in frame:

                original_message = frame["message"]["encrypted_message"]

                modified_message = f"{original_message}{hex.encode("message modifié ahah")} "

                frame["message"]["encrypted_message"] = modified_message

            modified_packet = self._serial_function(frame)
            
            return modified_packet, self._serial_function({"response": "ok"})
        
        except Exception as e:
            self._log.error(f"Erreur lors de la modification du message : {e}")
            return None, self._serial_function({"response": "ko"})

if __name__ == "__main__":
    server = RogueServer(6666, 6667)

    try:
        logging.info("Attente de messages...")
        while True:
            server.update()
    except KeyboardInterrupt:
        logging.info("Extinction du serveur")
    finally:
        server.close()