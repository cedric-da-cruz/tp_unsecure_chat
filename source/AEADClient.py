from AEClient import AEClient

class AEADClient(AEClient):
    def encrypt_message(self, password: str, message: str) -> tuple[bytes, bytes]:
        tagged_message = f"[{self._nick}] {message}"
        return super().encrypt_message(password, tagged_message)
    
    def decrypt_message(self, password: str, encrypted_message: bytes, salt: bytes, nick: str) -> str:
        decrypted = super().decrypt_message(password, encrypted_message, salt, nick)

        expected_prefix = f"[{nick}] "
        if not decrypted.startswith(expected_prefix):
            return "[AEAD WARNING: message modifié ou corrompu]"

        return decrypted[len(expected_prefix):]  

if __name__ == "__main__":
    import logging
    from names_generator import generate_name

    logging.basicConfig(level=logging.DEBUG)
    client = AEADClient("localhost", 6666, 6667, generate_name(), "Best_Secr3t_ever_!")
    client.run()